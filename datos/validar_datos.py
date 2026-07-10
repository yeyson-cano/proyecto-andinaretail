"""
Validador reproducible de datos sinteticos para AndinaRetail S.A.C.

Tarea: [Datos] Implementar validacion de integridad y escenarios.

Entradas:
- config/escenarios.yaml
- datos/tiendas.csv
- datos/productos.csv
- datos/clientes.csv
- datos/ventas.csv
- datos/inventario.csv

Salida:
- resultados/reporte_validacion_datos.txt
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List

import numpy as np
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "escenarios.yaml"
RESULTS_DIR = ROOT / "resultados"
REPORT_PATH = RESULTS_DIR / "reporte_validacion_datos.txt"


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader que falla si encuentra claves duplicadas en el mismo nivel."""


def construct_mapping_no_duplicates(
    loader: UniqueKeyLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict:
    mapping = {}

    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)

        if key in mapping:
            raise ValueError(
                f"Clave duplicada en config/escenarios.yaml: {key!r}. "
                "Revise el YAML antes de ejecutar el validador."
            )

        value = loader.construct_object(value_node, deep=deep)
        mapping[key] = value

    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping_no_duplicates,
)


@dataclass
class ResultadoValidacion:
    oks: List[str] = field(default_factory=list)
    advertencias: List[str] = field(default_factory=list)
    errores: List[str] = field(default_factory=list)

    def ok(self, mensaje: str) -> None:
        self.oks.append(mensaje)

    def warn(self, mensaje: str) -> None:
        self.advertencias.append(mensaje)

    def error(self, mensaje: str) -> None:
        self.errores.append(mensaje)

    def validar(self, condicion: bool, ok_msg: str, error_msg: str) -> None:
        if bool(condicion):
            self.ok(ok_msg)
        else:
            self.error(error_msg)

    @property
    def aprobado(self) -> bool:
        return len(self.errores) == 0


def cargar_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"No se encontro el archivo de configuracion: {path}")

    with path.open("r", encoding="utf-8") as file:
        config = yaml.load(file, Loader=UniqueKeyLoader)

    if not isinstance(config, dict):
        raise ValueError("El archivo YAML no se cargo como diccionario.")

    return config


def cargar_csv(config: Dict[str, Any], resultado: ResultadoValidacion) -> Dict[str, pd.DataFrame]:
    directorio = ROOT / config["salidas"]["directorio"]
    archivos = config["salidas"]["archivos"]

    tablas: Dict[str, pd.DataFrame] = {}

    for nombre_tabla, archivo in archivos.items():
        ruta = directorio / archivo

        if not ruta.exists():
            resultado.error(f"No existe el archivo requerido: {ruta.relative_to(ROOT)}")
            continue

        tablas[nombre_tabla] = pd.read_csv(ruta, encoding="utf-8")
        resultado.ok(f"Archivo cargado: {ruta.relative_to(ROOT)} ({len(tablas[nombre_tabla]):,} filas)")

    return tablas


def porcentaje_en_rango(valor_pct: float, rango: Iterable[float], tolerancia: float = 1e-9) -> bool:
    minimo, maximo = list(rango)
    return float(minimo) - tolerancia <= float(valor_pct) <= float(maximo) + tolerancia


def format_pct(valor: float) -> str:
    return f"{valor:.2f}%"


def porcentaje_en_rango_con_tolerancia_pp(
    valor_pct: float,
    rango: Iterable[float],
    tolerancia_pp: float = 0.25,
) -> bool:
    minimo, maximo = list(rango)
    return float(minimo) - tolerancia_pp <= float(valor_pct) <= float(maximo) + tolerancia_pp


def columnas_requeridas() -> Dict[str, List[str]]:
    return {
        "tiendas": [
            "id_tienda", "nombre", "tipo", "canal", "ciudad", "region",
            "area_m2", "fecha_apertura",
        ],
        "productos": [
            "id_producto", "nombre", "categoria", "subcategoria", "marca",
            "precio_lista", "costo_unitario", "fecha_alta",
        ],
        "clientes": [
            "id_cliente", "nombre", "edad", "genero", "ciudad", "distrito",
            "fecha_registro", "canal_preferido", "segmento",
        ],
        "ventas": [
            "id_linea", "id_venta", "fecha", "id_cliente", "id_tienda",
            "id_producto", "cantidad", "precio_unitario", "descuento_pct",
            "monto_total", "canal", "metodo_pago",
        ],
        "inventario": [
            "id_producto", "id_tienda", "periodo", "stock_inicial",
            "unidades_vendidas", "reabastecimiento", "stock_final",
            "costo_almacenamiento",
        ],
    }


def validar_columnas(tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    for tabla, columnas in columnas_requeridas().items():
        if tabla not in tablas:
            continue

        faltantes = [col for col in columnas if col not in tablas[tabla].columns]

        resultado.validar(
            not faltantes,
            f"{tabla}: columnas requeridas presentes.",
            f"{tabla}: faltan columnas requeridas: {faltantes}",
        )


def validar_claves_primarias(tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    claves = {
        "tiendas": ["id_tienda"],
        "productos": ["id_producto"],
        "clientes": ["id_cliente"],
        "ventas": ["id_linea"],
        "inventario": ["id_producto", "id_tienda", "periodo"],
    }

    for tabla, columnas in claves.items():
        if tabla not in tablas:
            continue

        df = tablas[tabla]
        nulos = int(df[columnas].isna().any(axis=1).sum())
        duplicados = int(df.duplicated(columnas).sum())

        resultado.validar(
            nulos == 0,
            f"{tabla}: clave primaria sin nulos.",
            f"{tabla}: clave primaria con {nulos:,} filas nulas.",
        )

        resultado.validar(
            duplicados == 0,
            f"{tabla}: clave primaria unica.",
            f"{tabla}: clave primaria con {duplicados:,} duplicados.",
        )


def validar_claves_foraneas(tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    ventas = tablas["ventas"]
    inventario = tablas["inventario"]
    tiendas = tablas["tiendas"]
    productos = tablas["productos"]
    clientes = tablas["clientes"]

    ids_tiendas = set(tiendas["id_tienda"].astype(str))
    ids_productos = set(productos["id_producto"].astype(str))
    ids_clientes = set(clientes["id_cliente"].astype(str))

    reglas = [
        ("ventas.id_tienda", set(ventas["id_tienda"].astype(str)), ids_tiendas),
        ("ventas.id_producto", set(ventas["id_producto"].astype(str)), ids_productos),
        ("ventas.id_cliente", set(ventas["id_cliente"].astype(str)), ids_clientes),
        ("inventario.id_tienda", set(inventario["id_tienda"].astype(str)), ids_tiendas),
        ("inventario.id_producto", set(inventario["id_producto"].astype(str)), ids_productos),
    ]

    for nombre, valores, referencia in reglas:
        huerfanas = valores - referencia

        resultado.validar(
            len(huerfanas) == 0,
            f"{nombre}: sin claves foraneas huerfanas.",
            f"{nombre}: contiene claves huerfanas. Ejemplos: {sorted(list(huerfanas))[:10]}",
        )


def validar_nulos_permitidos(config: Dict[str, Any], tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    campos_faltantes = config["calidad_datos"]["faltantes"]["campos_permitidos"]

    permitidos_por_tabla = {
        "tiendas": {"ciudad", "region", "area_m2"},
        "productos": set(campos_faltantes.get("productos", [])),
        "clientes": set(campos_faltantes.get("clientes", [])),
        "ventas": set(),
        "inventario": set(),
    }

    for tabla, df in tablas.items():
        permitidos = permitidos_por_tabla.get(tabla, set())
        columnas_no_permitidas = [col for col in df.columns if col not in permitidos]
        nulos_no_permitidos = int(df[columnas_no_permitidas].isna().sum().sum())

        resultado.validar(
            nulos_no_permitidos == 0,
            f"{tabla}: sin nulos fuera de campos permitidos.",
            f"{tabla}: contiene {nulos_no_permitidos:,} nulos fuera de campos permitidos.",
        )


def validar_dominios_y_rangos(
    config: Dict[str, Any],
    tablas: Dict[str, pd.DataFrame],
    resultado: ResultadoValidacion,
) -> None:
    dominios = config["dominios"]
    inicio = pd.Timestamp(config["periodo"]["inicio"])
    fin = pd.Timestamp(config["periodo"]["fin"])

    tiendas = tablas["tiendas"].copy()
    productos = tablas["productos"].copy()
    clientes = tablas["clientes"].copy()
    ventas = tablas["ventas"].copy()
    inventario = tablas["inventario"].copy()

    tipos_validos = set(dominios["tipos_tienda"])
    canales_validos = set(dominios["canales"])
    ciudades_validas = set(dominios["ciudades"])
    regiones_validas = set(dominios["regiones"])
    categorias_validas = set(dominios["categorias"])
    metodos_validos = set(dominios["metodos_pago"])
    segmentos_validos = set(dominios["segmentos_comerciales"])
    generos_validos = set(config["clientes"]["distribucion_genero"].keys())

    resultado.validar(
        set(tiendas["tipo"].dropna()).issubset(tipos_validos),
        "tiendas.tipo: dominio valido.",
        "tiendas.tipo: contiene valores fuera del dominio.",
    )

    resultado.validar(
        set(tiendas["canal"].dropna()).issubset(canales_validos),
        "tiendas.canal: dominio valido.",
        "tiendas.canal: contiene valores fuera del dominio.",
    )

    tiendas_fisicas = tiendas["tipo"].eq("Fisica")
    tiendas_virtuales = tiendas["tipo"].eq("Virtual")

    resultado.validar(
        tiendas.loc[tiendas_fisicas, ["ciudad", "region", "area_m2"]].notna().all().all(),
        "tiendas fisicas: ciudad, region y area_m2 informados.",
        "tiendas fisicas: existen nulos en ciudad, region o area_m2.",
    )

    resultado.validar(
        tiendas.loc[tiendas_fisicas, "canal"].eq("Tienda").all(),
        "tiendas fisicas: canal Tienda.",
        "tiendas fisicas: canal distinto de Tienda.",
    )

    resultado.validar(
        (pd.to_numeric(tiendas.loc[tiendas_fisicas, "area_m2"], errors="coerce") > 0).all(),
        "tiendas fisicas: area_m2 mayor que cero.",
        "tiendas fisicas: area_m2 no positivo o no numerico.",
    )

    resultado.validar(
        tiendas.loc[tiendas_virtuales, ["ciudad", "region", "area_m2"]].isna().all().all(),
        "tiendas virtuales: nulos estructurales validos.",
        "tiendas virtuales: ciudad, region o area_m2 deberian ser nulos.",
    )

    resultado.validar(
        set(tiendas.loc[tiendas_virtuales, "canal"]).issubset({"Web", "App"}),
        "tiendas virtuales: canales Web/App.",
        "tiendas virtuales: canal distinto de Web/App.",
    )

    resultado.validar(
        set(tiendas.loc[tiendas["ciudad"].notna(), "ciudad"]).issubset(ciudades_validas)
        and set(tiendas.loc[tiendas["region"].notna(), "region"]).issubset(regiones_validas),
        "tiendas: ciudad y region dentro de dominios.",
        "tiendas: ciudad o region fuera de dominios.",
    )

    resultado.validar(
        set(productos["categoria"].dropna()).issubset(categorias_validas),
        "productos.categoria: dominio valido.",
        "productos.categoria: contiene valores fuera del dominio.",
    )

    resultado.validar(
        (pd.to_numeric(productos["precio_lista"], errors="coerce") > 0).all(),
        "productos.precio_lista: positivo.",
        "productos.precio_lista: contiene valores no positivos o no numericos.",
    )

    resultado.validar(
        (pd.to_numeric(productos["costo_unitario"], errors="coerce") > 0).all(),
        "productos.costo_unitario: positivo.",
        "productos.costo_unitario: contiene valores no positivos o no numericos.",
    )

    resultado.validar(
        (
            pd.to_numeric(productos["costo_unitario"], errors="coerce")
            < pd.to_numeric(productos["precio_lista"], errors="coerce")
        ).all(),
        "productos: costo_unitario menor que precio_lista.",
        "productos: costo_unitario no es menor que precio_lista en todas las filas.",
    )

    productos_fecha = pd.to_datetime(productos["fecha_alta"], errors="coerce")

    resultado.validar(
        productos_fecha.notna().all() and (productos_fecha <= fin).all(),
        "productos.fecha_alta: fechas validas.",
        "productos.fecha_alta: fechas invalidas o posteriores al fin del periodo.",
    )

    for categoria, subcategorias in dominios["subcategorias_por_categoria"].items():
        mascara = productos["categoria"].eq(categoria) & productos["subcategoria"].notna()
        fuera = ~productos.loc[mascara, "subcategoria"].isin(subcategorias)

        resultado.validar(
            not fuera.any(),
            f"productos.subcategoria: dominio valido para {categoria}.",
            f"productos.subcategoria: valores fuera de catalogo para {categoria}.",
        )

    for categoria, marcas in dominios["marcas_ficticias_por_categoria"].items():
        mascara = productos["categoria"].eq(categoria) & productos["marca"].notna()
        fuera = ~productos.loc[mascara, "marca"].isin(marcas)

        resultado.validar(
            not fuera.any(),
            f"productos.marca: dominio valido para {categoria}.",
            f"productos.marca: valores fuera de catalogo para {categoria}.",
        )

    edad = pd.to_numeric(clientes["edad"], errors="coerce")
    edad_no_nula = edad[clientes["edad"].notna()]
    cfg_edad = config["clientes"]["edad"]

    resultado.validar(
        edad_no_nula.between(int(cfg_edad["minima"]), int(cfg_edad["maxima"])).all(),
        "clientes.edad: valores no nulos dentro de rango.",
        "clientes.edad: existen valores fuera de rango.",
    )

    resultado.validar(
        set(clientes["genero"].dropna()).issubset(generos_validos),
        "clientes.genero: dominio valido.",
        "clientes.genero: contiene valores fuera del dominio.",
    )

    resultado.validar(
        set(clientes["ciudad"].dropna()).issubset(ciudades_validas),
        "clientes.ciudad: dominio valido.",
        "clientes.ciudad: contiene valores fuera del dominio.",
    )

    resultado.validar(
        set(clientes["canal_preferido"].dropna()).issubset(canales_validos),
        "clientes.canal_preferido: dominio valido en valores no nulos.",
        "clientes.canal_preferido: contiene valores fuera del dominio.",
    )

    resultado.validar(
        set(clientes["segmento"].dropna()).issubset(segmentos_validos),
        "clientes.segmento: dominio valido.",
        "clientes.segmento: contiene valores fuera del dominio.",
    )

    clientes_fecha = pd.to_datetime(clientes["fecha_registro"], errors="coerce")
    reg_min = pd.Timestamp(config["clientes"]["fecha_registro"]["minima"])
    reg_max = pd.Timestamp(config["clientes"]["fecha_registro"]["maxima"])

    resultado.validar(
        clientes_fecha.notna().all() and clientes_fecha.between(reg_min, reg_max).all(),
        "clientes.fecha_registro: fechas validas dentro del rango.",
        "clientes.fecha_registro: fechas invalidas o fuera del rango.",
    )

    ventas_fecha = pd.to_datetime(ventas["fecha"], errors="coerce")

    resultado.validar(
        ventas_fecha.notna().all() and ventas_fecha.between(inicio, fin).all(),
        "ventas.fecha: fechas validas dentro del periodo.",
        "ventas.fecha: fechas invalidas o fuera del periodo.",
    )

    resultado.validar(
        (pd.to_numeric(ventas["cantidad"], errors="coerce") >= 1).all(),
        "ventas.cantidad: mayor o igual que uno.",
        "ventas.cantidad: contiene valores menores que uno o no numericos.",
    )

    resultado.validar(
        (pd.to_numeric(ventas["precio_unitario"], errors="coerce") > 0).all(),
        "ventas.precio_unitario: positivo.",
        "ventas.precio_unitario: contiene valores no positivos o no numericos.",
    )

    descuento = pd.to_numeric(ventas["descuento_pct"], errors="coerce")
    max_descuento = float(config["descuentos"]["maximo_pct"])

    resultado.validar(
        descuento.between(0, max_descuento).all(),
        "ventas.descuento_pct: dentro del rango permitido.",
        "ventas.descuento_pct: contiene valores fuera del rango permitido.",
    )

    resultado.validar(
        (pd.to_numeric(ventas["monto_total"], errors="coerce") > 0).all(),
        "ventas.monto_total: positivo.",
        "ventas.monto_total: contiene valores no positivos o no numericos.",
    )

    resultado.validar(
        set(ventas["canal"].dropna()).issubset(canales_validos),
        "ventas.canal: dominio valido.",
        "ventas.canal: contiene valores fuera del dominio.",
    )

    resultado.validar(
        set(ventas["metodo_pago"].dropna()).issubset(metodos_validos),
        "ventas.metodo_pago: dominio valido.",
        "ventas.metodo_pago: contiene valores fuera del dominio.",
    )

    ventas_tienda = ventas.merge(
        tiendas[["id_tienda", "canal"]],
        on="id_tienda",
        how="left",
        suffixes=("", "_tienda"),
    )

    resultado.validar(
        ventas_tienda["canal"].eq(ventas_tienda["canal_tienda"]).all(),
        "ventas.canal: coincide con tiendas.canal.",
        "ventas.canal: existen filas que no coinciden con tiendas.canal.",
    )

    ticket_cols = ["fecha", "id_cliente", "id_tienda", "canal", "metodo_pago"]
    max_valores_ticket = ventas.groupby("id_venta")[ticket_cols].nunique(dropna=False).max().max()

    resultado.validar(
        int(max_valores_ticket) == 1,
        "ventas: campos de cabecera consistentes por ticket.",
        "ventas: existen tickets con campos de cabecera inconsistentes.",
    )

    clientes_fechas = clientes[["id_cliente", "fecha_registro"]].copy()
    clientes_fechas["fecha_registro_dt"] = pd.to_datetime(clientes_fechas["fecha_registro"], errors="coerce")
    ventas_clientes = ventas[["id_cliente", "fecha"]].merge(clientes_fechas, on="id_cliente", how="left")
    ventas_clientes["fecha_dt"] = pd.to_datetime(ventas_clientes["fecha"], errors="coerce")

    resultado.validar(
        (ventas_clientes["fecha_registro_dt"] <= ventas_clientes["fecha_dt"]).all(),
        "coherencia temporal: cliente registrado antes o en la venta.",
        "coherencia temporal: existen ventas antes del registro del cliente.",
    )

    productos_fechas = productos[["id_producto", "fecha_alta"]].copy()
    productos_fechas["fecha_alta_dt"] = pd.to_datetime(productos_fechas["fecha_alta"], errors="coerce")
    ventas_productos = ventas[["id_producto", "fecha"]].merge(productos_fechas, on="id_producto", how="left")
    ventas_productos["fecha_dt"] = pd.to_datetime(ventas_productos["fecha"], errors="coerce")

    resultado.validar(
        (ventas_productos["fecha_alta_dt"] <= ventas_productos["fecha_dt"]).all(),
        "coherencia temporal: producto disponible antes o en la venta.",
        "coherencia temporal: existen ventas antes del alta del producto.",
    )

    periodos_validos = set(
        pd.period_range(config["periodo"]["inicio"][:7], config["periodo"]["fin"][:7], freq="M").astype(str)
    )

    resultado.validar(
        set(inventario["periodo"].dropna().astype(str)).issubset(periodos_validos),
        "inventario.periodo: dentro del periodo esperado.",
        "inventario.periodo: contiene periodos fuera del rango esperado.",
    )

    for columna in ["stock_inicial", "unidades_vendidas", "reabastecimiento", "stock_final"]:
        valores = pd.to_numeric(inventario[columna], errors="coerce")

        resultado.validar(
            valores.notna().all() and (valores >= 0).all() and np.isclose(valores, valores.round()).all(),
            f"inventario.{columna}: entero no negativo.",
            f"inventario.{columna}: contiene nulos, negativos o no enteros.",
        )

    resultado.validar(
        (pd.to_numeric(inventario["costo_almacenamiento"], errors="coerce") >= 0).all(),
        "inventario.costo_almacenamiento: no negativo.",
        "inventario.costo_almacenamiento: contiene valores negativos o no numericos.",
    )


def validar_formulas_monetarias(
    config: Dict[str, Any],
    tablas: Dict[str, pd.DataFrame],
    resultado: ResultadoValidacion,
) -> None:
    ventas = tablas["ventas"].copy()

    tolerancia = float(
        config.get("aptitud_predictiva", {})
        .get("integridad", {})
        .get("formulas_con_tolerancia_pen", 0.01)
    )

    monto_recalculado = (
        pd.to_numeric(ventas["cantidad"], errors="coerce")
        * pd.to_numeric(ventas["precio_unitario"], errors="coerce")
        * (1 - pd.to_numeric(ventas["descuento_pct"], errors="coerce"))
    ).round(2)

    diferencia = (pd.to_numeric(ventas["monto_total"], errors="coerce") - monto_recalculado).abs()
    max_diferencia = float(diferencia.max())

    resultado.validar(
        max_diferencia <= tolerancia + 0.001,
        f"Formula monto_total: diferencia maxima S/ {max_diferencia:.4f}.",
        f"Formula monto_total: diferencia maxima S/ {max_diferencia:.4f}, mayor que tolerancia S/ {tolerancia:.2f}.",
    )


def validar_inventario(tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    ventas = tablas["ventas"].copy()
    inventario = tablas["inventario"].copy()

    inv_num = inventario.copy()

    for columna in ["stock_inicial", "unidades_vendidas", "reabastecimiento", "stock_final"]:
        inv_num[columna] = pd.to_numeric(inv_num[columna], errors="coerce")

    stock_final_recalculado = inv_num["stock_inicial"] + inv_num["reabastecimiento"] - inv_num["unidades_vendidas"]
    diferencia_stock = (inv_num["stock_final"] - stock_final_recalculado).abs().max()

    resultado.validar(
        diferencia_stock == 0,
        "inventario: stock_final cumple formula de balance.",
        f"inventario: stock_final no cumple formula de balance. Diferencia maxima: {diferencia_stock}",
    )

    inventario_ordenado = inv_num.sort_values(["id_producto", "id_tienda", "periodo"]).copy()
    stock_final_anterior = inventario_ordenado.groupby(["id_producto", "id_tienda"])["stock_final"].shift(1)
    mascara = stock_final_anterior.notna()

    continuidad_ok = (
        inventario_ordenado.loc[mascara, "stock_inicial"].to_numpy()
        == stock_final_anterior.loc[mascara].to_numpy()
    ).all()

    resultado.validar(
        continuidad_ok,
        "inventario: continuidad mensual stock_inicial = stock_final anterior.",
        "inventario: se rompe la continuidad mensual entre stock_final y stock_inicial.",
    )

    resultado.validar(
        (inv_num["stock_final"] >= 0).all(),
        "inventario: stock_final no negativo.",
        "inventario: existen stock_final negativos.",
    )

    ventas["periodo"] = pd.to_datetime(ventas["fecha"], errors="coerce").dt.to_period("M").astype(str)

    unidades_ventas = (
        ventas.groupby(["id_producto", "id_tienda", "periodo"], as_index=False)["cantidad"]
        .sum()
        .rename(columns={"cantidad": "unidades_ventas"})
    )
    unidades_ventas["unidades_ventas"] = pd.to_numeric(unidades_ventas["unidades_ventas"], errors="coerce").astype(int)

    unidades_inv = inventario[["id_producto", "id_tienda", "periodo", "unidades_vendidas"]].copy()
    unidades_inv["unidades_vendidas"] = pd.to_numeric(unidades_inv["unidades_vendidas"], errors="coerce").astype(int)

    conciliacion = unidades_ventas.merge(
        unidades_inv,
        on=["id_producto", "id_tienda", "periodo"],
        how="left",
    )

    faltantes_inv = int(conciliacion["unidades_vendidas"].isna().sum())
    diferencias = int(
        (
            conciliacion["unidades_ventas"]
            != conciliacion["unidades_vendidas"].fillna(-1).astype(int)
        ).sum()
    )

    resultado.validar(
        faltantes_inv == 0 and diferencias == 0,
        "inventario: unidades_vendidas concilia con ventas.",
        f"inventario: {faltantes_inv:,} combinaciones faltantes y {diferencias:,} diferencias contra ventas.",
    )


def validar_volumenes(config: Dict[str, Any], tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    validacion = config["validacion"]["volumenes"]

    checks = [
        ("tiendas", len(tablas["tiendas"]), int(validacion["tiendas_total"])),
        ("productos", len(tablas["productos"]), int(validacion["productos"])),
        ("clientes", len(tablas["clientes"]), int(validacion["clientes"])),
    ]

    for nombre, observado, esperado in checks:
        resultado.validar(
            observado == esperado,
            f"Volumen {nombre}: {observado:,} filas.",
            f"Volumen {nombre}: observado {observado:,}, esperado {esperado:,}.",
        )

    lineas = len(tablas["ventas"])
    minimo = int(validacion["lineas_ventas"]["minima"])
    maximo = int(validacion["lineas_ventas"]["maxima"])

    resultado.validar(
        minimo <= lineas <= maximo,
        f"Volumen ventas: {lineas:,} lineas dentro de rango.",
        f"Volumen ventas: {lineas:,} lineas fuera de rango [{minimo:,}, {maximo:,}].",
    )


def validar_picos_y_digital(config: Dict[str, Any], tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    ventas = tablas["ventas"].copy()
    ventas["fecha_dt"] = pd.to_datetime(ventas["fecha"], errors="coerce")
    ventas["anio"] = ventas["fecha_dt"].dt.year
    ventas["mes"] = ventas["fecha_dt"].dt.month

    tickets = ventas.drop_duplicates("id_venta").copy()

    tickets_dia = (
        tickets.groupby(["anio", "mes", tickets["fecha_dt"].dt.date])
        .size()
        .reset_index(name="tickets")
    )

    promedio_diario_mes = (
        tickets_dia.groupby("mes")["tickets"]
        .mean()
        .reindex(range(1, 13), fill_value=0)
    )

    multiplicadores = {
        int(mes): float(valor)
        for mes, valor in config["estacionalidad"]["multiplicadores_mensuales"].items()
    }

    meses_base = [
        mes
        for mes, multiplicador in multiplicadores.items()
        if mes not in (7, 12) and abs(multiplicador - 1.0) < 1e-9
    ]

    if not meses_base:
        candidatos = {
            mes: abs(multiplicador - 1.0)
            for mes, multiplicador in multiplicadores.items()
            if mes not in (7, 12)
        }
        distancia_minima = min(candidatos.values())
        meses_base = [
            mes
            for mes, distancia in candidatos.items()
            if abs(distancia - distancia_minima) < 1e-9
        ]

    promedio_base = float(promedio_diario_mes.loc[meses_base].mean())

    julio_pct = ((float(promedio_diario_mes.loc[7]) / promedio_base) - 1) * 100
    diciembre_pct = ((float(promedio_diario_mes.loc[12]) / promedio_base) - 1) * 100

    rango_julio = config["validacion"]["pico_julio"]["rango_pct"]
    rango_diciembre = config["validacion"]["pico_diciembre"]["rango_pct"]

    resultado.validar(
        porcentaje_en_rango(julio_pct, rango_julio),
        f"Pico julio: {format_pct(julio_pct)} sobre meses base.",
        f"Pico julio fuera de rango: {format_pct(julio_pct)}; esperado {rango_julio}.",
    )

    resultado.validar(
        porcentaje_en_rango(diciembre_pct, rango_diciembre),
        f"Pico diciembre: {format_pct(diciembre_pct)} sobre meses base.",
        f"Pico diciembre fuera de rango: {format_pct(diciembre_pct)}; esperado {rango_diciembre}.",
    )

    tickets["es_digital"] = tickets["canal"].isin(["Web", "App"])
    digital_por_anio = tickets.groupby("anio")["es_digital"].mean() * 100

    for anio, clave in [(2023, "participacion_digital_2023"), (2025, "participacion_digital_2025")]:
        rango = config["validacion"][clave]["rango_pct"]
        valor = float(digital_por_anio.loc[anio])

        resultado.validar(
            porcentaje_en_rango_con_tolerancia_pp(valor, rango),
            f"Participacion digital {anio}: {format_pct(valor)}.",
            f"Participacion digital {anio} fuera de rango: {format_pct(valor)}; esperado {rango}.",
        )

    resultado.validar(
        float(digital_por_anio.loc[2025]) > float(digital_por_anio.loc[2023]),
        "Crecimiento digital: 2025 mayor que 2023.",
        "Crecimiento digital: 2025 no supera 2023.",
    )


def normalizar_trimestre(valor: str) -> str:
    return str(valor).replace("-", "")


def validar_trujillo(config: Dict[str, Any], tablas: Dict[str, pd.DataFrame], resultado: ResultadoValidacion) -> None:
    ventas = tablas["ventas"].copy()
    productos = tablas["productos"][["id_producto", "costo_unitario"]].copy()
    tiendas = tablas["tiendas"][["id_tienda", "tipo", "ciudad"]].copy()
    inventario = tablas["inventario"].copy()

    ventas["fecha_dt"] = pd.to_datetime(ventas["fecha"], errors="coerce")
    ventas["trimestre"] = ventas["fecha_dt"].dt.to_period("Q").astype(str)

    ventas = ventas.merge(productos, on="id_producto", how="left")
    ventas = ventas.merge(tiendas, on="id_tienda", how="left")

    ventas_fisicas = ventas[ventas["tipo"].eq("Fisica")].copy()
    ventas_fisicas["cantidad"] = pd.to_numeric(ventas_fisicas["cantidad"], errors="coerce")
    ventas_fisicas["monto_total"] = pd.to_numeric(ventas_fisicas["monto_total"], errors="coerce")
    ventas_fisicas["costo_unitario"] = pd.to_numeric(ventas_fisicas["costo_unitario"], errors="coerce")
    ventas_fisicas["margen_bruto"] = (
        ventas_fisicas["monto_total"]
        - ventas_fisicas["cantidad"] * ventas_fisicas["costo_unitario"]
    )

    ventas_q = (
        ventas_fisicas.groupby(["ciudad", "trimestre"], as_index=False)
        .agg(ventas_netas=("monto_total", "sum"), margen_bruto=("margen_bruto", "sum"))
    )

    inventario["periodo_dt"] = pd.PeriodIndex(inventario["periodo"].astype(str), freq="M").to_timestamp()
    inventario["trimestre"] = inventario["periodo_dt"].dt.to_period("Q").astype(str)
    inventario = inventario.merge(tiendas, on="id_tienda", how="left")
    inventario_fisico = inventario[inventario["tipo"].eq("Fisica")].copy()
    inventario_fisico["costo_almacenamiento"] = pd.to_numeric(
        inventario_fisico["costo_almacenamiento"],
        errors="coerce",
    )

    costo_q = (
        inventario_fisico.groupby(["ciudad", "trimestre"], as_index=False)["costo_almacenamiento"]
        .sum()
    )

    margen = ventas_q.merge(costo_q, on=["ciudad", "trimestre"], how="left")
    margen["costo_almacenamiento"] = margen["costo_almacenamiento"].fillna(0)
    margen["margen_operativo_pct"] = (
        margen["margen_bruto"] - margen["costo_almacenamiento"]
    ) / margen["ventas_netas"]

    cfg = config["validacion"]["caida_margen_operativo_trujillo"]
    periodo_base = normalizar_trimestre(cfg["periodo_base"])
    periodo_afectado = normalizar_trimestre(cfg["periodo_afectado"])

    base = margen.loc[
        margen["ciudad"].eq("Trujillo") & margen["trimestre"].eq(periodo_base),
        "margen_operativo_pct",
    ]

    afectado = margen.loc[
        margen["ciudad"].eq("Trujillo") & margen["trimestre"].eq(periodo_afectado),
        "margen_operativo_pct",
    ]

    if base.empty or afectado.empty:
        resultado.error("Trujillo: no hay datos suficientes para comparar 2025-Q1 vs 2025-Q2.")
        return

    caida_pp = (float(base.iloc[0]) - float(afectado.iloc[0])) * 100
    rango = cfg["rango_pp"]

    resultado.validar(
        porcentaje_en_rango(caida_pp, rango),
        f"Trujillo: caida de margen operativo {caida_pp:.2f} pp.",
        f"Trujillo: caida de margen operativo {caida_pp:.2f} pp fuera de rango {rango}.",
    )


def calcular_tasa_churn_descriptivo(config: Dict[str, Any], tablas: Dict[str, pd.DataFrame]) -> float:
    clientes = tablas["clientes"].copy()
    ventas = tablas["ventas"].copy()

    fecha_eval = pd.Timestamp(config["churn"]["fecha_evaluacion_descriptiva"])
    ventana = int(config["churn"]["ventana_inactividad_dias"])
    inicio_ventana = fecha_eval - pd.Timedelta(days=ventana - 1)

    clientes["fecha_registro_dt"] = pd.to_datetime(clientes["fecha_registro"], errors="coerce")
    ventas["fecha_dt"] = pd.to_datetime(ventas["fecha"], errors="coerce")

    clientes_registrados = set(
        clientes.loc[clientes["fecha_registro_dt"] < inicio_ventana, "id_cliente"].astype(str)
    )

    compra_historica = set(
        ventas.loc[ventas["fecha_dt"] < inicio_ventana, "id_cliente"].astype(str)
    )

    compra_reciente = set(
        ventas.loc[
            (ventas["fecha_dt"] >= inicio_ventana) & (ventas["fecha_dt"] <= fecha_eval),
            "id_cliente",
        ].astype(str)
    )

    elegibles = clientes_registrados & compra_historica

    if not elegibles:
        return 0.0

    churn = elegibles - compra_reciente
    return len(churn) / len(elegibles)


def validar_churn_faltantes_outliers(
    config: Dict[str, Any],
    tablas: Dict[str, pd.DataFrame],
    resultado: ResultadoValidacion,
) -> None:
    tasa_churn_pct = calcular_tasa_churn_descriptivo(config, tablas) * 100
    rango_churn = config["validacion"]["tasa_churn"]["rango_pct"]

    resultado.validar(
        porcentaje_en_rango(tasa_churn_pct, rango_churn),
        f"Churn descriptivo: {format_pct(tasa_churn_pct)}.",
        f"Churn descriptivo fuera de rango: {format_pct(tasa_churn_pct)}; esperado {rango_churn}.",
    )

    campos = config["calidad_datos"]["faltantes"]["campos_permitidos"]
    total_celdas = 0
    total_faltantes = 0

    for tabla, columnas in campos.items():
        df = tablas[tabla]

        for columna in columnas:
            total_celdas += len(df)
            total_faltantes += int(df[columna].isna().sum())

    pct_faltantes = (total_faltantes / max(total_celdas, 1)) * 100
    rango_faltantes = config["validacion"]["faltantes"]["rango_pct"]

    resultado.validar(
        porcentaje_en_rango(pct_faltantes, rango_faltantes),
        f"Faltantes controlados: {format_pct(pct_faltantes)} sobre celdas elegibles.",
        f"Faltantes controlados fuera de rango: {format_pct(pct_faltantes)}; esperado {rango_faltantes}.",
    )

    cantidad_normal_max = int(config["calidad_datos"]["outliers"]["cantidad_normal_maxima"])
    pct_outliers = (
        pd.to_numeric(tablas["ventas"]["cantidad"], errors="coerce") > cantidad_normal_max
    ).mean() * 100

    rango_outliers = config["validacion"]["outliers"]["rango_pct"]

    resultado.validar(
        porcentaje_en_rango(pct_outliers, rango_outliers),
        f"Outliers de cantidad: {format_pct(pct_outliers)}.",
        f"Outliers de cantidad fuera de rango: {format_pct(pct_outliers)}; esperado {rango_outliers}.",
    )


def validar_aptitud_predictiva(
    config: Dict[str, Any],
    tablas: Dict[str, pd.DataFrame],
    resultado: ResultadoValidacion,
) -> None:
    ventas = tablas["ventas"].copy()
    productos = tablas["productos"][["id_producto", "categoria"]].copy()
    tiendas = tablas["tiendas"].copy()
    clientes = tablas["clientes"].copy()

    ventas["fecha_dt"] = pd.to_datetime(ventas["fecha"], errors="coerce")
    ventas["periodo"] = ventas["fecha_dt"].dt.to_period("M").astype(str)
    ventas_prod = ventas.merge(productos, on="id_producto", how="left")

    periodos = pd.period_range(config["periodo"]["inicio"][:7], config["periodo"]["fin"][:7], freq="M").astype(str)
    nodos = tiendas["id_tienda"].astype(str).tolist()
    categorias = config["dominios"]["categorias"]

    demanda = (
        ventas_prod.groupby(["periodo", "id_tienda", "categoria"], as_index=False)["cantidad"]
        .sum()
        .rename(columns={"cantidad": "demanda_unidades"})
    )

    indice_completo = pd.MultiIndex.from_product(
        [periodos, nodos, categorias],
        names=["periodo", "id_tienda", "categoria"],
    )

    panel = (
        demanda.set_index(["periodo", "id_tienda", "categoria"])
        .reindex(indice_completo, fill_value=0)
        .reset_index()
    )

    esperado = len(periodos) * len(nodos) * len(categorias)

    resultado.validar(
        len(panel) == esperado,
        f"Aptitud demanda: panel mensual completo ({len(panel):,} filas).",
        f"Aptitud demanda: panel incompleto ({len(panel):,} filas, esperado {esperado:,}).",
    )

    primer_objetivo = pd.Period(config["modelado_predictivo"]["demanda"]["primer_periodo_objetivo"], freq="M")
    fin_periodo = pd.Period(config["periodo"]["fin"][:7], freq="M")
    meses_objetivo = len(pd.period_range(primer_objetivo, fin_periodo, freq="M"))
    min_meses = int(config["aptitud_predictiva"]["demanda"]["minimo_meses_objetivo"])

    resultado.validar(
        meses_objetivo >= min_meses,
        f"Aptitud demanda: {meses_objetivo} meses objetivo evaluables.",
        f"Aptitud demanda: solo {meses_objetivo} meses objetivo; minimo {min_meses}.",
    )

    resultado.validar(
        panel["demanda_unidades"].astype(float).std() > 0,
        "Aptitud demanda: variacion temporal distinta de cero.",
        "Aptitud demanda: no existe variacion en demanda_unidades.",
    )

    nodos_con_ventas = set(demanda.loc[demanda["demanda_unidades"] > 0, "id_tienda"].astype(str))
    categorias_con_ventas = set(demanda.loc[demanda["demanda_unidades"] > 0, "categoria"].astype(str))

    resultado.validar(
        set(nodos).issubset(nodos_con_ventas),
        "Aptitud demanda: todos los nodos tienen ventas representadas.",
        f"Aptitud demanda: nodos sin ventas representadas: {sorted(set(nodos) - nodos_con_ventas)}.",
    )

    resultado.validar(
        set(categorias).issubset(categorias_con_ventas),
        "Aptitud demanda: todas las categorias tienen ventas representadas.",
        f"Aptitud demanda: categorias sin ventas representadas: {sorted(set(categorias) - categorias_con_ventas)}.",
    )

    clientes["fecha_registro_dt"] = pd.to_datetime(clientes["fecha_registro"], errors="coerce")
    fechas_observacion = config["modelado_predictivo"]["churn"]["fechas_observacion"]
    ventana_objetivo = int(config["modelado_predictivo"]["churn"]["ventana_objetivo_dias"])
    min_clase = int(config["aptitud_predictiva"]["churn"]["minimo_observaciones_por_clase_y_corte"])
    rango_tasa = config["aptitud_predictiva"]["churn"]["rango_tasa_positiva_por_corte_pct"]
    fin_dataset = pd.Timestamp(config["periodo"]["fin"])

    for fecha_corte in fechas_observacion:
        corte = pd.Timestamp(fecha_corte)
        fin_objetivo = corte + pd.Timedelta(days=ventana_objetivo)

        if fin_objetivo > fin_dataset:
            resultado.error(f"Aptitud churn {fecha_corte}: ventana futura excede el periodo del dataset.")
            continue

        registrados = set(clientes.loc[clientes["fecha_registro_dt"] <= corte, "id_cliente"].astype(str))
        compra_previa = set(ventas.loc[ventas["fecha_dt"] <= corte, "id_cliente"].astype(str))
        elegibles = registrados & compra_previa

        compra_futura = set(
            ventas.loc[
                (ventas["fecha_dt"] > corte) & (ventas["fecha_dt"] <= fin_objetivo),
                "id_cliente",
            ].astype(str)
        )

        no_churn = len(elegibles & compra_futura)
        churn = len(elegibles - compra_futura)
        total = churn + no_churn
        tasa_positiva = (churn / total * 100) if total else 0.0

        resultado.validar(
            churn >= min_clase and no_churn >= min_clase,
            f"Aptitud churn {fecha_corte}: ambas clases presentes (churn={churn:,}, no_churn={no_churn:,}).",
            f"Aptitud churn {fecha_corte}: clases insuficientes (churn={churn:,}, no_churn={no_churn:,}, minimo={min_clase:,}).",
        )

        resultado.validar(
            porcentaje_en_rango(tasa_positiva, rango_tasa),
            f"Aptitud churn {fecha_corte}: tasa positiva {format_pct(tasa_positiva)}.",
            f"Aptitud churn {fecha_corte}: tasa positiva {format_pct(tasa_positiva)} fuera de rango {rango_tasa}.",
        )


def validar_aptitud_prescriptiva(
    config: Dict[str, Any],
    tablas: Dict[str, pd.DataFrame],
    resultado: ResultadoValidacion,
) -> None:
    inventario = tablas["inventario"].copy()
    productos = tablas["productos"][["id_producto", "categoria", "costo_unitario"]].copy()
    tiendas = tablas["tiendas"].copy()

    cfg = config["modelado_prescriptivo"]
    periodo_fuente = cfg["inventario_inicial"]["periodo_fuente"]
    categorias = set(config["dominios"]["categorias"])
    nodos = set(tiendas["id_tienda"].astype(str))

    inv_dic = inventario[inventario["periodo"].astype(str).eq(periodo_fuente)].merge(
        productos[["id_producto", "categoria"]],
        on="id_producto",
        how="left",
    )

    stock_categoria = (
        inv_dic.groupby(["id_tienda", "categoria"], as_index=False)["stock_final"]
        .sum()
    )

    combinaciones = set(zip(stock_categoria["id_tienda"].astype(str), stock_categoria["categoria"].astype(str)))
    esperadas = {(nodo, categoria) for nodo in nodos for categoria in categorias}

    resultado.validar(
        esperadas.issubset(combinaciones),
        "Aptitud prescriptiva: stock inicial derivable por nodo-categoria para diciembre 2025.",
        f"Aptitud prescriptiva: faltan combinaciones nodo-categoria: {sorted(esperadas - combinaciones)[:10]}.",
    )

    resultado.validar(
        (pd.to_numeric(productos["costo_unitario"], errors="coerce") > 0).all(),
        "Aptitud prescriptiva: costos unitarios positivos.",
        "Aptitud prescriptiva: existen costos unitarios no positivos.",
    )

    factores = cfg["capacidad"]["factores_espacio"]
    factores_ok = set(factores.keys()) == categorias and all(float(valor) > 0 for valor in factores.values())

    resultado.validar(
        factores_ok,
        "Aptitud prescriptiva: factores de espacio positivos para todas las categorias.",
        "Aptitud prescriptiva: factores de espacio incompletos o no positivos.",
    )

    escenarios = cfg["escenarios"]
    ids_escenarios = [esc["id"] for esc in escenarios]

    escenarios_ok = (
        len(escenarios) == 9
        and len(ids_escenarios) == len(set(ids_escenarios))
        and all(float(esc["factor_presupuesto"]) > 0 for esc in escenarios)
        and all(float(esc["factor_capacidad"]) > 0 for esc in escenarios)
        and all(0 < float(esc["nivel_servicio"]) <= 1 for esc in escenarios)
    )

    resultado.validar(
        escenarios_ok,
        "Aptitud prescriptiva: escenarios configurados completos y validos.",
        "Aptitud prescriptiva: escenarios incompletos, duplicados o con parametros invalidos.",
    )

    pred_dir = ROOT / config["salidas_predictivas"]["directorio"]
    pred_file = pred_dir / cfg["demanda"]["archivo"]

    if pred_file.exists():
        pred = pd.read_csv(pred_file)
        campos = [
            cfg["demanda"]["campo_bajo"],
            cfg["demanda"]["campo_central"],
            cfg["demanda"]["campo_alto"],
        ]

        faltantes = [col for col in campos + ["id_tienda", "categoria"] if col not in pred.columns]

        if faltantes:
            resultado.error(f"Aptitud prescriptiva: {pred_file.relative_to(ROOT)} no contiene columnas {faltantes}.")
        else:
            bajo = pd.to_numeric(pred[campos[0]], errors="coerce")
            central = pd.to_numeric(pred[campos[1]], errors="coerce")
            alto = pd.to_numeric(pred[campos[2]], errors="coerce")

            orden_ok = ((bajo <= central) & (central <= alto)).all()
            no_negativos = (pred[campos].apply(pd.to_numeric, errors="coerce") >= 0).all().all()
            duplicados = int(pred.duplicated(["id_tienda", "categoria"]).sum())

            resultado.validar(
                bool(orden_ok) and bool(no_negativos) and duplicados == 0,
                "Aptitud prescriptiva: archivo predictivo existente compatible.",
                "Aptitud prescriptiva: predicciones con intervalos invalidos, negativos o duplicados.",
            )
    else:
        resultado.warn(
            "Aptitud prescriptiva: predicciones_demanda.csv aun no existe; se valido la aptitud de las tablas fuente."
        )


def escribir_reporte(config: Dict[str, Any], resultado: ResultadoValidacion) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    estado = "APROBADO" if resultado.aprobado else "NO APROBADO"

    lineas = [
        "Reporte de validacion de datos — AndinaRetail S.A.C.",
        "=" * 60,
        f"Estado general: {estado}",
        f"Version config: {config.get('metadata', {}).get('version', 'N/D')}",
        f"Semilla: {config.get('reproducibilidad', {}).get('semilla', 'N/D')}",
        "",
        f"Validaciones correctas: {len(resultado.oks)}",
        f"Advertencias: {len(resultado.advertencias)}",
        f"Errores criticos: {len(resultado.errores)}",
        "",
        "OK",
        "--",
    ]

    lineas.extend([f"[OK] {mensaje}" for mensaje in resultado.oks])

    lineas.extend(["", "ADVERTENCIAS", "------------"])

    if resultado.advertencias:
        lineas.extend([f"[WARN] {mensaje}" for mensaje in resultado.advertencias])
    else:
        lineas.append("Sin advertencias.")

    lineas.extend(["", "ERRORES CRITICOS", "----------------"])

    if resultado.errores:
        lineas.extend([f"[ERROR] {mensaje}" for mensaje in resultado.errores])
    else:
        lineas.append("Sin errores criticos.")

    REPORT_PATH.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def main() -> int:
    resultado = ResultadoValidacion()

    try:
        config = cargar_config()
    except Exception as exc:
        print(f"ERROR al cargar configuracion: {exc}")
        return 1

    tablas = cargar_csv(config, resultado)
    requeridas = set(config["salidas"]["archivos"].keys())

    if set(tablas.keys()) != requeridas:
        escribir_reporte(config, resultado)
        print(f"Validacion NO APROBADA. Reporte: {REPORT_PATH.relative_to(ROOT)}")
        return 1

    validar_columnas(tablas, resultado)
    validar_claves_primarias(tablas, resultado)
    validar_claves_foraneas(tablas, resultado)
    validar_nulos_permitidos(config, tablas, resultado)
    validar_dominios_y_rangos(config, tablas, resultado)
    validar_formulas_monetarias(config, tablas, resultado)
    validar_inventario(tablas, resultado)
    validar_volumenes(config, tablas, resultado)
    validar_picos_y_digital(config, tablas, resultado)
    validar_trujillo(config, tablas, resultado)
    validar_churn_faltantes_outliers(config, tablas, resultado)
    validar_aptitud_predictiva(config, tablas, resultado)
    validar_aptitud_prescriptiva(config, tablas, resultado)

    escribir_reporte(config, resultado)

    print(f"Reporte generado: {REPORT_PATH.relative_to(ROOT)}")
    print(f"Validaciones correctas: {len(resultado.oks)}")
    print(f"Advertencias: {len(resultado.advertencias)}")
    print(f"Errores criticos: {len(resultado.errores)}")

    if resultado.aprobado:
        print("Validacion APROBADA.")
        return 0

    print("Validacion NO APROBADA. Revise el reporte.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
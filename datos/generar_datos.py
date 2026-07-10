"""
Generador reproducible de datos sinteticos para AndinaRetail S.A.C.
Tarea: [Datos] Incorporar patrones analiticos, faltantes y outliers.

Entradas:
- config/escenarios.yaml

Salidas:
- datos/tiendas.csv
- datos/productos.csv
- datos/clientes.csv
- datos/ventas.csv
- datos/inventario.csv

Notas de alcance:
- Genera las cinco tablas oficiales del proyecto de forma reproducible.
- Incorpora estacionalidad, crecimiento digital, deterioro de margen en Trujillo,
  relacion descuento-demanda, churn descriptivo inducido, faltantes controlados
  y outliers controlados de cantidad.
- No agrega columnas auxiliares al esquema fisico de los CSV.
- Incluye validaciones basicas y de humo; la validacion integral corresponde a una tarea posterior.
"""
 
from __future__ import annotations
 
import random
from pathlib import Path
from typing import Any, Dict, List, Tuple
 
import numpy as np
import pandas as pd
import yaml
from faker import Faker
 
 
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "escenarios.yaml"
DATA_DIR = ROOT / "datos"
 
 
class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader que falla si encuentra claves duplicadas en el mismo nivel."""
 
 
def construct_mapping_no_duplicates(loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(
                f"Clave duplicada en config/escenarios.yaml: {key!r}. "
                "Revise el YAML antes de ejecutar el generador."
            )
        value = loader.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping
 
 
UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping_no_duplicates,
)
 
 
def cargar_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    """Carga config/escenarios.yaml usando un loader que detecta claves duplicadas."""
    if not path.exists():
        raise FileNotFoundError(f"No se encontro el archivo de configuracion: {path}")
 
    with path.open("r", encoding="utf-8") as file:
        config = yaml.load(file, Loader=UniqueKeyLoader)
 
    if not isinstance(config, dict):
        raise ValueError("El archivo YAML no se cargo como diccionario.")
 
    return config
 
 
def configurar_semillas(config: Dict[str, Any]) -> Tuple[int, np.random.Generator, Faker]:
    """Configura random, numpy y Faker con la semilla global documentada."""
    seed = int(config["reproducibilidad"]["semilla"])
    locale = config.get("metadata", {}).get("locale_faker", "es_PE")
 
    random.seed(seed)
    np.random.seed(seed)
    rng = np.random.default_rng(seed)
 
    Faker.seed(seed)
    try:
        fake = Faker(locale)
    except AttributeError:
        # Algunas instalaciones de Faker no incluyen es_PE.
        # El YAML sigue siendo la fuente canónica; este fallback evita bloquear la ejecución local.
        print(f"Advertencia: Faker no reconoce el locale {locale!r}. Se usará es_ES como respaldo.")
        fake = Faker("es_ES")
    fake.seed_instance(seed)
 
    return seed, rng, fake
 
 
def normalizar_pesos(pesos: Dict[Any, float]) -> Tuple[List[Any], np.ndarray]:
    """Devuelve claves y probabilidades normalizadas para muestreo."""
    claves = list(pesos.keys())
    valores = np.array([float(pesos[k]) for k in claves], dtype=float)
    total = valores.sum()
    if total <= 0:
        raise ValueError(f"Los pesos no son validos: {pesos}")
    return claves, valores / total
 
 
def elegir_ponderado(rng: np.random.Generator, pesos: Dict[Any, float]) -> Any:
    """Elige una clave de un diccionario de pesos."""
    claves, probs = normalizar_pesos(pesos)
    return claves[int(rng.choice(len(claves), p=probs))]
 
 
def fecha_aleatoria(rng: np.random.Generator, inicio: str, fin: str) -> pd.Timestamp:
    """Genera una fecha aleatoria uniforme entre inicio y fin sin crear rangos grandes repetidos."""
    inicio_ts = pd.Timestamp(inicio)
    fin_ts = pd.Timestamp(fin)
    dias = (fin_ts - inicio_ts).days
    return inicio_ts + pd.Timedelta(days=int(rng.integers(0, dias + 1)))


def recalcular_monto_total(ventas: pd.DataFrame) -> pd.DataFrame:
    """Recalcula monto_total despues de cualquier cambio en cantidad, precio o descuento."""
    ventas = ventas.copy()
    ventas["monto_total"] = (
        ventas["cantidad"].astype(float)
        * ventas["precio_unitario"].astype(float)
        * (1 - ventas["descuento_pct"].astype(float))
    ).round(2)
    ventas["monto_total"] = ventas["monto_total"].apply(redondear_monto)
    return ventas


def obtener_inicio_ventana_churn(config: Dict[str, Any]) -> pd.Timestamp:
    """Devuelve el inicio de la ventana final usada para medir churn descriptivo."""
    cfg = config["churn"]
    fecha_eval = pd.Timestamp(cfg["fecha_evaluacion_descriptiva"])
    ventana = int(cfg["ventana_inactividad_dias"])
    return fecha_eval - pd.Timedelta(days=ventana - 1)


def preparar_clientes_activos_recientes(
    config: Dict[str, Any],
    clientes: pd.DataFrame,
    fechas_tickets: pd.DatetimeIndex,
    rng: np.random.Generator,
) -> Tuple[pd.Timestamp, np.ndarray]:
    """Selecciona clientes que deben aparecer en la ventana final para calibrar churn descriptivo."""
    inicio_ventana = obtener_inicio_ventana_churn(config)
    cfg_churn = config["churn"]
    min_churn = float(cfg_churn["proporcion_objetivo"]["minima"])
    max_churn = float(cfg_churn["proporcion_objetivo"]["maxima"])

    clientes_tmp = clientes.copy()
    clientes_tmp["fecha_registro_dt"] = pd.to_datetime(clientes_tmp["fecha_registro"])
    elegibles = clientes_tmp.loc[
        clientes_tmp["fecha_registro_dt"] < inicio_ventana,
        "id_cliente",
    ].to_numpy()

    tickets_ventana = int((fechas_tickets >= inicio_ventana).sum())
    if len(elegibles) == 0 or tickets_ventana == 0:
        return inicio_ventana, np.array([], dtype=object)

    # Se usa un objetivo dentro del rango documentado, con margen para que los tickets
    # disponibles en los ultimos 90 dias puedan cubrir clientes activos distintos.
    activos_max_por_churn_min = int(np.floor(len(elegibles) * (1 - min_churn - 0.01)))
    activos_min_por_churn_max = int(np.ceil(len(elegibles) * (1 - max_churn + 0.01)))
    activos_por_tickets = int(np.floor(tickets_ventana * 0.98))

    n_activos = min(activos_max_por_churn_min, activos_por_tickets, len(elegibles))
    n_activos = max(n_activos, min(activos_min_por_churn_max, len(elegibles), tickets_ventana))

    activos = rng.choice(elegibles, size=n_activos, replace=False)
    rng.shuffle(activos)
    return inicio_ventana, activos


def ajustar_probabilidades_mix_trujillo(
    config: Dict[str, Any],
    categorias: List[Any],
    probabilidades: np.ndarray,
) -> np.ndarray:
    """Desplaza parte del mix hacia categorias de menor margen para Trujillo afectado."""
    destino = set(config["trujillo"]["categorias_destino_mix"])
    desplazamiento = float(config["trujillo"]["desplazamiento_mix_menor_margen_pct"]) / 100.0

    probs = probabilidades.astype(float).copy()
    mascara_destino = np.array([cat in destino for cat in categorias], dtype=bool)
    if not mascara_destino.any() or mascara_destino.all():
        return probs / probs.sum()

    transferencia = probs[~mascara_destino].sum() * desplazamiento
    probs[~mascara_destino] *= (1 - desplazamiento)
    probs[mascara_destino] += transferencia * (probs[mascara_destino] / probs[mascara_destino].sum())
    return probs / probs.sum()


def ajustar_cantidad_por_descuento(
    cantidad_base: int,
    descuento_pct: float,
    config: Dict[str, Any],
    rng: np.random.Generator,
) -> int:
    """Aplica una relacion positiva, imperfecta y con ruido entre descuento y demanda."""
    cfg = config["relacion_descuento_demanda"]
    ref_descuento = float(cfg["aumento_descuento_pp_referencia"]) / 100.0
    min_efecto = float(cfg["aumento_demanda_pct_esperado"]["minimo"]) / 100.0
    max_efecto = float(cfg["aumento_demanda_pct_esperado"]["maximo"]) / 100.0
    ruido_sd = float(cfg["ruido_relativo_desviacion_estandar"])
    cantidad_max_normal = int(config["calidad_datos"]["outliers"]["cantidad_normal_maxima"])

    efecto_ref = float(rng.uniform(min_efecto, max_efecto))
    ruido = float(rng.normal(0, ruido_sd))
    factor = 1 + (descuento_pct / max(ref_descuento, 0.0001)) * efecto_ref + ruido
    cantidad = int(round(cantidad_base * max(0.2, factor)))
    return int(np.clip(cantidad, 1, cantidad_max_normal))


def redondear_monto(valor: float) -> float:
    """Redondea montos a dos decimales y evita -0.00 por efectos numericos."""
    valor = round(float(valor), 2)
    return 0.0 if abs(valor) < 0.005 else valor

def recalcular_monto_total(ventas: pd.DataFrame) -> pd.DataFrame:
    """Recalcula monto_total despues de cualquier cambio en cantidad, precio o descuento."""
    ventas = ventas.copy()
    ventas["monto_total"] = (
        ventas["cantidad"].astype(float)
        * ventas["precio_unitario"].astype(float)
        * (1 - ventas["descuento_pct"].astype(float))
    ).round(2)
    ventas["monto_total"] = ventas["monto_total"].apply(redondear_monto)
    return ventas


def obtener_inicio_ventana_churn(config: Dict[str, Any]) -> pd.Timestamp:
    """Devuelve el inicio de la ventana final usada para medir churn descriptivo."""
    cfg = config["churn"]
    fecha_eval = pd.Timestamp(cfg["fecha_evaluacion_descriptiva"])
    ventana = int(cfg["ventana_inactividad_dias"])
    return fecha_eval - pd.Timedelta(days=ventana - 1)


def ajustar_probabilidades_mix_trujillo(
    config: Dict[str, Any],
    categorias: List[Any],
    probabilidades: np.ndarray,
) -> np.ndarray:
    """Desplaza parte del mix hacia categorias de menor margen para Trujillo afectado."""
    destino = set(config["trujillo"]["categorias_destino_mix"])
    desplazamiento = float(config["trujillo"]["desplazamiento_mix_menor_margen_pct"]) / 100.0

    probs = probabilidades.astype(float).copy()
    mascara_destino = np.array([cat in destino for cat in categorias], dtype=bool)

    if not mascara_destino.any() or mascara_destino.all():
        return probs / probs.sum()

    transferencia = probs[~mascara_destino].sum() * desplazamiento
    probs[~mascara_destino] *= 1 - desplazamiento
    probs[mascara_destino] += transferencia * (
        probs[mascara_destino] / probs[mascara_destino].sum()
    )

    return probs / probs.sum()


def ajustar_cantidad_por_descuento(
    cantidad_base: int,
    descuento_pct: float,
    config: Dict[str, Any],
    rng: np.random.Generator,
) -> int:
    """Aplica una relacion positiva, imperfecta y con ruido entre descuento y demanda."""
    cfg = config["relacion_descuento_demanda"]

    ref_descuento = float(cfg["aumento_descuento_pp_referencia"]) / 100.0
    min_efecto = float(cfg["aumento_demanda_pct_esperado"]["minimo"]) / 100.0
    max_efecto = float(cfg["aumento_demanda_pct_esperado"]["maximo"]) / 100.0
    ruido_sd = float(cfg["ruido_relativo_desviacion_estandar"])
    cantidad_max_normal = int(config["calidad_datos"]["outliers"]["cantidad_normal_maxima"])

    efecto_ref = float(rng.uniform(min_efecto, max_efecto))
    ruido = float(rng.normal(0, ruido_sd))

    factor = 1 + (descuento_pct / max(ref_descuento, 0.0001)) * efecto_ref + ruido
    cantidad = int(round(cantidad_base * max(0.2, factor)))

    return int(np.clip(cantidad, 1, cantidad_max_normal))
 
 
def generar_tiendas(config: Dict[str, Any], fake: Faker, rng: np.random.Generator) -> pd.DataFrame:
    """Genera las 13 tiendas fisicas y los dos nodos virtuales WEB y APP."""
    dominios = config["dominios"]
    volumenes = config["volumenes"]
    region_por_ciudad = dominios["region_por_ciudad"]
 
    filas = []
    contador = 1
 
    for ciudad, cantidad in volumenes["tiendas_por_ciudad"].items():
        for _ in range(int(cantidad)):
            filas.append(
                {
                    "id_tienda": f"T{contador:03d}",
                    "nombre": f"Tienda {ciudad} {contador:03d}",
                    "tipo": "Fisica",
                    "canal": "Tienda",
                    "ciudad": ciudad,
                    "region": region_por_ciudad[ciudad],
                    "area_m2": int(rng.integers(180, 1201)),
                    "fecha_apertura": fecha_aleatoria(rng, "2018-01-01", "2022-12-31").date().isoformat(),
                }
            )
            contador += 1
 
    for nodo in volumenes["nodos_virtuales"]:
        filas.append(
            {
                "id_tienda": nodo["id_tienda"],
                "nombre": nodo["nombre"],
                "tipo": nodo["tipo"],
                "canal": nodo["canal"],
                "ciudad": nodo.get("ciudad"),
                "region": nodo.get("region"),
                "area_m2": nodo.get("area_m2"),
                "fecha_apertura": fecha_aleatoria(rng, "2020-01-01", "2022-12-31").date().isoformat(),
            }
        )
 
    columnas = ["id_tienda", "nombre", "tipo", "canal", "ciudad", "region", "area_m2", "fecha_apertura"]
    tiendas = pd.DataFrame(filas, columns=columnas)
    return tiendas
 
 
def distribuir_cantidades(total: int, proporciones: Dict[str, float]) -> Dict[str, int]:
    """Convierte proporciones en cantidades enteras que suman exactamente el total."""
    claves, probs = normalizar_pesos(proporciones)
    valores = probs * total
    cantidades = {clave: int(np.floor(valor)) for clave, valor in zip(claves, valores)}
    faltante = total - sum(cantidades.values())
 
    fracciones = sorted(
        zip(claves, valores - np.floor(valores)),
        key=lambda x: x[1],
        reverse=True,
    )
    for clave, _ in fracciones[:faltante]:
        cantidades[clave] += 1
 
    return cantidades
 
 
def generar_productos(config: Dict[str, Any], fake: Faker, rng: np.random.Generator) -> pd.DataFrame:
    """Genera el catalogo de productos con categorias, marcas, precios y costos."""
    dominios = config["dominios"]
    volumenes = config["volumenes"]
    precios = config["precios"]
 
    cantidades_por_categoria = distribuir_cantidades(
        int(volumenes["productos"]),
        volumenes["productos_por_categoria"],
    )
 
    filas = []
    contador = 1
 
    for categoria, cantidad in cantidades_por_categoria.items():
        subcategorias = dominios["subcategorias_por_categoria"][categoria]
        marcas = dominios["marcas_ficticias_por_categoria"][categoria]
        rango_precio = precios["precio_lista_por_categoria"][categoria]
        margen_base = float(precios["margen_bruto_base_por_categoria"][categoria])
 
        for _ in range(cantidad):
            subcategoria = str(rng.choice(subcategorias))
            marca = str(rng.choice(marcas))
            precio_lista = redondear_monto(rng.uniform(float(rango_precio["min"]), float(rango_precio["max"])))
            costo_unitario = redondear_monto(precio_lista * (1 - margen_base))
 
            filas.append(
                {
                    "id_producto": f"P{contador:04d}",
                    "nombre": f"{categoria} {subcategoria} {marca} {fake.bothify(text='??-###').upper()}",
                    "categoria": categoria,
                    "subcategoria": subcategoria,
                    "marca": marca,
                    "precio_lista": precio_lista,
                    "costo_unitario": costo_unitario,
                    "fecha_alta": fecha_aleatoria(rng, "2020-01-01", "2022-12-31").date().isoformat(),
                }
            )
            contador += 1
 
    columnas = [
        "id_producto",
        "nombre",
        "categoria",
        "subcategoria",
        "marca",
        "precio_lista",
        "costo_unitario",
        "fecha_alta",
    ]
    productos = pd.DataFrame(filas, columns=columnas)
    return productos
 
 
def generar_clientes(config: Dict[str, Any], fake: Faker, rng: np.random.Generator) -> pd.DataFrame:
    """Genera clientes sinteticos con datos demograficos y comerciales basicos."""
    cfg = config["clientes"]
    total_clientes = int(config["volumenes"]["clientes"])
 
    ciudades, p_ciudades = normalizar_pesos(cfg["distribucion_ciudad"])
    generos, p_generos = normalizar_pesos(cfg["distribucion_genero"])
    segmentos, p_segmentos = normalizar_pesos(cfg["distribucion_segmento_comercial"])
    canales, p_canales = normalizar_pesos(cfg["distribucion_canal_preferido"])
 
    distritos_por_ciudad = {
        "Lima": ["Los Olivos", "Miraflores", "San Isidro", "Ate", "Surco", "Comas"],
        "Arequipa": ["Cercado", "Yanahuara", "Cayma", "Socabaya"],
        "Trujillo": ["Trujillo", "Victor Larco", "La Esperanza", "El Porvenir"],
        "Cusco": ["Cusco", "Wanchaq", "San Sebastian", "San Jeronimo"],
        "Piura": ["Piura", "Castilla", "Veintiseis de Octubre", "Catacaos"],
    }
 
    filas = []
    for i in range(1, total_clientes + 1):
        ciudad = str(rng.choice(ciudades, p=p_ciudades))
        edad = int(round(rng.normal(cfg["edad"]["media"], cfg["edad"]["desviacion_estandar"])))
        edad = int(np.clip(edad, cfg["edad"]["minima"], cfg["edad"]["maxima"]))
 
        filas.append(
            {
                "id_cliente": f"C{i:05d}",
                "nombre": fake.name(),
                "edad": edad,
                "genero": str(rng.choice(generos, p=p_generos)),
                "ciudad": ciudad,
                "distrito": str(rng.choice(distritos_por_ciudad[ciudad])),
                "fecha_registro": fecha_aleatoria(
                    rng,
                    cfg["fecha_registro"]["minima"],
                    cfg["fecha_registro"]["maxima"],
                ).date().isoformat(),
                "canal_preferido": str(rng.choice(canales, p=p_canales)),
                "segmento": str(rng.choice(segmentos, p=p_segmentos)),
            }
        )
 
    columnas = [
        "id_cliente",
        "nombre",
        "edad",
        "genero",
        "ciudad",
        "distrito",
        "fecha_registro",
        "canal_preferido",
        "segmento",
    ]
    clientes = pd.DataFrame(filas, columns=columnas)
    clientes["fecha_registro"] = pd.to_datetime(clientes["fecha_registro"])
    clientes = clientes.sort_values("fecha_registro").reset_index(drop=True)
    clientes["fecha_registro"] = clientes["fecha_registro"].dt.date.astype(str)
    return clientes
 
 
def generar_lineas_por_ticket(config: Dict[str, Any], rng: np.random.Generator) -> np.ndarray:
    """Genera el numero de lineas por ticket y ajusta al objetivo exacto de lineas."""
    volumenes = config["volumenes"]
    n_tickets = int(volumenes["tickets_objetivo"])
    objetivo_lineas = int(volumenes["lineas_ventas_objetivo"])
    cfg_lineas = volumenes["lineas_por_ticket"]
 
    valores = np.rint(
        rng.normal(
            float(cfg_lineas["media"]),
            float(cfg_lineas["desviacion_estandar"]),
            size=n_tickets,
        )
    ).astype(int)
 
    minimo = int(cfg_lineas["minimo"])
    maximo = int(cfg_lineas["maximo"])
    valores = np.clip(valores, minimo, maximo)
 
    diferencia = objetivo_lineas - int(valores.sum())
    while diferencia != 0:
        if diferencia > 0:
            candidatos = np.where(valores < maximo)[0]
            if len(candidatos) == 0:
                break
            idx = int(rng.choice(candidatos))
            valores[idx] += 1
            diferencia -= 1
        else:
            candidatos = np.where(valores > minimo)[0]
            if len(candidatos) == 0:
                break
            idx = int(rng.choice(candidatos))
            valores[idx] -= 1
            diferencia += 1
 
    return valores
 
 
def generar_fechas_tickets(config: Dict[str, Any], rng: np.random.Generator, n_tickets: int) -> pd.DatetimeIndex:
    """Genera fechas de tickets usando periodo, estacionalidad mensual y crecimiento anual."""
    inicio = config["periodo"]["inicio"]
    fin = config["periodo"]["fin"]
    fechas = pd.date_range(inicio, fin, freq="D")
 
    multiplicadores = config["estacionalidad"]["multiplicadores_mensuales"]
    crecimiento_anual = float(config["estacionalidad"].get("crecimiento_anual_pct", 0.0))
    anio_inicio = pd.Timestamp(inicio).year
 
    pesos = []
    for fecha in fechas:
        mult_mes = float(multiplicadores[int(fecha.month)])
        mult_anio = (1 + crecimiento_anual) ** (int(fecha.year) - anio_inicio)
        pesos.append(mult_mes * mult_anio)
 
    pesos = np.array(pesos, dtype=float)
    pesos = pesos / pesos.sum()
    seleccion = rng.choice(fechas.to_numpy(), size=n_tickets, replace=True, p=pesos)
    return pd.DatetimeIndex(pd.to_datetime(seleccion))
 
 
def participacion_digital(config: Dict[str, Any], fecha: pd.Timestamp) -> float:
    """Calcula la participacion digital esperada entre inicio y fin del periodo."""
    cfg = config["canal_digital"]
    inicio = pd.Timestamp(config["periodo"]["inicio"])
    fin = pd.Timestamp(config["periodo"]["fin"])
    avance = (fecha - inicio).days / max((fin - inicio).days, 1)
    avance = float(np.clip(avance, 0, 1))
    return float(cfg["participacion_inicial"]) + avance * (
        float(cfg["participacion_final"]) - float(cfg["participacion_inicial"])
    )
 
 
def split_web(config: Dict[str, Any], fecha: pd.Timestamp) -> float:
    """Calcula la proporcion Web dentro del canal digital entre inicio y fin."""
    cfg = config["canal_digital"]
    inicio = pd.Timestamp(config["periodo"]["inicio"])
    fin = pd.Timestamp(config["periodo"]["fin"])
    avance = (fecha - inicio).days / max((fin - inicio).days, 1)
    avance = float(np.clip(avance, 0, 1))
    return float(cfg["split_web_inicial"]) + avance * (
        float(cfg["split_web_final"]) - float(cfg["split_web_inicial"])
    )
 
 
def construir_indices_clientes(clientes: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """Prepara clientes ordenados por fecha de registro para elegir solo clientes elegibles."""
    clientes_ordenados = clientes.sort_values("fecha_registro").reset_index(drop=True)
    fechas_registro = pd.to_datetime(clientes_ordenados["fecha_registro"]).to_numpy(dtype="datetime64[D]")
    ids_clientes = clientes_ordenados["id_cliente"].to_numpy()
    return fechas_registro, ids_clientes
 
 
def elegir_cliente_elegible(
    rng: np.random.Generator,
    fecha: pd.Timestamp,
    fechas_registro: np.ndarray,
    ids_clientes: np.ndarray,
) -> str:
    """Elige un cliente registrado antes o en la fecha del ticket."""
    fecha_np = np.datetime64(fecha.date())
    limite = int(np.searchsorted(fechas_registro, fecha_np, side="right"))
    if limite <= 0:
        limite = 1
    return str(ids_clientes[int(rng.integers(0, limite))])
 
 
def elegir_nodo_venta(
    config: Dict[str, Any],
    tiendas: pd.DataFrame,
    rng: np.random.Generator,
    fecha: pd.Timestamp,
) -> Tuple[str, str]:
    """Elige id_tienda y canal asegurando coherencia con tiendas.canal."""
    if rng.random() < participacion_digital(config, fecha):
        canal = "Web" if rng.random() < split_web(config, fecha) else "App"
        return ("WEB" if canal == "Web" else "APP"), canal
 
    ciudad = elegir_ponderado(rng, config["distribucion_ventas"]["pesos_ciudad"])
    tiendas_ciudad = tiendas[(tiendas["tipo"] == "Fisica") & (tiendas["ciudad"] == ciudad)]["id_tienda"].to_numpy()
    return str(rng.choice(tiendas_ciudad)), "Tienda"
 
 
def generar_descuento(config: Dict[str, Any], canal: str, rng: np.random.Generator, es_trujillo_afectado: bool) -> float:
    """Genera descuento por canal y aplica incremento para Trujillo afectado si corresponde."""
    cfg = config["descuentos"]["por_canal"][canal]
    maximo = float(config["descuentos"]["maximo_pct"])
 
    if rng.random() < float(cfg["proporcion_sin_descuento"]):
        descuento = 0.0
    else:
        descuento = float(rng.normal(float(cfg["media_pct"]), float(cfg["desviacion_estandar_pct"])))
 
    if es_trujillo_afectado:
        descuento += float(config["trujillo"]["aumento_descuento_pp"]) / 100.0
 
    return round(float(np.clip(descuento, 0.0, maximo)), 4)
 
 
def generar_ventas_base(
    config: Dict[str, Any],
    tiendas: pd.DataFrame,
    productos: pd.DataFrame,
    clientes: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Genera ventas a nivel de linea, manteniendo coherencia de ticket y relaciones."""
    n_tickets = int(config["volumenes"]["tickets_objetivo"])
    lineas_por_ticket = generar_lineas_por_ticket(config, rng)
    fechas_tickets = generar_fechas_tickets(config, rng, n_tickets)
    fechas_clientes, ids_clientes = construir_indices_clientes(clientes)
 
    # Catálogos preprocesados para evitar recalcular pesos dentro del bucle principal.
    cat_keys, cat_probs = normalizar_pesos(config["distribucion_ventas"]["pesos_categoria"])
    qty_keys, qty_probs = normalizar_pesos(config["distribucion_ventas"]["cantidad_normal"]["probabilidades"])
    qty_values = np.array([int(q) for q in qty_keys], dtype=int)
    city_keys, city_probs = normalizar_pesos(config["distribucion_ventas"]["pesos_ciudad"])
    
    cat_probs_trujillo = ajustar_probabilidades_mix_trujillo(config, cat_keys, cat_probs)

    payment_options = {}
    for canal, pesos in config["metodos_pago_por_canal"].items():
        payment_options[canal] = normalizar_pesos(pesos)
 
    stores_by_city = {
        ciudad: tiendas[(tiendas["tipo"] == "Fisica") & (tiendas["ciudad"] == ciudad)]["id_tienda"].to_numpy()
        for ciudad in city_keys
    }
    tiendas_lookup = tiendas.set_index("id_tienda").to_dict(orient="index")
 
    productos_por_categoria = {}
    for categoria, df in productos.groupby("categoria", sort=False):
        productos_por_categoria[categoria] = {
            "id_producto": df["id_producto"].to_numpy(),
            "precio_lista": df["precio_lista"].astype(float).to_numpy(),
        }
 
    variacion_precio = config["precios"]["variacion_historica_precio_pct"]
    var_min = float(variacion_precio["minima"])
    var_max = float(variacion_precio["maxima"])
    inicio_trujillo = pd.Timestamp(config["trujillo"]["inicio_problema"])
 
    filas = []
    id_linea = 1
 
    for i in range(n_tickets):
        fecha = pd.Timestamp(fechas_tickets[i])
        id_venta = f"V{i + 1:06d}"
        id_cliente = elegir_cliente_elegible(rng, fecha, fechas_clientes, ids_clientes)
 
        # Selección de nodo y canal, respetando la tendencia digital documentada.
        if rng.random() < participacion_digital(config, fecha):
            canal = "Web" if rng.random() < split_web(config, fecha) else "App"
            id_tienda = "WEB" if canal == "Web" else "APP"
        else:
            ciudad = city_keys[int(rng.choice(len(city_keys), p=city_probs))]
            tiendas_ciudad = stores_by_city[ciudad]
            id_tienda = str(tiendas_ciudad[int(rng.integers(0, len(tiendas_ciudad)))])
            canal = "Tienda"
 
        metodos, p_metodos = payment_options[canal]
        metodo_pago = metodos[int(rng.choice(len(metodos), p=p_metodos))]
 
        tienda = tiendas_lookup[id_tienda]
        es_trujillo_afectado = (
            canal == "Tienda"
            and tienda.get("ciudad") == "Trujillo"
            and fecha >= inicio_trujillo
        )
        probs_categoria = cat_probs_trujillo if es_trujillo_afectado else cat_probs
        
        for _ in range(int(lineas_por_ticket[i])):
            categoria = cat_keys[int(rng.choice(len(cat_keys), p=probs_categoria))]
            productos_categoria = productos_por_categoria[categoria]
            idx_producto = int(rng.integers(0, len(productos_categoria["id_producto"])))
            id_producto = str(productos_categoria["id_producto"][idx_producto])
            precio_lista = float(productos_categoria["precio_lista"][idx_producto])

            cantidad_base = int(qty_values[int(rng.choice(len(qty_values), p=qty_probs))])
            precio_unitario = redondear_monto(precio_lista * (1 + rng.uniform(var_min, var_max)))
            descuento_pct = generar_descuento(config, canal, rng, es_trujillo_afectado)
            cantidad = ajustar_cantidad_por_descuento(cantidad_base, descuento_pct, config, rng)
            monto_total = redondear_monto(cantidad * precio_unitario * (1 - descuento_pct))

            filas.append(
                (
                    f"L{id_linea:07d}",
                    id_venta,
                    fecha.date().isoformat(),
                    id_cliente,
                    id_tienda,
                    id_producto,
                    cantidad,
                    precio_unitario,
                    descuento_pct,
                    monto_total,
                    canal,
                    metodo_pago,
                )
            )
            id_linea += 1
 
    columnas = [
        "id_linea",
        "id_venta",
        "fecha",
        "id_cliente",
        "id_tienda",
        "id_producto",
        "cantidad",
        "precio_unitario",
        "descuento_pct",
        "monto_total",
        "canal",
        "metodo_pago",
    ]
    ventas = pd.DataFrame.from_records(filas, columns=columnas)
    return ventas

def asignar_clientes_a_tickets(
    ticket_ids: np.ndarray,
    cliente_ids: np.ndarray,
    rng: np.random.Generator,
) -> Dict[str, str]:
    """Asigna clientes a tickets garantizando que cada cliente objetivo aparezca al menos una vez."""
    tickets = np.array(ticket_ids, dtype=object).copy()
    clientes = np.array(cliente_ids, dtype=object).copy()

    rng.shuffle(tickets)
    rng.shuffle(clientes)

    asignaciones: Dict[str, str] = {}

    for i, ticket_id in enumerate(tickets):
        if i < len(clientes):
            cliente_id = clientes[i]
        else:
            cliente_id = clientes[int(rng.integers(0, len(clientes)))]

        asignaciones[str(ticket_id)] = str(cliente_id)

    return asignaciones


def calibrar_churn_descriptivo(
    config: Dict[str, Any],
    clientes: pd.DataFrame,
    ventas: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Calibra el churn descriptivo sin agregar columnas auxiliares."""
    ventas = ventas.copy()

    inicio_ventana = obtener_inicio_ventana_churn(config)
    fecha_inicio_ventas = pd.Timestamp(config["periodo"]["inicio"])

    min_churn = float(config["churn"]["proporcion_objetivo"]["minima"])
    max_churn = float(config["churn"]["proporcion_objetivo"]["maxima"])
    target_churn = (min_churn + max_churn) / 2

    clientes_tmp = clientes.copy()
    clientes_tmp["fecha_registro_dt"] = pd.to_datetime(clientes_tmp["fecha_registro"])

    candidatos = (
        clientes_tmp.loc[
            clientes_tmp["fecha_registro_dt"] <= fecha_inicio_ventas,
            "id_cliente",
        ]
        .astype(str)
        .to_numpy()
    )

    tickets = ventas[["id_venta", "fecha"]].drop_duplicates("id_venta").copy()
    tickets["fecha_dt"] = pd.to_datetime(tickets["fecha"])

    tickets_historicos = tickets.loc[tickets["fecha_dt"] < inicio_ventana, "id_venta"].astype(str).to_numpy()
    tickets_recientes = tickets.loc[tickets["fecha_dt"] >= inicio_ventana, "id_venta"].astype(str).to_numpy()

    if len(candidatos) == 0 or len(tickets_historicos) == 0 or len(tickets_recientes) == 0:
        return ventas

    max_elegibles_por_recientes = int(
        np.floor(len(tickets_recientes) / max(1 - target_churn, 0.0001))
    )

    n_elegibles = min(
        len(candidatos),
        len(tickets_historicos),
        max_elegibles_por_recientes,
    )

    if n_elegibles <= 0:
        return ventas

    elegibles = rng.choice(candidatos, size=n_elegibles, replace=False)

    n_activos = int(round(n_elegibles * (1 - target_churn)))
    n_activos = min(max(1, n_activos), len(tickets_recientes), n_elegibles)

    while n_activos < n_elegibles and (1 - n_activos / n_elegibles) > max_churn:
        n_activos += 1

    while n_activos > 1 and (1 - n_activos / n_elegibles) < min_churn:
        n_activos -= 1

    activos = rng.choice(elegibles, size=n_activos, replace=False)

    asignaciones_historicas = asignar_clientes_a_tickets(tickets_historicos, elegibles, rng)
    asignaciones_recientes = asignar_clientes_a_tickets(tickets_recientes, activos, rng)

    asignaciones = {}
    asignaciones.update(asignaciones_historicas)
    asignaciones.update(asignaciones_recientes)

    ventas["id_cliente"] = ventas["id_venta"].astype(str).map(asignaciones).fillna(ventas["id_cliente"])

    return ventas

def aplicar_outliers_cantidad(
    config: Dict[str, Any],
    ventas: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Inserta outliers controlados solo en ventas.cantidad y recalcula monto_total."""
    ventas = ventas.copy()

    cfg = config["calidad_datos"]["outliers"]
    proporcion = float(cfg["proporcion_objetivo"])
    cantidad_normal_max = int(cfg["cantidad_normal_maxima"])
    out_min = int(cfg["cantidad_outlier_minima"])
    out_max = int(cfg["cantidad_outlier_maxima"])

    elegibles = ventas.index[ventas["cantidad"].astype(int) <= cantidad_normal_max].to_numpy()
    n_outliers = int(round(len(ventas) * proporcion))
    n_outliers = min(n_outliers, len(elegibles))

    if n_outliers > 0:
        indices = rng.choice(elegibles, size=n_outliers, replace=False)
        ventas.loc[indices, "cantidad"] = rng.integers(out_min, out_max + 1, size=n_outliers)

    ventas["cantidad"] = ventas["cantidad"].astype(int)
    ventas = recalcular_monto_total(ventas)

    return ventas


def aplicar_faltantes_controlados(
    config: Dict[str, Any],
    clientes: pd.DataFrame,
    productos: pd.DataFrame,
    rng: np.random.Generator,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Inserta faltantes solo en campos permitidos por la configuracion."""
    clientes = clientes.copy()
    productos = productos.copy()

    cfg = config["calidad_datos"]["faltantes"]
    proporcion = float(cfg["proporcion_objetivo"])
    campos = cfg["campos_permitidos"]

    tablas = {
        "clientes": clientes,
        "productos": productos,
    }

    celdas_elegibles = []

    for tabla_nombre, columnas in campos.items():
        if tabla_nombre not in tablas:
            continue

        df = tablas[tabla_nombre]

        for columna in columnas:
            if columna not in df.columns:
                raise ValueError(f"Campo permitido no existe en {tabla_nombre}: {columna}")

            for idx in df.index:
                celdas_elegibles.append((tabla_nombre, idx, columna))

    n_faltantes = int(round(len(celdas_elegibles) * proporcion))

    if n_faltantes > 0:
        seleccion = rng.choice(len(celdas_elegibles), size=n_faltantes, replace=False)

        for pos in seleccion:
            tabla_nombre, idx, columna = celdas_elegibles[int(pos)]
            tablas[tabla_nombre].loc[idx, columna] = pd.NA

    return tablas["clientes"], tablas["productos"]

def aplicar_outliers_cantidad(
    config: Dict[str, Any],
    ventas: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Inserta outliers controlados solo en ventas.cantidad y recalcula monto_total."""
    ventas = ventas.copy()
    cfg = config["calidad_datos"]["outliers"]
    proporcion = float(cfg["proporcion_objetivo"])
    cantidad_normal_max = int(cfg["cantidad_normal_maxima"])
    out_min = int(cfg["cantidad_outlier_minima"])
    out_max = int(cfg["cantidad_outlier_maxima"])

    elegibles = ventas.index[ventas["cantidad"].astype(int) <= cantidad_normal_max].to_numpy()
    n_outliers = int(round(len(ventas) * proporcion))
    n_outliers = min(n_outliers, len(elegibles))

    if n_outliers > 0:
        indices = rng.choice(elegibles, size=n_outliers, replace=False)
        ventas.loc[indices, "cantidad"] = rng.integers(out_min, out_max + 1, size=n_outliers)

    ventas["cantidad"] = ventas["cantidad"].astype(int)
    ventas = recalcular_monto_total(ventas)
    return ventas


def aplicar_faltantes_controlados(
    config: Dict[str, Any],
    clientes: pd.DataFrame,
    productos: pd.DataFrame,
    rng: np.random.Generator,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Inserta faltantes solo en campos permitidos por la configuracion."""
    clientes = clientes.copy()
    productos = productos.copy()
    cfg = config["calidad_datos"]["faltantes"]
    proporcion = float(cfg["proporcion_objetivo"])
    campos = cfg["campos_permitidos"]

    tablas = {
        "clientes": clientes,
        "productos": productos,
    }

    celdas_elegibles = []
    for tabla_nombre, columnas in campos.items():
        if tabla_nombre not in tablas:
            continue
        df = tablas[tabla_nombre]
        for columna in columnas:
            if columna not in df.columns:
                raise ValueError(f"Campo permitido no existe en {tabla_nombre}: {columna}")
            for idx in df.index:
                celdas_elegibles.append((tabla_nombre, idx, columna))

    n_faltantes = int(round(len(celdas_elegibles) * proporcion))
    if n_faltantes > 0:
        seleccion = rng.choice(len(celdas_elegibles), size=n_faltantes, replace=False)
        for pos in seleccion:
            tabla_nombre, idx, columna = celdas_elegibles[int(pos)]
            tablas[tabla_nombre].loc[idx, columna] = pd.NA

    return tablas["clientes"], tablas["productos"]

 
def generar_inventario_base(
    config: Dict[str, Any],
    ventas: pd.DataFrame,
    productos: pd.DataFrame,
    tiendas: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    """Genera snapshots mensuales de inventario por producto, nodo y periodo."""
    ventas_tmp = ventas.copy()
    ventas_tmp["periodo"] = pd.to_datetime(ventas_tmp["fecha"]).dt.to_period("M").astype(str)

    unidades = (
        ventas_tmp
        .groupby(["id_producto", "id_tienda", "periodo"], as_index=False)
        .agg(unidades_vendidas=("cantidad", "sum"))
    )

    unidades_lookup: Dict[Tuple[str, str, str], int] = {
        (
            str(row["id_producto"]),
            str(row["id_tienda"]),
            str(row["periodo"]),
        ): int(row["unidades_vendidas"])
        for row in unidades.to_dict(orient="records")
    }

    periodos = pd.period_range(config["periodo"]["inicio"][:7], config["periodo"]["fin"][:7], freq="M").astype(str)
    ids_tienda = tiendas["id_tienda"].astype(str).tolist()
    productos_lookup = productos.set_index("id_producto")[["categoria", "costo_unitario"]].to_dict(orient="index")
    tiendas_lookup = tiendas.set_index("id_tienda").to_dict(orient="index")
 
    ventas_promedio = unidades.groupby(["id_producto", "id_tienda"])["unidades_vendidas"].mean().to_dict()
    cobertura_cfg = config["inventario"]["cobertura_stock_meses"]
    tasa_base = float(config["inventario"]["tasa_holding_mensual_pct"])
    inicio_trujillo = pd.Period(config["trujillo"]["inicio_problema"][:7], freq="M")
 
    filas = []
 
    for id_producto, producto in productos_lookup.items():
        costo_unitario = float(producto["costo_unitario"])
 
        for id_tienda in ids_tienda:
            promedio = float(ventas_promedio.get((id_producto, id_tienda), 0.0))
            if promedio <= 0:
                promedio = float(rng.uniform(0.2, 2.0))
 
            cobertura = float(
                np.clip(
                    rng.normal(cobertura_cfg["media"], cobertura_cfg["desviacion_estandar"]),
                    cobertura_cfg["minima"],
                    cobertura_cfg["maxima"],
                )
            )
            stock_inicial = int(np.ceil(promedio * cobertura + rng.integers(0, 5)))
 
            for periodo in periodos:
                unidades_vendidas = unidades_lookup.get((str(id_producto), str(id_tienda), str(periodo)), 0)
                objetivo_cierre = int(np.ceil(max(promedio * cobertura, unidades_vendidas * 0.25)))
                reabastecimiento = max(0, unidades_vendidas + objetivo_cierre - stock_inicial)
                stock_final = stock_inicial + reabastecimiento - unidades_vendidas
 
                periodo_obj = pd.Period(periodo, freq="M")
                tasa_holding = tasa_base
                tienda = tiendas_lookup[id_tienda]
                if (
                    tienda.get("tipo") == "Fisica"
                    and tienda.get("ciudad") == "Trujillo"
                    and periodo_obj >= inicio_trujillo
                ):
                    tasa_holding *= 1 + float(config["trujillo"]["aumento_costo_almacenamiento_pct"]) / 100.0
 
                stock_promedio = (stock_inicial + stock_final) / 2
                costo_almacenamiento = redondear_monto(stock_promedio * tasa_holding * costo_unitario)
 
                filas.append(
                    {
                        "id_producto": id_producto,
                        "id_tienda": id_tienda,
                        "periodo": periodo,
                        "stock_inicial": int(stock_inicial),
                        "unidades_vendidas": int(unidades_vendidas),
                        "reabastecimiento": int(reabastecimiento),
                        "stock_final": int(stock_final),
                        "costo_almacenamiento": costo_almacenamiento,
                    }
                )
 
                stock_inicial = int(stock_final)
 
    columnas = [
        "id_producto",
        "id_tienda",
        "periodo",
        "stock_inicial",
        "unidades_vendidas",
        "reabastecimiento",
        "stock_final",
        "costo_almacenamiento",
    ]
    inventario = pd.DataFrame(filas, columns=columnas)
    return inventario
 
 
def validar_integridad_basica(
    config: Dict[str, Any],
    tiendas: pd.DataFrame,
    productos: pd.DataFrame,
    clientes: pd.DataFrame,
    ventas: pd.DataFrame,
    inventario: pd.DataFrame,
) -> None:
    """Ejecuta validaciones minimas. La validacion completa sera una tarea posterior."""
    assert len(tiendas) == int(config["validacion"]["volumenes"]["tiendas_total"]), "Cantidad de tiendas incorrecta."
    assert len(productos) == int(config["validacion"]["volumenes"]["productos"]), "Cantidad de productos incorrecta."
    assert len(clientes) == int(config["validacion"]["volumenes"]["clientes"]), "Cantidad de clientes incorrecta."
 
    lineas_min = int(config["validacion"]["volumenes"]["lineas_ventas"]["minima"])
    lineas_max = int(config["validacion"]["volumenes"]["lineas_ventas"]["maxima"])
    assert lineas_min <= len(ventas) <= lineas_max, "Cantidad de lineas de venta fuera de rango."
 
    assert ventas["id_linea"].is_unique, "id_linea debe ser unico."
    assert tiendas["id_tienda"].is_unique, "id_tienda debe ser unico."
    assert productos["id_producto"].is_unique, "id_producto debe ser unico."
    assert clientes["id_cliente"].is_unique, "id_cliente debe ser unico."
 
    assert set(ventas["id_tienda"]).issubset(set(tiendas["id_tienda"])), "ventas.id_tienda contiene claves huerfanas."
    assert set(ventas["id_producto"]).issubset(set(productos["id_producto"])), "ventas.id_producto contiene claves huerfanas."
    assert set(ventas["id_cliente"]).issubset(set(clientes["id_cliente"])), "ventas.id_cliente contiene claves huerfanas."
    assert set(inventario["id_tienda"]).issubset(set(tiendas["id_tienda"])), "inventario.id_tienda contiene claves huerfanas."
    assert set(inventario["id_producto"]).issubset(set(productos["id_producto"])), "inventario.id_producto contiene claves huerfanas."
 
    monto_recalculado = (ventas["cantidad"] * ventas["precio_unitario"] * (1 - ventas["descuento_pct"])).round(2)
    diferencia_monto = (ventas["monto_total"] - monto_recalculado).abs().max()
    assert diferencia_monto <= 0.011, "monto_total no coincide con la formula oficial."
 
    ticket_cols = ["fecha", "id_cliente", "id_tienda", "canal", "metodo_pago"]
    max_valores_por_ticket = ventas.groupby("id_venta")[ticket_cols].nunique().max().max()
    assert max_valores_por_ticket == 1, "Hay tickets con campos de cabecera inconsistentes."
 
    ventas_tmp = ventas.copy()
    ventas_tmp["periodo"] = pd.to_datetime(ventas_tmp["fecha"]).dt.to_period("M").astype(str)
    unidades_ventas = ventas_tmp.groupby(["id_producto", "id_tienda", "periodo"])["cantidad"].sum()
    unidades_inv = inventario.set_index(["id_producto", "id_tienda", "periodo"])["unidades_vendidas"]
    unidades_inv_alineado = unidades_inv.reindex(unidades_ventas.index).fillna(-1).astype(int)
    assert (unidades_ventas.astype(int) == unidades_inv_alineado).all(), "Inventario no concilia con ventas."
 
    inventario_ordenado = inventario.sort_values(["id_producto", "id_tienda", "periodo"]).copy()
    stock_final_anterior = inventario_ordenado.groupby(["id_producto", "id_tienda"])["stock_final"].shift(1)
    mascara = stock_final_anterior.notna()
    assert (
        inventario_ordenado.loc[mascara, "stock_inicial"].to_numpy()
        == stock_final_anterior.loc[mascara].astype(int).to_numpy()
    ).all(), "La continuidad mensual de inventario no se cumple."
 
    assert (inventario["stock_final"] >= 0).all(), "stock_final no puede ser negativo."
 
 
def calcular_tasa_churn_descriptivo(
    config: Dict[str, Any],
    clientes: pd.DataFrame,
    ventas: pd.DataFrame,
) -> float:
    """Calcula tasa de churn descriptivo segun inactividad en la ventana final."""
    inicio_ventana = obtener_inicio_ventana_churn(config)

    clientes_tmp = clientes.copy()
    clientes_tmp["fecha_registro_dt"] = pd.to_datetime(clientes_tmp["fecha_registro"])

    ventas_tmp = ventas.copy()
    ventas_tmp["fecha_dt"] = pd.to_datetime(ventas_tmp["fecha"])

    clientes_registrados = set(
        clientes_tmp.loc[
            clientes_tmp["fecha_registro_dt"] < inicio_ventana,
            "id_cliente",
        ].astype(str)
    )

    compra_historica = set(
        ventas_tmp.loc[
            ventas_tmp["fecha_dt"] < inicio_ventana,
            "id_cliente",
        ].astype(str)
    )

    compra_reciente = set(
        ventas_tmp.loc[
            ventas_tmp["fecha_dt"] >= inicio_ventana,
            "id_cliente",
        ].astype(str)
    )

    elegibles = clientes_registrados & compra_historica

    if not elegibles:
        return 0.0

    churn = elegibles - compra_reciente
    return len(churn) / len(elegibles)

def validar_patrones_calidad(
    config: Dict[str, Any],
    tiendas: pd.DataFrame,
    productos: pd.DataFrame,
    clientes: pd.DataFrame,
    ventas: pd.DataFrame,
    inventario: pd.DataFrame,
) -> None:
    """Valida que los patrones principales existan sin exigir resultados exactos de modelos."""
    ventas_tmp = ventas.copy()
    ventas_tmp["fecha_dt"] = pd.to_datetime(ventas_tmp["fecha"])
    ventas_tmp["anio"] = ventas_tmp["fecha_dt"].dt.year
    ventas_tmp["mes"] = ventas_tmp["fecha_dt"].dt.month

    tickets = ventas_tmp.drop_duplicates("id_venta").copy()

    tickets_mes = tickets.groupby("mes").size().reindex(range(1, 13), fill_value=0)
    meses_base = [m for m in range(1, 13) if m not in (7, 12)]
    base = tickets_mes.loc[meses_base].mean()

    assert tickets_mes.loc[7] > base, "No se observa pico de tickets en julio."
    assert tickets_mes.loc[12] > base, "No se observa pico de tickets en diciembre."

    digital_por_anio = (
        tickets.assign(es_digital=tickets["canal"].isin(["Web", "App"]))
        .groupby("anio")["es_digital"]
        .mean()
    )

    assert digital_por_anio.loc[2025] > digital_por_anio.loc[2023], (
        "La participacion digital no crece de 2023 a 2025."
    )

    ventas_prod = ventas_tmp.merge(
        productos[["id_producto", "costo_unitario"]],
        on="id_producto",
        how="left",
    )
    ventas_prod = ventas_prod.merge(
        tiendas[["id_tienda", "tipo", "ciudad"]],
        on="id_tienda",
        how="left",
    )

    ventas_prod["margen_bruto_proxy"] = (
        ventas_prod["monto_total"]
        - ventas_prod["cantidad"] * ventas_prod["costo_unitario"]
    ) / ventas_prod["monto_total"].replace(0, np.nan)

    trujillo = ventas_prod[
        (ventas_prod["tipo"] == "Fisica")
        & (ventas_prod["ciudad"] == "Trujillo")
    ].copy()

    base_trujillo = trujillo[
        (trujillo["fecha_dt"] >= "2025-01-01")
        & (trujillo["fecha_dt"] < "2025-04-01")
    ]["margen_bruto_proxy"].mean()

    afectado_trujillo = trujillo[
        (trujillo["fecha_dt"] >= "2025-04-01")
        & (trujillo["fecha_dt"] < "2025-07-01")
    ]["margen_bruto_proxy"].mean()

    assert not pd.isna(base_trujillo), "No hay datos base suficientes para Trujillo."
    assert not pd.isna(afectado_trujillo), "No hay datos afectados suficientes para Trujillo."
    assert afectado_trujillo < base_trujillo, (
        "No se observa deterioro de margen proxy en Trujillo desde 2025-Q2."
    )

    corr_valor = ventas_tmp["descuento_pct"].astype(float).corr(
        ventas_tmp["cantidad"].astype(float)
    )
    corr = 0.0 if pd.isna(corr_valor) else float(corr_valor)

    assert corr > 0, "La relacion descuento-demanda no muestra asociacion positiva."

    tasa_churn = calcular_tasa_churn_descriptivo(config, clientes, ventas)
    min_churn = float(config["churn"]["proporcion_objetivo"]["minima"])
    max_churn = float(config["churn"]["proporcion_objetivo"]["maxima"])

    assert min_churn <= tasa_churn <= max_churn, (
        f"Tasa churn fuera de rango: {tasa_churn:.2%}"
    )

    campos = config["calidad_datos"]["faltantes"]["campos_permitidos"]
    tablas = {
        "clientes": clientes,
        "productos": productos,
        "tiendas": tiendas,
        "ventas": ventas,
        "inventario": inventario,
    }

    faltantes = 0
    elegibles = 0

    for tabla_nombre, columnas in campos.items():
        df = tablas[tabla_nombre]

        for columna in columnas:
            elegibles += len(df)
            faltantes += int(df[columna].isna().sum())

    pct_faltantes = (faltantes / max(elegibles, 1)) * 100
    rango_faltantes = config["validacion"]["faltantes"]["rango_pct"]

    assert rango_faltantes[0] <= pct_faltantes <= rango_faltantes[1], (
        f"Faltantes fuera de rango: {pct_faltantes:.2f}%"
    )

    nulos_estructurales_por_tabla = {
        "tiendas": {"ciudad", "region", "area_m2"},
        "productos": set(),
        "clientes": set(),
        "ventas": set(),
        "inventario": set(),
    }

    for tabla_nombre, df in tablas.items():
        permitidos = (
            set(campos.get(tabla_nombre, []))
            | nulos_estructurales_por_tabla.get(tabla_nombre, set())
        )
        columnas_no_permitidas = [c for c in df.columns if c not in permitidos]

        assert not df[columnas_no_permitidas].isna().any().any(), (
            f"Nulos no permitidos en {tabla_nombre}."
        )

    tiendas_virtuales = tiendas["tipo"].eq("Virtual")
    tiendas_fisicas = tiendas["tipo"].eq("Fisica")

    assert tiendas.loc[tiendas_virtuales, ["ciudad", "region", "area_m2"]].isna().all().all(), (
        "Los nodos virtuales deben tener ciudad, region y area_m2 nulos."
    )

    assert tiendas.loc[tiendas_fisicas, ["ciudad", "region", "area_m2"]].notna().all().all(), (
        "Las tiendas fisicas deben tener ciudad, region y area_m2 informados."
    )

    assert (tiendas.loc[tiendas_fisicas, "area_m2"].astype(float) > 0).all(), (
        "Las tiendas fisicas deben tener area_m2 mayor que cero."
    )

    out_cfg = config["calidad_datos"]["outliers"]
    pct_outliers = (
        ventas["cantidad"].astype(int) > int(out_cfg["cantidad_normal_maxima"])
    ).mean() * 100

    rango_outliers = config["validacion"]["outliers"]["rango_pct"]

    assert rango_outliers[0] <= pct_outliers <= rango_outliers[1], (
        f"Outliers fuera de rango: {pct_outliers:.2f}%"
    )

    assert not ventas.isna().any().any(), "ventas.csv no debe contener nulos."
    assert not inventario.isna().any().any(), "inventario.csv no debe contener nulos."

 
def guardar_csv(tablas: Dict[str, pd.DataFrame], config: Dict[str, Any]) -> None:
    """Guarda los CSV configurados sin tocar data_dictionary.md."""
    directorio = ROOT / config["salidas"]["directorio"]
    directorio.mkdir(parents=True, exist_ok=True)
 
    archivos = config["salidas"]["archivos"]
    for nombre_tabla, df in tablas.items():
        ruta = directorio / archivos[nombre_tabla]
        df.to_csv(ruta, index=False, encoding="utf-8")
 
 
def imprimir_resumen(seed: int, tablas: Dict[str, pd.DataFrame]) -> None:
    """Imprime un resumen simple para la revision del PR."""
    print("\nGeneracion completada correctamente.")
    print(f"Semilla: {seed}")
    print(f"Salida: {DATA_DIR.relative_to(ROOT)}/")
    for nombre, df in tablas.items():
        print(f"- {nombre}.csv: {len(df):,} filas")
 
    ventas = tablas["ventas"]
    print(f"- tickets unicos: {ventas['id_venta'].nunique():,}")
    print(f"- lineas por ticket promedio: {len(ventas) / ventas['id_venta'].nunique():.2f}")
 
 
def main() -> None:
    config = cargar_config()
    seed, rng, fake = configurar_semillas(config)

    tiendas = generar_tiendas(config, fake, rng)
    productos = generar_productos(config, fake, rng)
    clientes = generar_clientes(config, fake, rng)

    ventas = generar_ventas_base(config, tiendas, productos, clientes, rng)
    ventas = calibrar_churn_descriptivo(config, clientes, ventas, rng)
    ventas = aplicar_outliers_cantidad(config, ventas, rng)

    clientes, productos = aplicar_faltantes_controlados(config, clientes, productos, rng)

    inventario = generar_inventario_base(config, ventas, productos, tiendas, rng)

    tablas = {
        "tiendas": tiendas,
        "productos": productos,
        "clientes": clientes,
        "ventas": ventas,
        "inventario": inventario,
    }

    validar_integridad_basica(config, tiendas, productos, clientes, ventas, inventario)
    validar_patrones_calidad(config, tiendas, productos, clientes, ventas, inventario)

    guardar_csv(tablas, config)
    imprimir_resumen(seed, tablas)

 
if __name__ == "__main__":
    main()


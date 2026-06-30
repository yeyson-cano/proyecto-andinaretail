# Diccionario de datos — AndinaRetail S.A.C.

## Propósito

Referencia authoritative para el generador de datos sintéticos y para todos los notebooks del proyecto. Toda decisión de esquema, tipo, dominio o fórmula que no esté aquí debe resolverse antes de escribir código.

Fuente canónica: `docs/00_especificacion_datos_y_analitica.md`, Sección 11.

---

## Tablas

| Tabla | Archivo | PK | Granularidad |
|---|---|---|---|
| tiendas | tiendas.csv | `id_tienda` | 1 fila por tienda física o nodo virtual nacional |
| productos | productos.csv | `id_producto` | 1 fila por SKU |
| clientes | clientes.csv | `id_cliente` | 1 fila por cliente registrado |
| ventas | ventas.csv | `id_linea` | 1 fila por línea de producto dentro de una venta |
| inventario | inventario.csv | (`id_producto`, `id_tienda`, `periodo`) | 1 snapshot mensual por (producto, tienda) |

---

## tiendas.csv

**PK:** `id_tienda`

| Campo | Tipo | Nulable | Dominio | Descripción |
|---|---|---|---|---|
| id_tienda | string | No | Único, ej. `T001`, `WEB`, `APP` | Identificador del nodo de venta |
| nombre | string | No | Ficticio | Nombre de la tienda o nodo |
| canal | string | No | `Tienda` \| `Web` \| `App` | Canal de venta; es la fuente de verdad para `ventas.canal` |
| ciudad | string | Sí | `Lima` \| `Arequipa` \| `Trujillo` \| `Cusco` \| `Piura` \| `NULL` | `NULL` para los nodos Web y App (nacionales) |
| region | string | Sí | `Costa` \| `Sierra` | `NULL` para nodos digitales. Mapeo: Lima / Trujillo / Piura → `Costa`; Arequipa / Cusco → `Sierra` |
| area_m2 | numeric | Sí | > 0 | Solo aplica cuando `canal = Tienda` |
| fecha_apertura | date | No | 2020-01-01 a 2022-12-31 | Fecha de apertura o activación del nodo |

**Valores especiales:**
- `id_tienda = 'WEB'`, `canal = 'Web'`, `ciudad = NULL` → nodo nacional Web
- `id_tienda = 'APP'`, `canal = 'App'`, `ciudad = NULL` → nodo nacional App

---

## productos.csv

**PK:** `id_producto`

| Campo | Tipo | Nulable | Dominio | Descripción |
|---|---|---|---|---|
| id_producto | string | No | Único, ej. `P0001` | Identificador del producto |
| nombre | string | No | Ficticio | Nombre del producto |
| categoria | string | No | `Abarrotes` \| `Bebidas` \| `Limpieza` \| `Cuidado Personal` \| `Electrohogar` \| `Hogar` | Categoría principal |
| subcategoria | string | Sí | Lista controlada por categoría (pendiente F0-04) | Subcategoría |
| marca | string | Sí | Ficticia | Marca del producto |
| precio_lista | numeric | No | > 0, en PEN | Precio base sin descuento |
| costo_unitario | numeric | No | > 0 y < `precio_lista` | Costo de adquisición por unidad. Siempre menor que `precio_lista`; el alza en Trujillo se codifica en `config/` |
| fecha_alta | date | No | 2022-01-01 a 2023-01-01 | Fecha desde la cual el producto está disponible |

---

## clientes.csv

**PK:** `id_cliente`

| Campo | Tipo | Nulable | Dominio | Descripción |
|---|---|---|---|---|
| id_cliente | string | No | Único, ej. `C00001` | Identificador del cliente |
| nombre | string | No | Ficticio (Faker) | Nombre completo generado |
| edad | integer | Sí | 18 a 80 | Edad en años al momento del registro |
| genero | string | Sí | `M` \| `F` \| `No especificado` | Género sintético |
| ciudad | string | No | `Lima` \| `Arequipa` \| `Trujillo` \| `Cusco` \| `Piura` | Ciudad del cliente. Para ventas digitales, este campo es el ancla geográfica |
| distrito | string | Sí | Ficticio | Distrito dentro de la ciudad |
| fecha_registro | date | No | 2020-01-01 a 2025-12-31 | Fecha de registro (puede ser anterior al periodo de ventas 2023–2025) |
| canal_preferido | string | Sí | `Tienda` \| `Web` \| `App` | Canal declarado al registro; no se usa como feature de ML |

> **Ausente por diseño:** no existe campo `segmento`. La segmentación RFM es un output de la Parte 2, derivado de `ventas`. Incluirlo en la fuente haría trivial el ejercicio analítico.

---

## ventas.csv

**PK:** `id_linea`  
**Agrupador de ticket:** `id_venta` (varias filas con el mismo `id_venta` forman un único ticket)

| Campo | Tipo | Nulable | Dominio | Descripción |
|---|---|---|---|---|
| id_linea | string | No | Único, ej. `L0000001` | PK de la línea de venta |
| id_venta | string | No | Puede repetirse (agrupa líneas del mismo ticket) | Identificador del ticket / compra |
| fecha | date | No | 2023-01-01 a 2025-12-31 | Fecha de la transacción |
| id_cliente | string | No | FK → `clientes.id_cliente` | Cliente que realizó la compra |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Nodo de venta |
| id_producto | string | No | FK → `productos.id_producto` | Producto vendido en esta línea |
| cantidad | integer | No | ≥ 1 | Unidades vendidas |
| precio_unitario | numeric | No | > 0, en PEN | Precio aplicado (puede diferir de `precio_lista` por campañas) |
| descuento_pct | numeric | No | 0.00 a 0.35 | Porcentaje de descuento (0 = sin descuento) |
| monto_total | numeric | No | > 0, en PEN | Derivado almacenado; ver fórmulas oficiales |
| canal | string | No | `Tienda` \| `Web` \| `App` | Denormalización de `tiendas.canal`; debe coincidir con el canal del `id_tienda` referenciado |
| metodo_pago | string | No | `Efectivo` \| `Tarjeta débito` \| `Tarjeta crédito` \| `Billetera digital` \| `Transferencia` | Medio de pago |

---

## inventario.csv

**PK compuesta:** (`id_producto`, `id_tienda`, `periodo`)

| Campo | Tipo | Nulable | Dominio | Descripción |
|---|---|---|---|---|
| id_producto | string | No | FK → `productos.id_producto` | Producto del snapshot |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Tienda del snapshot |
| periodo | string | No | Formato `AAAA-MM` | Mes al que corresponde el snapshot |
| stock_inicial | integer | No | ≥ 0 | Unidades disponibles al inicio del mes |
| unidades_vendidas | integer | No | ≥ 0 | Unidades salidas por ventas durante el mes |
| reabastecimiento | integer | No | ≥ 0 | Unidades ingresadas por reposición durante el mes |
| stock_final | integer | No | ≥ 0 | `stock_inicial + reabastecimiento − unidades_vendidas` |
| costo_almacenamiento | numeric | No | ≥ 0, en PEN | Costo total mensual de almacenamiento. Cálculo: `stock_promedio × tasa_holding_mensual × costo_unitario`; la tasa se define en `config/` |

---

## Relaciones

```
ventas.id_cliente      → clientes.id_cliente
ventas.id_tienda       → tiendas.id_tienda
ventas.id_producto     → productos.id_producto
inventario.id_tienda   → tiendas.id_tienda
inventario.id_producto → productos.id_producto
```

**Regla de geografía digital:** para ventas con `canal IN ('Web', 'App')`, obtener la ciudad mediante `ventas → clientes → clientes.ciudad`. No usar `tiendas.ciudad` (es `NULL` para nodos digitales).

---

## Fórmulas oficiales

```python
# Nivel de línea (calculadas durante la generación, monto_total se almacena)
venta_bruta     = cantidad * precio_unitario
descuento_monto = venta_bruta * descuento_pct
monto_total     = venta_bruta - descuento_monto          # campo almacenado en ventas.csv
costo_total     = cantidad * costo_unitario
margen_bruto    = monto_total - costo_total
margen_pct      = margen_bruto / monto_total             # sin riesgo de /0 (ver nota)

# Nivel de ticket (medida agregada, no almacenada)
# ticket = ventas.groupby("id_venta")["monto_total"].sum()

# Nivel de inventario
# stock_final = stock_inicial + reabastecimiento - unidades_vendidas
```

**Notas:**
- `monto_total > 0` está garantizado por dominio (`cantidad ≥ 1`, `precio_unitario > 0`, `descuento_pct ≤ 0.35 < 1`). No se necesita guarda NULL en `margen_pct`.
- `margen_bruto < 0` es un resultado válido (costo > precio neto). Es el patrón artificial de Trujillo desde Q2 2025 y no debe ser rechazado por el validador.
- `precio_unitario` puede diferir de `productos.precio_lista`. El descuento se aplica sobre `precio_unitario`.

---

## Reglas de integridad

| # | Regla |
|---|---|
| 1 | Sin nulos en campos no nulables |
| 2 | `ventas.fecha` ∈ [2023-01-01, 2025-12-31] |
| 3 | `ventas.cantidad ≥ 1` |
| 4 | `ventas.precio_unitario > 0` |
| 5 | `ventas.descuento_pct` ∈ [0.00, 0.35] |
| 6 | `ventas.monto_total = cantidad × precio_unitario × (1 − descuento_pct)` (tolerancia ± 0.01 PEN) |
| 7 | `ventas.canal = tiendas.canal` para cada `id_tienda` |
| 8 | `inventario.stock_final = stock_inicial + reabastecimiento − unidades_vendidas` |
| 9 | `inventario.stock_final ≥ 0` |
| 10 | `productos.costo_unitario < productos.precio_lista` |
| 11 | Sin claves foráneas huérfanas |

---

## Aspectos pendientes (definir en F0-04 o posterior)

- Subcategorías por categoría de producto.
- Volúmenes exactos de filas por tabla.
- Rango de `descuento_pct` por canal o categoría.
- Tasa `holding` mensual para `costo_almacenamiento`.
- Umbral de días que define un cliente como inactivo (churn).
- Granularidad y horizonte del pronóstico de demanda.
- Criterios automáticos del script de validación.

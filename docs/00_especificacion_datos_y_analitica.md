# Especificación de datos y analítica — AndinaRetail S.A.C.

## 1. Propósito del documento

Este documento consolida las decisiones funcionales, analíticas y técnicas que guiarán el desarrollo del Proyecto Grupal de la asignatura Analítica de Datos.

Su finalidad es proporcionar una referencia común para los cinco integrantes del equipo y asegurar que la generación de datos sintéticos, los análisis estadísticos, los modelos descriptivos, predictivos y prescriptivos, y los tableros de Power BI formen parte de una única solución coherente.

El documento será ampliado progresivamente durante la Fase 0 con el contrato de datos, los parámetros de generación, las definiciones analíticas, los criterios de validación y la trazabilidad entre las cinco partes del proyecto.

## 2. Descripción del caso

AndinaRetail S.A.C. es una empresa ficticia peruana del sector retail omnicanal. Opera tiendas físicas y canales digitales en las ciudades de Lima, Arequipa, Trujillo, Cusco y Piura.

La empresa atiende a clientes minoristas y comercializa productos pertenecientes a las siguientes categorías:

- Abarrotes.
- Bebidas.
- Limpieza.
- Cuidado Personal.
- Electrohogar.
- Hogar.

Los canales de venta considerados serán:

- Tienda física.
- Web.
- Aplicación móvil.

Las transacciones serán representadas mediante datos completamente sintéticos. No se utilizarán datos reales de personas ni de empresas.

## 3. Objetivo general del proyecto

Diseñar y ejecutar una solución integral de analítica de datos para AndinaRetail S.A.C., utilizando datos sintéticos reproducibles para comprender el comportamiento de las ventas y los clientes, diagnosticar problemas de margen, anticipar la demanda y la inactividad de clientes, recomendar decisiones de inventario y comunicar los resultados mediante tableros gerenciales.

## 4. Alcance del proyecto

### 4.1 Alcance temporal

El conjunto principal de ventas representará operaciones realizadas entre:

- Fecha inicial: 1 de enero de 2023.
- Fecha final: 31 de diciembre de 2025.

Este periodo permitirá analizar tres años completos, observar estacionalidad anual, comparar tendencias entre periodos y construir problemas predictivos con información histórica.

### 4.2 Alcance geográfico

El proyecto abarcará cinco ciudades del Perú:

- Lima.
- Arequipa.
- Trujillo.
- Cusco.
- Piura.

El problema diagnóstico principal se concentrará en las operaciones de Trujillo a partir del segundo trimestre de 2025.

### 4.3 Alcance comercial

Se analizarán:

- Ventas y tickets.
- Productos y categorías.
- Clientes y comportamiento de compra.
- Canales físicos y digitales.
- Descuentos.
- Costos y margen.
- Inventario y reabastecimiento.
- Inactividad de clientes.
- Demanda futura.

### 4.4 Alcance analítico

El proyecto cubrirá cinco niveles complementarios:

1. Analítica estadística para caracterizar el negocio y contrastar hipótesis.
2. Analítica descriptiva y diagnóstica para explicar tendencias, segmentos y causas.
3. Analítica predictiva para estimar demanda y riesgo de inactividad.
4. Analítica prescriptiva para recomendar decisiones de reposición de inventario.
5. Visualización ejecutiva en Power BI para comunicar resultados y apoyar decisiones.

## 5. Exclusiones del alcance

Quedan fuera del alcance del proyecto:

- El uso de información real de personas o empresas.
- La integración con sistemas transaccionales reales.
- La implementación de una aplicación productiva o servicio en línea.
- La ejecución automática de acciones comerciales reales.
- El análisis de proveedores, logística internacional o recursos humanos.
- La optimización integral de todas las operaciones de la empresa.
- El desarrollo de modelos para problemas distintos de demanda y churn, salvo que el equipo lo justifique posteriormente.
- La inclusión de ciudades o categorías diferentes de las aprobadas durante la Fase 0.

Estas exclusiones buscan evitar el crecimiento innecesario del alcance durante el plazo disponible.

## 6. Preocupaciones estratégicas

La solución analítica responderá a cuatro preocupaciones principales de la Gerencia General:

1. Comprender el comportamiento de las ventas, los tickets y los clientes.
2. Explicar los patrones históricos y diagnosticar la caída del margen en Trujillo.
3. Anticipar la demanda y la probabilidad de inactividad de los clientes.
4. Recomendar decisiones de inventario y comunicar los resultados mediante tableros ejecutivos.

## 7. Preguntas de negocio

### 7.1 Parte 1 — Técnicas estadísticas

Pregunta principal:

> ¿Cómo se distribuyen las ventas, los tickets y los clientes, y existen diferencias estadísticamente significativas entre canales, ciudades o categorías?

Preguntas complementarias:

- ¿El ticket promedio difiere entre el canal físico y los canales digitales?
- ¿El margen presenta diferencias significativas entre ciudades?
- ¿Existe asociación entre la categoría comprada y el método de pago?
- ¿Qué relación existe entre el descuento aplicado y la cantidad vendida?

### 7.2 Parte 2 — Analítica descriptiva y diagnóstica

Pregunta principal:

> ¿Qué patrones históricos, tendencias y factores explican el desempeño de AndinaRetail?

Preguntas complementarias:

- ¿Qué tendencias y estacionalidades presentan las ventas y los márgenes?
- ¿Qué productos, clientes y categorías concentran la mayor parte de los resultados?
- ¿Qué segmentos de clientes pueden identificarse mediante su comportamiento de compra?
- ¿Por qué cae el margen de Trujillo desde el segundo trimestre de 2025?
- ¿Qué participación tienen los descuentos, los costos de almacenamiento y la mezcla de productos en esta caída?

### 7.3 Parte 3 — Modelos predictivos

Preguntas principales:

> ¿Qué demanda se espera por periodo, ciudad, canal y categoría?

> ¿Qué clientes presentan mayor probabilidad de volverse inactivos?

El proyecto abordará:

- Un problema de regresión para pronosticar demanda.
- Un problema de clasificación para predecir churn o inactividad.

Las definiciones detalladas de variable objetivo, granularidad, horizonte y cortes temporales se establecerán en una sección posterior de este documento.

### 7.4 Parte 4 — Modelo prescriptivo

Pregunta principal:

> ¿Cuánto inventario debería reponerse para atender la demanda esperada y controlar los costos operativos?

El problema prescriptivo se orientará inicialmente a recomendar cantidades de reposición considerando:

- Demanda pronosticada.
- Inventario disponible.
- Presupuesto.
- Capacidad.
- Costos de almacenamiento.
- Nivel de servicio.

La formulación matemática y los parámetros concretos se definirán posteriormente.

### 7.5 Parte 5 — Power BI

Pregunta principal:

> ¿Cómo integrar y monitorear los principales resultados del proyecto en tableros que faciliten la toma de decisiones gerenciales?

El tablero deberá permitir revisar:

- Indicadores ejecutivos.
- Ventas y margen.
- Tendencias por ciudad, categoría, canal y tiempo.
- Segmentos de clientes y riesgo de churn.
- Pronósticos de demanda.
- Recomendaciones de reposición y escenarios.

## 8. Relación entre preguntas y partes del proyecto

| Parte | Propósito | Pregunta central | Resultado esperado |
|---|---|---|---|
| Parte 1 | Caracterizar y contrastar | ¿Existen diferencias relevantes entre grupos? | Estadísticos, hipótesis e intervalos de confianza |
| Parte 2 | Explicar qué pasó y por qué | ¿Qué patrones y causas explican el desempeño? | Tendencias, Pareto, segmentos y diagnóstico del margen |
| Parte 3 | Anticipar | ¿Qué demanda habrá y qué clientes pueden quedar inactivos? | Pronósticos y probabilidades de churn |
| Parte 4 | Recomendar | ¿Cuánto inventario conviene reponer? | Plan de reposición y análisis de escenarios |
| Parte 5 | Comunicar | ¿Cómo monitorear los resultados para decidir? | Tableros ejecutivos de Power BI |

## 9. Decisiones aprobadas

Durante la reunión inicial del equipo se aprobaron las siguientes decisiones generales:

- Mantener el caso AndinaRetail S.A.C.
- Mantener el sector retail omnicanal.
- Considerar las cinco ciudades propuestas en el documento oficial.
- Mantener las seis categorías propuestas.
- Analizar el periodo 2023–2025.
- Utilizar Trujillo como ciudad principal del diagnóstico de margen.
- Desarrollar un modelo de demanda y un modelo de churn.
- Utilizar la reposición de inventario como problema prescriptivo.
- Integrar los resultados en Power BI.
- Utilizar únicamente datos sintéticos y reproducibles.

## 10. Aspectos que se definirán en tareas posteriores

Los siguientes elementos no se fijan en esta sección y serán desarrollados en las siguientes actividades de la Fase 0:

- Tablas, campos, tipos, claves y relaciones.
- Fórmulas oficiales de venta, ticket, costo y margen.
- Volúmenes exactos de registros.
- Magnitud de los picos de julio y diciembre.
- Evolución cuantitativa del canal digital.
- Magnitud de la caída de margen en Trujillo.
- Porcentajes de descuentos y costos de almacenamiento.
- Definición temporal y variables del churn.
- Granularidad y horizonte del pronóstico de demanda.
- Función objetivo y restricciones del modelo prescriptivo.
- Criterios automáticos de aceptación del dataset.
- Archivos de salida de cada fase.

## 11. Contrato de datos

### 11.1 Principios generales

- Los datos serán 100 % sintéticos y reproducibles (semilla fija en `config/`).
- Las tablas mínimas son: `tiendas`, `productos`, `clientes`, `ventas` e `inventario`.
- Cada fila de `ventas` representa **una línea de producto dentro de una compra**. Un ticket (compra completa) se identifica por `id_venta`; varias filas pueden compartir el mismo `id_venta`.
- Las fórmulas oficiales definidas en la sección 11.5 se aplican de forma idéntica en todas las partes del proyecto.
- La caída artificial de margen en Trujillo desde el Q2 2025 se produce mediante parámetros de generación en `config/`, no mediante excepciones al esquema de datos.

### 11.2 Tablas oficiales

| Tabla | Archivo | Granularidad | Descripción |
|---|---|---|---|
| tiendas | tiendas.csv | 1 fila por tienda física o nodo virtual nacional | Catálogo de puntos de venta (físicos y digitales) |
| productos | productos.csv | 1 fila por producto (SKU) | Catálogo de productos con precios y costos |
| clientes | clientes.csv | 1 fila por cliente registrado | Datos demográficos y de registro |
| ventas | ventas.csv | 1 fila por línea de producto dentro de una venta | Tabla de hechos principal del proyecto |
| inventario | inventario.csv | 1 snapshot mensual por combinación (producto, tienda) | Estado mensual de stock y costos de almacenamiento |

### 11.3 Diccionario preliminar de campos

#### tiendas.csv — PK: `id_tienda`

| Campo | Tipo | Nulable | Dominio / regla | Descripción |
|---|---|---|---|---|
| id_tienda | string | No | Único, ej. `T001`, `WEB`, `APP` | Identificador del nodo de venta |
| nombre | string | No | Ficticio | Nombre de la tienda o nodo |
| canal | string | No | `Tienda` \| `Web` \| `App` | Canal de venta; determina el valor de `ventas.canal` |
| ciudad | string | Sí | Lima, Arequipa, Trujillo, Cusco, Piura, `NULL` | `NULL` para los nodos Web y App (alcance nacional) |
| region | string | Sí | `Costa` \| `Sierra` | `NULL` para nodos digitales. Lima / Trujillo / Piura → Costa; Arequipa / Cusco → Sierra |
| area_m2 | numeric | Sí | > 0 | Superficie de la tienda; solo aplica cuando `canal = Tienda` |
| fecha_apertura | date | No | 2020-01-01 a 2022-12-31 | Fecha de apertura o activación del nodo |

> Los canales digitales se representan con **exactamente 1 fila Web y 1 fila App** en esta tabla (nodos nacionales). Para ventas digitales, la ciudad de referencia es `clientes.ciudad`, no `tiendas.ciudad`.

#### productos.csv — PK: `id_producto`

| Campo | Tipo | Nulable | Dominio / regla | Descripción |
|---|---|---|---|---|
| id_producto | string | No | Único, ej. `P0001` | Identificador del producto |
| nombre | string | No | Ficticio | Nombre del producto |
| categoria | string | No | Abarrotes \| Bebidas \| Limpieza \| Cuidado Personal \| Electrohogar \| Hogar | Categoría principal |
| subcategoria | string | Sí | Lista controlada por categoría (definir en F0-04) | Subcategoría del producto |
| marca | string | Sí | Ficticia | Marca del producto |
| precio_lista | numeric | No | > 0, en PEN | Precio base sin descuento |
| costo_unitario | numeric | No | > 0 y < `precio_lista` | Costo de adquisición por unidad. El alza artificial en Trujillo va en `config/`, no aquí |
| fecha_alta | date | No | 2022-01-01 a 2023-01-01 | Fecha desde la cual el producto está disponible para la venta |

#### clientes.csv — PK: `id_cliente`

| Campo | Tipo | Nulable | Dominio / regla | Descripción |
|---|---|---|---|---|
| id_cliente | string | No | Único, ej. `C00001` | Identificador del cliente |
| nombre | string | No | Ficticio (Faker) | Nombre completo generado sintéticamente |
| edad | integer | Sí | 18 a 80 | Edad en años al momento del registro |
| genero | string | Sí | `M` \| `F` \| `No especificado` | Género sintético |
| ciudad | string | No | Lima, Arequipa, Trujillo, Cusco, Piura | Ciudad del cliente — ancla geográfica para ventas digitales |
| distrito | string | Sí | Ficticio | Distrito dentro de la ciudad |
| fecha_registro | date | No | 2020-01-01 a 2025-12-31 | Fecha de registro del cliente (puede ser anterior al periodo de ventas) |
| canal_preferido | string | Sí | `Tienda` \| `Web` \| `App` | Canal de compra más frecuente declarado al registro |

> No existe campo `segmento` en esta tabla. La segmentación RFM es un **output analítico** de la Parte 2, derivado de `ventas`. Incluirlo como campo de entrada haría trivial el ejercicio de segmentación.

#### ventas.csv — PK: `id_linea`

| Campo | Tipo | Nulable | Dominio / regla | Descripción |
|---|---|---|---|---|
| id_linea | string | No | Único, ej. `L0000001` | PK de la línea de venta |
| id_venta | string | No | Puede repetirse; agrupa líneas del mismo ticket | Identificador del ticket o compra |
| fecha | date | No | 2023-01-01 a 2025-12-31 | Fecha de la transacción |
| id_cliente | string | No | FK → `clientes.id_cliente` | Cliente que realizó la compra |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Nodo de venta (tienda física o virtual) |
| id_producto | string | No | FK → `productos.id_producto` | Producto vendido en esta línea |
| cantidad | integer | No | ≥ 1 | Unidades vendidas en esta línea |
| precio_unitario | numeric | No | > 0, en PEN | Precio aplicado en la transacción (puede diferir de `precio_lista` por campaña) |
| descuento_pct | numeric | No | 0.00 a 0.35 | Porcentaje de descuento aplicado (0 = sin descuento) |
| monto_total | numeric | No | > 0, en PEN | Campo derivado almacenado; ver fórmula oficial en sección 11.5 |
| canal | string | No | `Tienda` \| `Web` \| `App` | Denormalización de `tiendas.canal`; debe ser idéntico para cada `id_tienda` |
| metodo_pago | string | No | `Efectivo` \| `Tarjeta débito` \| `Tarjeta crédito` \| `Billetera digital` \| `Transferencia` | Medio de pago utilizado |

#### inventario.csv — PK compuesta: (`id_producto`, `id_tienda`, `periodo`)

| Campo | Tipo | Nulable | Dominio / regla | Descripción |
|---|---|---|---|---|
| id_producto | string | No | FK → `productos.id_producto` | Producto del snapshot |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Tienda del snapshot |
| periodo | string | No | Formato `AAAA-MM` | Mes al que corresponde el snapshot |
| stock_inicial | integer | No | ≥ 0 | Unidades disponibles al inicio del mes |
| unidades_vendidas | integer | No | ≥ 0 | Unidades salidas por ventas durante el mes |
| reabastecimiento | integer | No | ≥ 0 | Unidades ingresadas por reposición durante el mes |
| stock_final | integer | No | ≥ 0 | Derivado: `stock_inicial + reabastecimiento − unidades_vendidas` |
| costo_almacenamiento | numeric | No | ≥ 0, en PEN | Costo total mensual de almacenamiento de este producto en esta tienda. Cálculo: `stock_promedio × tasa_holding_mensual × costo_unitario`; la tasa es un parámetro de `config/` |

### 11.4 Relaciones entre tablas

```
ventas.id_cliente    → clientes.id_cliente
ventas.id_tienda     → tiendas.id_tienda
ventas.id_producto   → productos.id_producto
inventario.id_tienda → tiendas.id_tienda
inventario.id_producto → productos.id_producto
```

**Regla para geografía digital:** cuando `ventas.canal IN ('Web', 'App')`, la ciudad de la venta se obtiene mediante `ventas → clientes → clientes.ciudad`. No se usa `tiendas.ciudad`, que es `NULL` para los nodos digitales.

**Esquema estrella (Power BI):** `ventas` es la tabla de hechos principal; `tiendas`, `productos` y `clientes` son dimensiones; `inventario` es una tabla de hechos secundaria conectada por `id_producto` e `id_tienda`.

### 11.5 Fórmulas oficiales

```
# Nivel de línea (ventas.csv)
venta_bruta     = cantidad × precio_unitario
descuento_monto = venta_bruta × descuento_pct
monto_total     = venta_bruta − descuento_monto      ← campo almacenado en ventas.csv
costo_total     = cantidad × costo_unitario
margen_bruto    = monto_total − costo_total
margen_pct      = margen_bruto / monto_total

# Nivel de ticket (medida agregada, no campo almacenado)
ticket          = SUM(monto_total) agrupado por id_venta

# Nivel de inventario
stock_final     = stock_inicial + reabastecimiento − unidades_vendidas
```

**Notas:**

- `margen_pct` no tiene riesgo de división por cero: `monto_total > 0` está garantizado por las reglas de dominio (`cantidad ≥ 1`, `precio_unitario > 0`, `descuento_pct ≤ 0.35 < 1`). No es necesario agregar guarda `NULL`.
- `margen_bruto < 0` es válido: indica que el costo supera el precio neto. Este es el patrón inyectado artificialmente en Trujillo desde Q2 2025 y no debe tratarse como error en los scripts de validación.
- `precio_unitario` en `ventas` puede diferir de `productos.precio_lista` (por campañas o precios especiales). El descuento se aplica sobre `precio_unitario`, no sobre `precio_lista`.
- `ticket` es una medida de negocio, no un campo almacenado. Se calcula al vuelo con un `GROUP BY id_venta`.

### 11.6 Reglas de integridad

1. Ningún campo marcado como no nulable puede contener valores `NULL` o vacíos.
2. `ventas.fecha` debe estar dentro del rango `2023-01-01` a `2025-12-31`.
3. `ventas.cantidad ≥ 1`.
4. `ventas.precio_unitario > 0`, `productos.precio_lista > 0` y `productos.costo_unitario > 0`.
5. `ventas.descuento_pct ∈ [0.00, 0.35]`.
6. `ventas.monto_total = ventas.cantidad × ventas.precio_unitario × (1 − ventas.descuento_pct)` (el script de validación debe verificar esta igualdad con tolerancia de ± 0.01 PEN por redondeo).
7. `ventas.canal = tiendas.canal` para cada `id_tienda` referenciado (consistencia de la denormalización).
8. `inventario.stock_final = inventario.stock_inicial + inventario.reabastecimiento − inventario.unidades_vendidas`.
9. `inventario.stock_final ≥ 0`.
10. `productos.costo_unitario < productos.precio_lista`.
11. Todas las claves foráneas deben referenciar claves primarias existentes (sin registros huérfanos).

### 11.7 Trazabilidad campos ↔ partes del proyecto

| Campo o fórmula | P1 Estadístico | P2 Descriptivo | P3 Predictivo | P4 Prescriptivo | P5 Power BI |
|---|---|---|---|---|---|
| `ventas.monto_total`, `margen_bruto`, `margen_pct` | ✓ | ✓ | ✓ | — | ✓ |
| `ventas.canal`, `tiendas.canal` | ✓ | ✓ | ✓ | — | ✓ |
| `tiendas.ciudad`, `clientes.ciudad` | ✓ | ✓ | ✓ | — | ✓ |
| `productos.categoria` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ventas.metodo_pago` | ✓ | — | — | — | ✓ |
| `ventas.descuento_pct`, `descuento_monto` | ✓ | ✓ | — | — | ✓ |
| `ventas.fecha` (serie temporal) | — | ✓ | ✓ | — | ✓ |
| `ticket` (agregado por `id_venta`) | ✓ | ✓ | — | — | ✓ |
| `clientes.id_cliente`, `clientes.fecha_registro` | — | ✓ | ✓ (churn) | — | ✓ |
| `inventario.stock_*`, `reabastecimiento` | — | — | — | ✓ | ✓ |
| `inventario.costo_almacenamiento` | — | ✓ (diagnóstico) | — | ✓ | ✓ |

### 11.8 Aspectos pendientes de definir en tareas posteriores

Los siguientes elementos quedan fuera del alcance de esta tarea y se abordarán en F0-04 o en las secciones de cada parte:

- Volúmenes exactos de filas por tabla.
- Subcategorías por categoría de producto.
- Magnitud exacta de los picos de julio y diciembre.
- Evolución cuantitativa del canal digital a lo largo del periodo.
- Magnitud de la caída de margen en Trujillo y su codificación en `config/`.
- Rango de descuentos por categoría o canal.
- Definición temporal de "cliente inactivo" (umbral de días para churn).
- Granularidad y horizonte del pronóstico de demanda.
- Función objetivo y restricciones del modelo prescriptivo.
- Criterios automáticos de aceptación del dataset (script de validación).
- Archivos de salida de cada fase.
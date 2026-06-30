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

## 12. Parámetros de generación y escenarios controlados

Esta sección traduce la narrativa del caso AndinaRetail a parámetros numéricos concretos que el script generador de datos sintéticos consumirá. El archivo de referencia es `config/escenarios.yaml`; los valores aquí documentados y los valores en ese archivo deben mantenerse sincronizados.

Cada parámetro se describe con su nombre de clave YAML, tipo de dato, unidad, rango permitido, valor por defecto y justificación.

### 12.1 Reproducibilidad

El mismo código, semilla y archivo de configuración deben producir exactamente los mismos CSV en cualquier máquina. Las semillas se aplican a `numpy.random`, `random` de la biblioteca estándar y `Faker`.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `semilla` | int | — | [0, 2³²−1] | 2026 | Semilla global para todos los generadores de aleatoriedad |

### 12.2 Periodo

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `periodo.inicio` | date | AAAA-MM-DD | ≤ `periodo.fin` | 2023-01-01 | Primera fecha posible de registro de venta |
| `periodo.fin` | date | AAAA-MM-DD | ≥ `periodo.inicio` | 2025-12-31 | Última fecha posible de registro de venta |

### 12.3 Dominios

Los listados `ciudades`, `canales` y `categorias` son las enumeraciones autorizadas. Cualquier modificación debe reflejarse también en el contrato de datos (§11). No son parámetros de ajuste numérico sino referencias de valores permitidos para el generador.

### 12.4 Volúmenes y distribuciones

El volumen total de líneas en `ventas.csv` se deriva de los parámetros de clientes y frecuencia de compra, en lugar de especificarse como un número fijo. Esto permite ajustar el dataset sin romper la coherencia interna.

Estimado resultante: `15 000 clientes × 5 compras/año × 3 años × 2,5 líneas/ticket ≈ 281 000 líneas`.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `volumenes.tiendas_fisicas` | int | tiendas | [5, 50] | 15 | Total de tiendas físicas (canal=Tienda). Los nodos WEB y APP son siempre 2 filas adicionales en `tiendas.csv` y no se cuentan aquí |
| `volumenes.tiendas_por_ciudad.*` | int | tiendas | ≥ 1 | Lima:5, Arequipa:3, Trujillo:3, Cusco:2, Piura:2 | Distribución de las 15 tiendas físicas por ciudad; debe sumar `tiendas_fisicas` |
| `volumenes.productos` | int | SKUs | [100, 2000] | 500 | Total de productos en el catálogo |
| `volumenes.productos_por_categoria.*` | float | proporción | (0, 1) por valor; suma = 1.0 | ver YAML | Fracción del catálogo asignada a cada categoría |
| `volumenes.clientes` | int | clientes | [1000, 100 000] | 15 000 | Total de clientes registrados |
| `volumenes.compras_por_cliente_por_anio.media` | float | tickets/año | [1, 52] | 5.0 | Promedio de compras anuales por cliente activo |
| `volumenes.compras_por_cliente_por_anio.std` | float | tickets/año | [0, media] | 3.5 | Desviación estándar de la frecuencia de compra |
| `volumenes.compras_por_cliente_por_anio.min` | int | tickets/año | ≥ 1 | 1 | Mínimo garantizado de compras por cliente en todo el periodo |
| `volumenes.avg_lineas_por_ticket` | float | líneas/ticket | [1.0, 10.0] | 2.5 | Media de líneas de producto por compra |
| `volumenes.std_lineas_por_ticket` | float | líneas/ticket | [0, avg] | 1.5 | Desviación estándar de líneas por compra |

#### Distribución de ventas

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `distribucion_ventas.pesos_ciudad.*` | float | proporción | (0, 1); suma = 1.0 | Lima:0.40, Arequipa:0.20, Trujillo:0.18, Cusco:0.12, Piura:0.10 | Participación de cada ciudad en el volumen total de ventas. Lima domina por tamaño de mercado |
| `distribucion_ventas.pesos_categoria.*` | float | proporción | (0, 1); suma = 1.0 | Abarrotes:0.28, Bebidas:0.22, ... | Frecuencia relativa de venta por categoría. Abarrotes y Bebidas lideran por alta rotación |

### 12.5 Precios y márgenes base

El `margen_bruto_base_pct` es el parámetro más crítico del generador: determina `costo_unitario` para todos los productos y es la línea de base desde la cual se mide el deterioro de Trujillo.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `precios.margen_bruto_base_pct` | float | proporción | (0, 1) | 0.28 | Margen bruto normal de la empresa. `costo_unitario = precio_lista × (1 − 0.28)` |
| `precios.precio_lista_por_categoria.*.min` | float | PEN | > 0 | ver YAML | Precio mínimo de catálogo por categoría |
| `precios.precio_lista_por_categoria.*.max` | float | PEN | > min | ver YAML | Precio máximo de catálogo por categoría. Electrohogar tiene el rango más amplio (50–2 500 PEN) |

### 12.6 Descuentos

El descuento no es uniforme: el 40 % de las líneas no lleva descuento (compras al precio de lista), y el resto sigue una distribución normal truncada en [0, 0.35].

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `descuentos.media_pct` | float | proporción | [0, maximo_pct] | 0.08 | Descuento promedio sobre líneas con descuento > 0 |
| `descuentos.std_pct` | float | proporción | [0, media_pct] | 0.06 | Desviación estándar del descuento |
| `descuentos.maximo_pct` | float | proporción | (0, 1) | 0.35 | Techo absoluto — sincronizado con el contrato §11.3 |
| `descuentos.proporcion_sin_descuento` | float | proporción | [0, 1] | 0.40 | Fracción de líneas de venta donde `descuento_pct = 0` |

### 12.7 Estacionalidad

Los multiplicadores mensuales escalan el volumen base del mes. Un multiplicador de 1.20 en julio significa que julio genera un 20 % más de ventas que un mes con multiplicador 1.0. La suma de los 12 multiplicadores es aproximadamente 12.0, preservando así el volumen anual esperado.

El crecimiento interanual se aplica sobre el volumen base antes de la estacionalidad: el año 2024 genera un 7 % más de ventas que 2023, y 2025 un 7 % más que 2024.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `estacionalidad.multiplicadores_mensuales.*` | float | — | [0.5, 3.0] | ver YAML | Factor mensual de demanda. Suma ≈ 12.0 |
| `estacionalidad.crecimiento_anual_pct` | float | proporción | [0, 0.30] | 0.07 | Crecimiento interanual de demanda (7 %) |
| `estacionalidad.rangos_aceptacion.julio` | {min, max} | puntos % | — | [15, 25] | Rango de aceptación del pico de julio para el validador |
| `estacionalidad.rangos_aceptacion.diciembre` | {min, max} | puntos % | — | [30, 45] | Rango de aceptación del pico de diciembre para el validador |

### 12.8 Crecimiento del canal digital

La participación del canal digital (Web + App) sobre el total de ventas crece de forma gradual desde el 20 % en enero de 2023 hasta el 38 % en diciembre de 2025. Dentro de ese bloque digital, la App gana terreno frente a la Web a lo largo del periodo.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `canal_digital.participacion_inicial` | float | proporción | (0, 1) | 0.20 | Participación digital al inicio del periodo |
| `canal_digital.participacion_final` | float | proporción | (participacion_inicial, 1) | 0.38 | Participación digital al cierre del periodo |
| `canal_digital.curva` | string | — | `"lineal"` \| `"exponencial"` | `"lineal"` | Forma del crecimiento a lo largo del tiempo |
| `canal_digital.split_web_app_inicial` | float | proporción de digital | (0, 1) | 0.60 | Fracción Web dentro del total digital al inicio. App = 1 − valor |
| `canal_digital.split_web_app_final` | float | proporción de digital | (0, 1) | 0.45 | Fracción Web al cierre. La App pasa de 40 % a 55 % |

### 12.9 Escenario diagnóstico de Trujillo

A partir del 1 de abril de 2025 (inicio del Q2 2025), las ventas de Trujillo experimentan un deterioro artificial de margen generado por tres mecanismos causales simultáneos. El resultado esperado (caída de 6 a 9 puntos porcentuales en el margen bruto) es una consecuencia de estos parámetros y se verifica en el bloque de validación (§12.15), no aquí.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `trujillo.inicio_problema` | date | AAAA-MM-DD | dentro del periodo | 2025-04-01 | Fecha de inicio del deterioro |
| `trujillo.canales_afectados` | list[string] | — | subconjunto de `canales` | [Tienda, Web, App] | Canales afectados. Si el problema es solo físico, cambiar a [Tienda] |
| `trujillo.aumento_descuento_pp` | int | puntos porcentuales | [1, 20] | 6 | Incremento de `descuento_pct` promedio en Trujillo respecto al resto del país |
| `trujillo.aumento_costo_almacenamiento_pct` | int | % | [5, 100] | 30 | Incremento porcentual de `tasa_holding_mensual_pct` para inventario en Trujillo |
| `trujillo.desplazamiento_mix_menor_margen_pct` | int | % de ventas | [5, 50] | 15 | Porcentaje de ventas de Trujillo que se redirige hacia Abarrotes y Bebidas (categorías de menor margen) |

### 12.10 Relación descuento–demanda

El generador aplica una elasticidad precio-demanda simplificada: cuando el descuento sube, la cantidad vendida aumenta. El efecto no es determinístico; se añade ruido gaussiano para que la relación sea estadísticamente detectable pero no perfecta, lo que justifica el análisis en la Parte 1.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `relacion_descuento_demanda.aumento_descuento_pp_referencia` | int | puntos porcentuales | [1, 35] | 10 | Magnitud de referencia del descuento para la elasticidad |
| `relacion_descuento_demanda.aumento_demanda_pct_esperado.min` | int | % | ≥ 0 | 8 | Incremento mínimo esperado de cantidad por el aumento de referencia |
| `relacion_descuento_demanda.aumento_demanda_pct_esperado.max` | int | % | ≥ min | 12 | Incremento máximo esperado de cantidad por el aumento de referencia |
| `relacion_descuento_demanda.elasticidad_ruido_std_pct` | float | proporción | [0, 0.30] | 0.05 | Desviación estándar del ruido sobre el efecto de elasticidad |

### 12.11 Inventario

El `inventario.csv` registra snapshots mensuales por (producto, tienda). La cobertura objetivo define cuántos meses de demanda esperada se mantienen como stock. El costo de almacenamiento se calcula con la fórmula: `stock_promedio × tasa_holding_mensual_pct × costo_unitario`.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `inventario.tasa_holding_mensual_pct` | float | proporción/mes | (0, 0.10] | 0.02 | Fracción del costo unitario que representa el costo de almacenamiento mensual por unidad |
| `inventario.cobertura_stock_meses` | float | meses | [0.5, 6.0] | 2.0 | Meses de demanda proyectada que el stock inicial de cada mes debe cubrir |
| `inventario.std_cobertura` | float | meses | [0, cobertura] | 0.5 | Variación aleatoria alrededor del objetivo de cobertura |
| `inventario.reabastecimiento_frecuencia` | string | — | `"mensual"` | `"mensual"` | Frecuencia de reposición de stock |

### 12.12 Clientes

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `clientes.edad_min` | int | años | [18, edad_max) | 18 | Edad mínima del cliente al registrarse |
| `clientes.edad_max` | int | años | (edad_min, 100] | 80 | Edad máxima del cliente al registrarse |
| `clientes.distribucion_genero.*` | float | proporción | (0, 1); suma = 1.0 | M:0.48, F:0.48, No especificado:0.04 | Distribución del campo `genero` |
| `clientes.distribucion_ciudad.*` | float | proporción | (0, 1); suma = 1.0 | Lima:0.45, Arequipa:0.18, Trujillo:0.16, Cusco:0.11, Piura:0.10 | Ciudad de residencia del cliente. Ancla geográfica para ventas digitales |
| `clientes.fecha_registro_min` | date | AAAA-MM-DD | ≤ `periodo.inicio` | 2020-01-01 | Los clientes pueden haberse registrado hasta 3 años antes del inicio del periodo de ventas |

### 12.13 Churn

Un cliente se considera **inactivo** si no realizó ninguna compra en los últimos 90 días previos a `fecha_evaluacion`. La tasa objetivo de churn (25 %–35 %) se logra sesgando la distribución de frecuencias de compra para que una fracción significativa de clientes caiga naturalmente por debajo del umbral. Los pesos RFM guían la probabilidad de inactividad de cada cliente durante la generación.

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `churn.fecha_evaluacion` | date | AAAA-MM-DD | dentro del periodo | 2025-12-31 | Fecha de corte para clasificar clientes como activos o inactivos |
| `churn.ventana_inactividad_dias` | int | días | [30, 365] | 90 | Días sin compra que determinan la inactividad |
| `churn.proporcion_objetivo.min` | float | proporción | [0, max] | 0.25 | Límite inferior de la tasa de churn aceptable |
| `churn.proporcion_objetivo.max` | float | proporción | [min, 1] | 0.35 | Límite superior de la tasa de churn aceptable |
| `churn.pesos_rfm.recencia` | float | — | (0, 1); suma con los otros = 1.0 | 0.50 | Peso de la recencia en el score de riesgo de churn |
| `churn.pesos_rfm.frecuencia` | float | — | (0, 1) | 0.30 | Peso de la frecuencia de compra |
| `churn.pesos_rfm.valor` | float | — | (0, 1) | 0.20 | Peso del gasto histórico acumulado |

### 12.14 Calidad de datos

Los faltantes y los outliers se introducen de forma controlada para que el dataset refleje la calidad real de datos de producción sin comprometer la integridad analítica. El 2 % de faltantes aplica únicamente sobre los campos permitidos (ningún campo de `ventas.csv` admite nulos).

| Parámetro | Tipo | Unidad | Rango permitido | Valor por defecto | Descripción |
|---|---|---|---|---|---|
| `calidad_datos.faltantes.proporcion_objetivo` | float | proporción | [0.005, 0.10] | 0.020 | Proporción de valores nulos sobre el total de celdas en campos elegibles |
| `calidad_datos.faltantes.rango_aceptacion.min` | float | proporción | ≥ 0 | 0.010 | Límite inferior del validador |
| `calidad_datos.faltantes.rango_aceptacion.max` | float | proporción | ≤ 0.10 | 0.030 | Límite superior del validador |
| `calidad_datos.faltantes.campos_permitidos.clientes` | list[string] | — | campos nulables de clientes | [edad, distrito, canal_preferido] | Campos de `clientes.csv` donde se permiten nulos |
| `calidad_datos.faltantes.campos_permitidos.productos` | list[string] | — | campos nulables de productos | [subcategoria, marca] | Campos de `productos.csv` donde se permiten nulos |
| `calidad_datos.outliers.proporcion_objetivo` | float | proporción | [0.001, 0.02] | 0.005 | Proporción de líneas con valores extremos en `cantidad` o `monto_total` |
| `calidad_datos.outliers.magnitud_maxima_sigma` | float | σ | [2.0, 6.0] | 4.0 | Magnitud máxima de los outliers expresada en desviaciones estándar |

### 12.15 Criterios de aceptación del dataset

El script de validación usa este bloque para verificar automáticamente que el dataset generado cumple los patrones de negocio esperados. Estos son **resultados**, no entradas: si un criterio falla, debe ajustarse el parámetro causal correspondiente, no el rango de aceptación.

| Criterio | Parámetro causal asociado | Rango objetivo |
|---|---|---|
| Pico de julio (% sobre base) | `estacionalidad.multiplicadores_mensuales.7` | 15 % – 25 % |
| Pico de diciembre (% sobre base) | `estacionalidad.multiplicadores_mensuales.12` | 30 % – 45 % |
| Participación digital en 2023 | `canal_digital.participacion_inicial` | 18 % – 23 % |
| Participación digital en 2025 | `canal_digital.participacion_final` | 35 % – 42 % |
| Caída de margen en Trujillo (pp) | `trujillo.*` | 6 pp – 9 pp |
| Tasa de churn | `churn.*` | 25 % – 35 % |
| Proporción de faltantes | `calidad_datos.faltantes.*` | 1.0 % – 3.0 % |
| Proporción de outliers | `calidad_datos.outliers.*` | 0.3 % – 0.8 % |
# Diccionario de datos — AndinaRetail S.A.C.

## 1. Propósito y alcance

Este archivo es la **fuente canónica del esquema físico de datos** del proyecto. Define las tablas, campos, tipos, dominios, claves, relaciones, fórmulas derivadas y reglas de integridad que deberán respetar:

- el script generador de datos sintéticos;
- los scripts de validación;
- los notebooks de las Partes 1 a 4;
- el modelo de datos de Power BI.

Las decisiones de negocio y el alcance analítico general se documentan en [`docs/00_especificacion_datos_y_analitica.md`](../docs/00_especificacion_datos_y_analitica.md).

Los valores concretos de generación —volúmenes, distribuciones, probabilidades, magnitud de patrones, tolerancias y criterios de aceptación— se encuentran en [`config/escenarios.yaml`](../config/escenarios.yaml), que constituye la **fuente canónica de los parámetros numéricos** del proyecto.

En consecuencia:

- este diccionario es la fuente canónica del **esquema físico y sus reglas**;
- `config/escenarios.yaml` es la fuente canónica de los **valores numéricos de generación y validación**;
- el documento maestro explica el alcance y la interpretación funcional de ambos.

Toda modificación posterior del esquema debe actualizar este archivo y revisar su impacto en las fases posteriores.

---

## 2. Principios generales

- Todos los datos serán **100 % sintéticos** y se generarán con semillas fijas.
- Las tablas mínimas son `tiendas`, `productos`, `clientes`, `ventas` e `inventario`.
- Cada fila de `ventas` representa **una línea de producto dentro de una compra**.
- `id_venta` agrupa todas las líneas pertenecientes al mismo ticket; `id_linea` identifica cada línea de forma única.
- Los canales digitales se representan mediante dos nodos virtuales nacionales de venta y cumplimiento: `WEB` y `APP`.
- El dataset contendrá 15 nodos en total: 13 tiendas físicas, un nodo Web y un nodo App.
- Los nodos virtuales mantienen inventario propio dentro del modelo sintético.
- La ciudad comercial de una venta física se obtiene de la tienda; la de una venta digital se obtiene del cliente.
- La segmentación RFM no se almacena como dato fuente: se calcula en la Parte 2.
- Las fórmulas oficiales de este documento deben utilizarse de manera idéntica en Python y Power BI.
- Los valores faltantes y outliers controlados nunca podrán romper claves, relaciones, fórmulas financieras ni restricciones duras.

---

## 3. Resumen de tablas

| Tabla | Archivo | Clave primaria | Granularidad |
|---|---|---|---|
| tiendas | `tiendas.csv` | `id_tienda` | 1 fila por tienda física o nodo virtual |
| productos | `productos.csv` | `id_producto` | 1 fila por SKU |
| clientes | `clientes.csv` | `id_cliente` | 1 fila por cliente registrado |
| ventas | `ventas.csv` | `id_linea` | 1 fila por línea de producto dentro de una venta |
| inventario | `inventario.csv` | (`id_producto`, `id_tienda`, `periodo`) | 1 snapshot mensual por producto y nodo que mantiene stock |

---

## 4. Esquema de tablas

### 4.1 `tiendas.csv`

**PK:** `id_tienda`

| Campo | Tipo | Nulable | Dominio o regla | Descripción |
|---|---|---|---|---|
| id_tienda | string | No | Único; p. ej. `T001`, `WEB`, `APP` | Identificador del punto de venta o nodo virtual |
| nombre | string | No | Ficticio | Nombre de la tienda o nodo |
| tipo | string | No | `Fisica` \| `Virtual` | Tipo operativo exigido por el esquema del proyecto |
| canal | string | No | `Tienda` \| `Web` \| `App` | Canal atendido por el nodo |
| ciudad | string | Sí | `Lima` \| `Arequipa` \| `Trujillo` \| `Cusco` \| `Piura` \| `NULL` | Ciudad del nodo; puede ser `NULL` en nodos digitales de alcance nacional |
| region | string | Sí | `Costa` \| `Sierra` \| `NULL` | Región asociada al nodo; será `NULL` en los nodos digitales nacionales |
| area_m2 | numeric | Sí | `> 0` cuando `tipo = Fisica`; `NULL` cuando `tipo = Virtual` | Área del establecimiento físico |
| fecha_apertura | date | No | Fecha `<= 2025-12-31` | Fecha de apertura o activación del nodo |

**Mapeo oficial ciudad–región:**

| Ciudad | Región |
|---|---|
| Lima | Costa |
| Arequipa | Sierra |
| Trujillo | Costa |
| Cusco | Sierra |
| Piura | Costa |

**Reglas específicas:**

- Si `tipo = Fisica`, entonces `canal = Tienda`, `ciudad` no es nula y `area_m2 > 0`.
- Si `tipo = Virtual`, entonces `canal` es `Web` o `App` y `area_m2 = NULL`.
- Los nodos virtuales representan operaciones de venta y cumplimiento con inventario propio dentro del modelo sintético.
- Se generarán exactamente 13 tiendas físicas, distribuidas entre las cinco ciudades, y dos nodos virtuales nacionales.
- `id_tienda = WEB` identifica el nodo del canal Web.
- `id_tienda = APP` identifica el nodo del canal App.
- Los nodos `WEB` y `APP` mantienen inventario propio.

---

### 4.2 `productos.csv`

**PK:** `id_producto`

| Campo | Tipo | Nulable | Dominio o regla | Descripción |
|---|---|---|---|---|
| id_producto | string | No | Único; p. ej. `P0001` | Identificador del producto |
| nombre | string | No | Ficticio | Nombre comercial del producto |
| categoria | string | No | `Abarrotes` \| `Bebidas` \| `Limpieza` \| `Cuidado Personal` \| `Electrohogar` \| `Hogar` | Categoría principal |
| subcategoria | string | Sí | Lista controlada por categoría definida en `config/escenarios.yaml` | Subcategoría del producto |
| marca | string | Sí | Marca ficticia autorizada para la categoría en `config/escenarios.yaml` | Marca sintética |
| precio_lista | numeric | No | `> 0`, en PEN | Precio de referencia vigente del catálogo |
| costo_unitario | numeric | No | `> 0` y `< precio_lista`, en PEN | Costo de adquisición por unidad |
| fecha_alta | date | No | Fecha `<= 2025-12-31` | Fecha desde la cual el producto está disponible |

Las categorías, subcategorías y marcas permitidas se encuentran declaradas en `config/escenarios.yaml`. El generador no deberá crear valores fuera de esos catálogos sin actualizar primero ambos archivos.

**Regla de precios:** `precio_lista` es el precio de referencia del catálogo. No incluye el descuento aplicado a una transacción concreta.

---

### 4.3 `clientes.csv`

**PK:** `id_cliente`

| Campo | Tipo | Nulable | Dominio o regla | Descripción |
|---|---|---|---|---|
| id_cliente | string | No | Único; p. ej. `C00001` | Identificador del cliente |
| nombre | string | No | Ficticio, generado con Faker | Nombre completo sintético |
| edad | integer | Sí | 18 a 80 | Edad del cliente |
| genero | string | No | `M` \| `F` \| `No especificado` | Género sintético |
| ciudad | string | No | `Lima` \| `Arequipa` \| `Trujillo` \| `Cusco` \| `Piura` | Ciudad de residencia; ancla geográfica de las ventas digitales |
| distrito | string | Sí | Lista ficticia coherente con la ciudad | Distrito de residencia |
| fecha_registro | date | No | 2020-01-01 a 2025-12-31 | Fecha de incorporación del cliente |
| canal_preferido | string | Sí | `Tienda` \| `Web` \| `App` | Preferencia asignada sintéticamente al registrarse; no se deriva de ventas futuras |
| segmento | string | No | `Masivo` \| `Preferente` \| `Premium` | Segmento comercial inicial, independiente de la segmentación RFM |

> `segmento` no representa el resultado de RFM. Los segmentos RFM se derivarán exclusivamente del comportamiento observado en `ventas` durante la Parte 2.

---

### 4.4 `ventas.csv`

**PK:** `id_linea`
**Agrupador de ticket:** `id_venta`

| Campo | Tipo | Nulable | Dominio o regla | Descripción |
|---|---|---|---|---|
| id_linea | string | No | Único; p. ej. `L0000001` | Identificador de la línea de venta |
| id_venta | string | No | Puede repetirse entre líneas del mismo ticket | Identificador de la compra completa |
| fecha | date | No | 2023-01-01 a 2025-12-31 | Fecha de la transacción |
| id_cliente | string | No | FK → `clientes.id_cliente` | Cliente de la compra |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Nodo físico o virtual que procesó la venta |
| id_producto | string | No | FK → `productos.id_producto` | Producto vendido |
| cantidad | integer | No | `>= 1` | Unidades vendidas en la línea |
| precio_unitario | numeric | No | `> 0`, en PEN | Precio base vigente en la fecha de la operación, antes del descuento de la línea |
| descuento_pct | numeric | No | 0.00 a 0.35 | Descuento aplicado sobre `precio_unitario` |
| monto_total | numeric | No | `> 0`, en PEN | Venta neta de la línea, almacenada con dos decimales |
| canal | string | No | `Tienda` \| `Web` \| `App` | Canal de la transacción; debe coincidir con `tiendas.canal` |
| metodo_pago | string | No | `Efectivo` \| `Tarjeta debito` \| `Tarjeta credito` \| `Billetera digital` \| `Transferencia` | Medio de pago del ticket |

**Reglas de precio y promoción:**

- `precio_unitario` puede diferir de `precio_lista` por evolución histórica o ajustes de precio controlados.
- La promoción de la línea se representa exclusivamente mediante `descuento_pct`.
- No se debe reducir `precio_unitario` por una promoción y volver a aplicar el mismo descuento en `descuento_pct`.
- Todas las líneas con el mismo `id_venta` comparten `fecha`, `id_cliente`, `id_tienda`, `canal` y `metodo_pago`.

---

### 4.5 `inventario.csv`

**PK compuesta:** (`id_producto`, `id_tienda`, `periodo`)

| Campo | Tipo | Nulable | Dominio o regla | Descripción |
|---|---|---|---|---|
| id_producto | string | No | FK → `productos.id_producto` | Producto del snapshot |
| id_tienda | string | No | FK → `tiendas.id_tienda` | Nodo físico o virtual que mantiene el stock |
| periodo | string | No | Formato `AAAA-MM`; 2023-01 a 2025-12 | Mes del snapshot |
| stock_inicial | integer | No | `>= 0` | Unidades al inicio del mes |
| unidades_vendidas | integer | No | `>= 0` | Unidades vendidas durante el mes |
| reabastecimiento | integer | No | `>= 0` | Unidades ingresadas durante el mes |
| stock_final | integer | No | `>= 0` | Stock al cierre del mes |
| costo_almacenamiento | numeric | No | `>= 0`, en PEN | Costo total mensual de almacenamiento del producto en el nodo |

**Reglas específicas:**

- Cada nodo que procese ventas debe participar en `inventario.csv` cuando mantenga stock.
- Los nodos virtuales Web y App se consideran nodos de cumplimiento con inventario dentro del caso sintético.
- `unidades_vendidas` debe conciliar con la suma mensual de `ventas.cantidad` para la misma combinación producto–tienda.
- Para un mismo producto–tienda, el `stock_inicial` del mes siguiente debe ser igual al `stock_final` del mes anterior.

---

## 5. Relaciones

```text
ventas.id_cliente       -> clientes.id_cliente
ventas.id_tienda        -> tiendas.id_tienda
ventas.id_producto      -> productos.id_producto
inventario.id_tienda    -> tiendas.id_tienda
inventario.id_producto  -> productos.id_producto
```

### 5.1 Geografía de la venta

La dimensión derivada `ciudad_venta` se obtiene así:

```text
si ventas.canal = 'Tienda': ciudad_venta = tiendas.ciudad
si ventas.canal in ('Web', 'App'): ciudad_venta = clientes.ciudad
```

La caída de margen de Trujillo desde 2025-Q2 se analizará principalmente sobre las tiendas físicas ubicadas en Trujillo. Las ventas digitales pueden analizarse geográficamente por residencia del cliente, pero su costo de almacenamiento pertenece al nodo virtual nacional que las atiende.

### 5.2 Modelo analítico

- `ventas` es la tabla de hechos principal.
- `inventario` es una tabla de hechos secundaria.
- `tiendas`, `productos` y `clientes` funcionan como dimensiones compartidas.
- Power BI deberá incorporar además una tabla calendario derivada.

---

## 6. Fórmulas oficiales

### 6.1 Nivel de línea de venta

```text
venta_bruta          = cantidad * precio_unitario
descuento_monto      = venta_bruta * descuento_pct
monto_total          = venta_bruta - descuento_monto
costo_mercaderia     = cantidad * costo_unitario
margen_bruto         = monto_total - costo_mercaderia
margen_bruto_pct     = margen_bruto / monto_total
```

`monto_total` se almacena en `ventas.csv`. Las demás métricas se calculan en los notebooks y en Power BI usando estas mismas fórmulas.

### 6.2 Nivel de ticket

```text
ticket_total     = SUM(monto_total) agrupado por id_venta
ticket_promedio  = AVG(ticket_total)
```

### 6.3 Nivel de inventario

```text
stock_final       = stock_inicial + reabastecimiento - unidades_vendidas
stock_promedio    = (stock_inicial + stock_final) / 2
costo_almacenamiento = stock_promedio * tasa_holding_mensual * costo_unitario
```

La `tasa_holding_mensual` es un parámetro de `config/escenarios.yaml` y puede variar de forma controlada por ciudad y periodo.

### 6.4 Margen operativo por nodo y periodo

```text
ventas_netas_periodo    = SUM(monto_total)
margen_bruto_periodo    = SUM(margen_bruto)
margen_operativo        = margen_bruto_periodo - SUM(costo_almacenamiento)
margen_operativo_pct    = margen_operativo / ventas_netas_periodo
```

El patrón diagnóstico de Trujillo se evaluará principalmente mediante `margen_operativo_pct`, porque incorpora tanto el aumento del descuento como el aumento del costo de almacenamiento.

### 6.5 Notas de interpretación

- `monto_total > 0` está garantizado por `cantidad >= 1`, `precio_unitario > 0` y `descuento_pct < 1`.
- Un `margen_bruto < 0` puede existir en una proporción pequeña y controlada debido a descuentos extremos; no debe ser el mecanismo principal del patrón de Trujillo.
- La caída de Trujillo debe observarse como una reducción agregada del margen operativo, no como pérdidas generalizadas en todas sus líneas.
- El costo de almacenamiento no se asigna directamente a cada línea; se incorpora al margen operativo en el nivel producto–nodo–periodo.

### 6.6 Variables derivadas para la Parte 1

Las siguientes variables no se almacenan en los CSV. Se construyen de forma reproducible durante el analisis estadistico.

#### Grupo de canal

```text
grupo_canal =
    "Fisico"  si ventas.canal = "Tienda"
    "Digital" si ventas.canal in ("Web", "App")
```

Se utilizara para comparar el ticket entre operaciones fisicas y digitales.

#### Total del ticket

```text
ticket_total = SUM(ventas.monto_total) agrupado por ventas.id_venta
```

Cada `id_venta` constituye una unica observacion en los analisis realizados a nivel de ticket.

#### Categoria principal del ticket

```text
categoria_ticket =
categoria con el mayor SUM(monto_total) dentro de cada id_venta
```

Si dos o mas categorias presentan el mismo monto agregado, se seleccionara de forma deterministica la primera categoria segun orden alfabetico.

Esta variable se utilizara para analizar la asociacion entre categoria y metodo de pago sin duplicar un mismo ticket por cada linea de producto.

#### Periodo mensual

```text
periodo_mes = ventas.fecha expresada en formato AAAA-MM
```

Se utilizara para agregar ventas, margenes e inventario en una granularidad mensual.

#### Margen operativo por ciudad y mes

Para las tiendas fisicas:

```text
ventas_netas_ciudad_mes =
SUM(monto_total) por ciudad y periodo_mes

margen_bruto_ciudad_mes =
SUM(margen_bruto) por ciudad y periodo_mes

costo_almacenamiento_ciudad_mes =
SUM(costo_almacenamiento) por ciudad y periodo_mes

margen_operativo_ciudad_mes =
margen_bruto_ciudad_mes - costo_almacenamiento_ciudad_mes

margen_operativo_pct_ciudad_mes =
margen_operativo_ciudad_mes / ventas_netas_ciudad_mes
```

La agregacion debera incluir unicamente tiendas fisicas cuando se compare el margen entre ciudades, porque los nodos `WEB` y `APP` son nacionales y no pertenecen a una ciudad especifica.

---

### 6.7 Datasets derivados para la Parte 3
Los problemas predictivos no añadirán columnas a los CSV fuente. Sus unidades de análisis, objetivos y variables se construirán de manera reproducible mediante código.

#### Panel mensual de demanda
Cada observación representa una combinación de:
periodo_objetivo x id_tienda x categoria

La variable objetivo será:
demanda_unidades = SUM(ventas.cantidad) para el nodo, la categoría y el periodo objetivo

El panel incluirá todas las combinaciones activas de nodo, categoría y mes. Una combinación se considera activa cuando el nodo ya se encuentra operativo y existe al menos un producto de la categoría disponible en ese periodo. Si una combinación activa no registra ventas durante un mes, demanda_unidades será cero; la observación no se eliminará.

Para predecir el mes t, las variables históricas solo podrán utilizar información disponible hasta el final del mes t-1. Las variables de calendario del propio mes objetivo podrán utilizarse porque son conocidas anticipadamente.

Variables históricas candidatas:
demanda_lag_1
demanda_lag_2
demanda_lag_3
demanda_lag_6
demanda_lag_12
demanda_media_movil_3
demanda_media_movil_6
demanda_media_movil_12
demanda_desviacion_movil_3
tickets_lag_1
descuento_promedio_lag_1
precio_promedio_lag_1
proporcion_promocion_lag_1

Variables de calendario y tendencia:
anio
mes
trimestre
tendencia
mes_sin
mes_cos
es_julio
es_diciembre

No se utilizarán como predictores el descuento, precio, número de tickets o cantidad real del mes objetivo.

#### Dataset cliente-fecha de observación para churn
Cada observación representa:
id_cliente x fecha_observacion

Un cliente será elegible cuando:
clientes.fecha_registro <= fecha_observacion; y haya realizado al menos una compra hasta la fecha de observación.

El target será:
churn_90d = 1 si el cliente no realiza compras en (fecha_observacion, fecha_observacion + 90 días]
churn_90d = 0 si registra al menos una compra dentro de esa ventana

La ventana histórica principal será de 365 días anteriores al corte. La recencia se calculará desde la última compra histórica disponible hasta la fecha de observación, aunque esa compra sea anterior a la ventana de 365 días.

Variables candidatas:
recencia_dias
frecuencia_tickets_365d
valor_monetario_365d
ticket_promedio_365d
unidades_365d
meses_activos_365d
categorias_distintas_365d
categoria_dominante
proporcion_digital_365d
proporcion_web_365d
proporcion_app_365d
descuento_promedio_365d
dias_desde_penultima_compra
solo_una_compra
frecuencia_ultimos_90d
frecuencia_90d_previos
tendencia_frecuencia
antiguedad_cliente_dias

Cuando el cliente tenga una sola compra histórica, solo_una_compra = 1 y dias_desde_penultima_compra se representará como dato faltante para que el pipeline lo trate de forma reproducible.

También podrán utilizarse variables de perfil disponibles antes del corte:
edad
genero
ciudad
segmento
canal_preferido

No se utilizarán como predictores: id_cliente, nombre, información posterior al corte, el indicador descriptivo final calculado al 31 de diciembre de 2025, segmentos RFM calculados con información futura, o compras realizadas dentro de la ventana objetivo.

#### Diferencia entre churn descriptivo y predictivo
El indicador descriptivo final identifica clientes inactivos observando los 90 días anteriores al 31 de diciembre de 2025. El target predictivo utiliza cortes históricos y observa los 90 días posteriores a cada fecha de observación. Ambos conceptos emplean el mismo umbral temporal, pero cumplen propósitos diferentes.

#### Salidas derivadas de la Parte 3
Los resultados predictivos no forman parte de los CSV fuente. Se producirán en la carpeta resultados/ mediante los siguientes archivos:
predicciones_demanda.csv
predicciones_churn.csv
metricas_predictivas.csv
importancia_variables.csv

### 6.8 Dataset derivado para la Parte 4

La Parte 4 no añadirá columnas a los CSV fuente. El modelo prescriptivo construirá sus parámetros de forma reproducible a partir de los datos oficiales, la configuración y las salidas de la Parte 3.

#### Unidad de optimización

Cada observación del problema representa:

periodo × id_tienda × categoria

El periodo operativo será 2026-01. La recomendación será táctica por nodo y categoría; no se desagregará el pronóstico a producto en esta versión.

#### Demanda por escenario

La demanda se leerá desde resultados/predicciones_demanda.csv mediante los campos demanda_baja, demanda_predicha y demanda_alta.

Para cada escenario:

demanda_escenario = max(0, redondear al entero más cercano)

Después del redondeo deberá cumplirse:

demanda_baja <= demanda_predicha <= demanda_alta

#### Inventario inicial

stock_inicial_optimizacion[n,c] = SUM(inventario.stock_final)

Se utilizará inventario.periodo = "2025-12" y se agregará desde producto-nodo hacia nodo-categoría mediante productos.categoria.

#### Costo de adquisición unitario

costo_adquisicion_unitario[n,c]

Se calculará como el promedio ponderado de productos.costo_unitario, utilizando como peso las unidades vendidas durante 2025 en cada nodo-categoría.

Si una combinación no tiene ventas suficientes, se aplicarán en orden:

1. promedio ponderado de la categoría en todo el negocio;
2. promedio simple del catálogo de la categoría.

#### Costo unitario de demanda no atendida

costo_faltante_unitario[n,c] = SUM(monto_total) / SUM(cantidad)

Se utilizarán las ventas de 2025 del nodo y categoría. Si no existe información suficiente, se aplicarán en orden:

1. promedio de la categoría en todo el negocio;
2. promedio simple del precio neto estimado de la categoría.

#### Costo de almacenamiento unitario

costo_holding_unitario[n,c] = costo_adquisicion_unitario[n,c] × tasa_holding_mensual_nodo

La tasa será:

- 0.020 para los nodos no afectados;
- 0.026 para las tiendas físicas de Trujillo, correspondiente a 0.020 × 1.30.

#### Capacidad equivalente

Como el esquema no registra volumen físico por producto, se utilizarán unidades equivalentes de espacio:

- Abarrotes: 1.0
- Bebidas: 1.2
- Limpieza: 1.3
- Cuidado Personal: 0.8
- Electrohogar: 6.0
- Hogar: 3.0
Para cada nodo y mes:

stock_equivalente[n,m] = SUM(factor_espacio[c] × stock_categoria[n,c,m])

La capacidad base será:

capacidad_base[n] = 1.10 × MAX(stock_equivalente_inicial, stock_equivalente_final)

considerando todos los meses históricos disponibles.

#### Presupuesto base

necesidad_neta_central[n,c] = max(0, demanda_predicha[n,c] - stock_inicial_optimizacion[n,c])

presupuesto_referencia = SUM(costo_adquisicion_unitario[n,c] × necesidad_neta_central[n,c])

presupuesto_base = presupuesto_referencia

El monto se deriva del dataset y no se fija arbitrariamente antes de generar los datos.

#### Variables del modelo

q[n,c] = unidades de la categoría c que deben reponerse en el nodo n
u[n,c] = unidades de demanda no atendida
e[n,c] = inventario final estimado

Las tres variables serán enteras y no negativas.

#### Balance de inventario

e[n,c] = stock_inicial_optimizacion[n,c] + q[n,c] - demanda[n,c] + u[n,c]

con:

0 <= u[n,c] <= demanda[n,c]

#### Salidas derivadas de la Parte 4

Los resultados prescriptivos se producirán en resultados/:

recomendaciones_reposicion.csv
resumen_escenarios_optimizacion.csv
uso_capacidad_optimizacion.csv


## 7. Reglas de integridad y calidad

1. Las claves primarias deben ser únicas y no nulas.
2. No puede haber claves foráneas huérfanas.
3. Ningún campo marcado como no nulable puede contener `NULL` o cadenas vacías.
4. `ventas.fecha` debe pertenecer al periodo 2023-01-01 a 2025-12-31.
5. `ventas.fecha >= clientes.fecha_registro`.
6. `ventas.fecha >= productos.fecha_alta`.
7. `ventas.fecha >= tiendas.fecha_apertura`.
8. Todas las líneas de un mismo `id_venta` deben compartir fecha, cliente, tienda, canal y método de pago.
9. `ventas.cantidad >= 1`.
10. `ventas.precio_unitario > 0`, `productos.precio_lista > 0` y `productos.costo_unitario > 0`.
11. `productos.costo_unitario < productos.precio_lista`.
12. `ventas.descuento_pct` debe encontrarse entre 0.00 y 0.35.
13. `ventas.monto_total = cantidad * precio_unitario * (1 - descuento_pct)`, con tolerancia de ± 0.01 PEN.
14. `ventas.canal = tiendas.canal` para el `id_tienda` referenciado.
15. `inventario.stock_final = stock_inicial + reabastecimiento - unidades_vendidas`.
16. `inventario.stock_final >= 0`.
17. Para cada producto–tienda, `stock_inicial[t] = stock_final[t-1]`.
18. `inventario.unidades_vendidas` debe coincidir con la suma mensual de `ventas.cantidad` por producto–tienda.
19. Toda combinación producto–tienda–mes con ventas debe tener un registro correspondiente en `inventario.csv`.
20. Los valores faltantes controlados solo se introducirán en campos nulables y no se contarán junto con los nulos estructurales de nodos virtuales.
21. Los outliers no podrán violar claves, fechas, fórmulas, rangos duros ni integridad referencial.
22. Para el indicador descriptivo final, un cliente se considera inactivo si no realizó compras durante los 90 días anteriores al 2025-12-31. El denominador se limitará a clientes registrados antes del inicio de esa ventana y con al menos una compra histórica.
23. Para el modelo predictivo, churn_90d se calculará independientemente para cada fecha de observación y utilizará únicamente compras posteriores al corte para construir el target.
24. Ninguna variable predictora podrá contener información posterior a su fecha de observación o al inicio del periodo objetivo.
25. Las transformaciones, imputaciones, codificaciones y escalados se ajustarán únicamente con el conjunto de entrenamiento de cada partición.
26. id_cliente, nombre, id_venta e id_linea no se utilizarán como variables predictoras.
27. Todas las observaciones pertenecientes al mismo mes objetivo permanecerán juntas en las particiones temporales del modelo de demanda.
28. Toda fecha de observación de churn deberá tener su ventana futura completa dentro del periodo disponible del dataset.
29. Las combinaciones activas nodo-categoría sin ventas en un mes se conservarán con demanda_unidades = 0.
30. El pronóstico utilizado por la Parte 4 deberá corresponder a 2026-01.
31. Cada escenario deberá contener como máximo una observación por combinación id_tienda-categoria.
32. Las demandas baja, central y alta deberán ser no negativas y cumplir demanda_baja <= demanda_predicha <= demanda_alta.
33. El stock inicial de la optimización deberá conciliar con la suma del stock_final de diciembre de 2025 por nodo y categoría.
34. Los costos unitarios, capacidades y presupuestos deberán ser positivos y derivarse mediante las reglas aprobadas.
35. reposicion_optima, demanda_no_atendida y stock_final_estimado deberán ser enteros no negativos.
36. Cada solución deberá satisfacer la ecuación de balance de inventario.
37. El costo total de adquisición no podrá superar el presupuesto del escenario.
38. El inventario más la reposición no podrá superar la capacidad equivalente del nodo.
39. El nivel de servicio se calculará como fill rate en unidades y deberá cumplir el mínimo del escenario para cada nodo cuando la solución sea factible.
40. El estado del solver deberá registrarse explícitamente.
41. Los escenarios inviables no podrán convertirse en factibles relajando restricciones de forma silenciosa.
42. Los totales del detalle deberán conciliar con los archivos de resumen y utilización de capacidad.
43. Los resultados prescriptivos deberán generarse mediante código y no podrán editarse manualmente.

---

## 8. Trazabilidad hacia las partes del proyecto

| Campo o métrica | P1 Estadística | P2 Descriptivo | P3 Predictivo | P4 Prescriptivo | P5 Power BI |
|---|---:|---:|---:|---:|---:|
| `monto_total`, `ticket_total`, `ticket_promedio` | ✓ | ✓ | ✓ | — | ✓ |
| `margen_bruto`, `margen_bruto_pct` | ✓ | ✓ | — | — | ✓ |
| `margen_operativo`, `margen_operativo_pct` | ✓ | ✓ | — | ✓ | ✓ |
| `canal`, `tipo`, `ciudad_venta` | ✓ | ✓ | ✓ | — | ✓ |
| `categoria`, `subcategoria` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `metodo_pago` | ✓ | — | — | — | ✓ |
| `precio_unitario`, `descuento_pct`, `descuento_monto` | ✓ | ✓ | ✓ | — | ✓ |
| `fecha`, mes y variables temporales | ✓ | ✓ | ✓ | ✓ | ✓ |
| historial por `id_cliente` | — | ✓ | ✓ (churn) | — | ✓ |
| `segmento` comercial | ✓ | ✓ | ✓ | — | ✓ |
| `stock_inicial`, `stock_final`, `reabastecimiento` | — | — | — | ✓ | ✓ |
| `costo_almacenamiento` | ✓ | ✓ | — | ✓ | ✓ |
| demanda agregada por categoría y periodo | — | ✓ | ✓ | ✓ | ✓ |
| `cantidad`, `demanda_unidades`, rezagos y medias móviles | — | ✓ | ✓ (demanda) | ✓ | ✓ |
| recencia, frecuencia, valor y comportamiento histórico | — | ✓ | ✓ (churn) | — | ✓ |
| `demanda_predicha`, límites bajo y alto | — | — | ✓ | ✓ | ✓ |
| `probabilidad_churn`, `prediccion_churn` | — | — | ✓ | — | ✓ |
| stock de diciembre agregado por nodo y categoría | — | — | — | ✓ | ✓ |
| costo de adquisición e ingreso neto unitario | — | — | — | ✓ | ✓ |
| capacidad equivalente y presupuesto | — | — | — | ✓ | ✓ |
| reposicion_optima, demanda_atendida, faltante_estimado | — | — | — | ✓ | ✓ |
| stock_final_estimado, costo total y nivel de servicio | — | — | — | ✓ | ✓ |
| escenarios y utilización de capacidad | — | — | — | ✓ | ✓ |
---

## 9. Continuidad después de F0-07

F0-07 cerró los siguientes elementos de la Parte 4:

- periodo de optimización enero de 2026;
- granularidad nodo-categoría;
- decisión de no desagregar el pronóstico a producto;
- variable de decisión de reposición;
- variables auxiliares de demanda no atendida y stock final;
- función objetivo de costo total;
- restricciones de balance, presupuesto, capacidad y nivel de servicio;
- reglas para derivar demanda, stock, costos, presupuesto y capacidad;
- nivel de servicio base del 95 % por nodo;
- escenario base y escenarios de sensibilidad;
- política simple de referencia;
- archivos prescriptivos y salidas analíticas requeridas por fase;
- resultados que consumirá Power BI.

Las siguientes decisiones permanecen reservadas para tareas posteriores:

- reglas definitivas de segmentación RFM o clustering de la Parte 2;
- estructura final del modelo de datos de Power BI;
- medidas DAX;
- páginas, interactividad y storytelling del tablero.

Las fases posteriores deberán utilizar conjuntamente este diccionario, config/escenarios.yaml y docs/00_especificacion_datos_y_analitica.md. Ninguna fase deberá redefinir unilateralmente las granularidades, fórmulas, parámetros o salidas aprobadas.

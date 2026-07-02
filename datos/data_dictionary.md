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

---

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
22. Para la validación general del dataset, un cliente se considera inactivo si no realizó compras durante los 90 días anteriores al 2025-12-31.
23. F0-06 deberá definir por separado la ventana histórica de variables, la fecha de corte y el periodo objetivo utilizados para entrenar y evaluar el modelo predictivo, evitando fuga de información.

---

## 8. Trazabilidad hacia las partes del proyecto

| Campo o métrica | P1 Estadística | P2 Descriptivo | P3 Predictivo | P4 Prescriptivo | P5 Power BI |
|---|---:|---:|---:|---:|---:|
| `monto_total`, `ticket_total`, `ticket_promedio` | ✓ | ✓ | ✓ | — | ✓ |
| `margen_bruto`, `margen_bruto_pct` | ✓ | ✓ | — | — | ✓ |
| `margen_operativo`, `margen_operativo_pct` | — | ✓ | — | ✓ | ✓ |
| `canal`, `tipo`, `ciudad_venta` | ✓ | ✓ | ✓ | — | ✓ |
| `categoria`, `subcategoria` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `metodo_pago` | ✓ | — | — | — | ✓ |
| `precio_unitario`, `descuento_pct`, `descuento_monto` | ✓ | ✓ | ✓ | — | ✓ |
| `fecha`, mes y variables temporales | ✓ | ✓ | ✓ | ✓ | ✓ |
| historial por `id_cliente` | — | ✓ | ✓ (churn) | — | ✓ |
| `segmento` comercial | ✓ | ✓ | ✓ | — | ✓ |
| `stock_inicial`, `stock_final`, `reabastecimiento` | — | — | — | ✓ | ✓ |
| `costo_almacenamiento` | — | ✓ | — | ✓ | ✓ |
| demanda agregada por categoría y periodo | — | ✓ | ✓ | ✓ | ✓ |

---

## 9. Continuidad después de F0-04

F0-04 cerró en `config/escenarios.yaml` los siguientes elementos:

- cantidad y distribución de nodos físicos y virtuales;
- volúmenes objetivo de productos, clientes, tickets y líneas de venta;
- categorías, subcategorías y marcas ficticias;
- distribuciones de precios, costos, cantidades, canales y métodos de pago;
- magnitud de los picos de julio y diciembre;
- crecimiento del canal digital;
- causas y rango esperado de la caída del margen operativo de Trujillo;
- descuentos por canal;
- tasa de almacenamiento mensual;
- parámetros de clientes y segmentos comerciales;
- definición general de churn a 90 días;
- porcentajes y campos permitidos para faltantes y outliers;
- archivos CSV producidos por el generador;
- criterios automáticos de aceptación del dataset.

Las siguientes decisiones permanecen reservadas para las fases analíticas posteriores:

- hipótesis y pruebas estadísticas definitivas de la Parte 1;
- reglas de construcción e interpretación de la segmentación RFM o clustering;
- fecha de corte, ventana histórica y periodo objetivo del modelo de churn;
- granularidad y horizonte definitivos del pronóstico de demanda;
- variables predictoras, particiones temporales y métricas de los modelos;
- variables de decisión, función objetivo y restricciones del modelo prescriptivo;
- estructura final del modelo de Power BI y sus medidas DAX;
- archivos de salida analíticos específicos de cada parte.

Las tareas posteriores deberán utilizar conjuntamente:

1. este diccionario para conocer el esquema y las reglas de integridad;
2. `config/escenarios.yaml` para conocer los valores numéricos;
3. `docs/00_especificacion_datos_y_analitica.md` para conocer el alcance y la interpretación de negocio.

Ninguna fase deberá redefinir unilateralmente campos, fórmulas o parámetros sin actualizar los tres artefactos afectados.

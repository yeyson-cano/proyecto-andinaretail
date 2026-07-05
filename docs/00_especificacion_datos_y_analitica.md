# Especificación de datos y analítica — AndinaRetail S.A.C.

## 1. Propósito del documento

Este documento consolida las decisiones funcionales y analíticas que guiarán el Proyecto Grupal de Analítica de Datos. Su propósito es proporcionar una referencia común para los cinco integrantes y asegurar que la generación de datos sintéticos, los análisis estadísticos, los modelos descriptivos, predictivos y prescriptivos, y los tableros de Power BI formen parte de una única solución coherente.

El documento se amplía progresivamente durante la Fase 0. El detalle físico de tablas, campos, dominios, fórmulas y reglas de integridad se mantiene en [`datos/data_dictionary.md`](../datos/data_dictionary.md).

---

## 2. Descripción del caso

AndinaRetail S.A.C. es una empresa ficticia peruana del sector retail omnicanal. Opera tiendas físicas y canales digitales —Web y aplicación móvil— en Lima, Arequipa, Trujillo, Cusco y Piura.

La empresa comercializa productos de seis categorías:

- Abarrotes.
- Bebidas.
- Limpieza.
- Cuidado Personal.
- Electrohogar.
- Hogar.

AndinaRetail atiende a clientes minoristas y registra sus transacciones a nivel de línea de venta. Todos los datos del proyecto serán sintéticos; no se utilizará información real de personas o empresas.

---

## 3. Objetivo general

Diseñar y ejecutar una solución integral de analítica de datos para AndinaRetail S.A.C. que permita comprender el comportamiento de las ventas y los clientes, diagnosticar problemas de margen, anticipar la demanda y la inactividad de clientes, recomendar decisiones de inventario y comunicar los resultados mediante tableros gerenciales.

---

## 4. Alcance del proyecto

### 4.1 Alcance temporal

El conjunto principal de ventas representará operaciones realizadas entre el 1 de enero de 2023 y el 31 de diciembre de 2025.

Este periodo permitirá:

- analizar tres años completos;
- observar estacionalidad anual;
- comparar tendencias y cambios estructurales;
- construir problemas predictivos con separación temporal.

### 4.2 Alcance geográfico

El proyecto abarca:

- Lima;
- Arequipa;
- Trujillo;
- Cusco;
- Piura.

El problema diagnóstico principal se concentrará en las tiendas físicas de Trujillo desde el segundo trimestre de 2025.

### 4.3 Alcance comercial

Se analizarán:

- ventas y tickets;
- productos y categorías;
- clientes y comportamiento de compra;
- canales físicos y digitales;
- precios y descuentos;
- costos de mercadería y almacenamiento;
- margen bruto y margen operativo;
- inventario y reabastecimiento;
- inactividad de clientes;
- demanda futura.

### 4.4 Alcance analítico

El proyecto cubrirá cinco niveles complementarios:

1. Estadística descriptiva e inferencial para caracterizar el negocio y contrastar hipótesis.
2. Analítica descriptiva y diagnóstica para explicar tendencias, segmentos y causas.
3. Analítica predictiva para estimar demanda y riesgo de inactividad.
4. Analítica prescriptiva para recomendar decisiones de reposición de inventario.
5. Visualización ejecutiva en Power BI para comunicar resultados y apoyar decisiones.

---

## 5. Exclusiones del alcance

Quedan fuera del alcance:

- el uso de datos reales de personas o empresas;
- la integración con sistemas transaccionales reales;
- el desarrollo de una aplicación productiva o servicio en línea;
- la ejecución automática de decisiones comerciales reales;
- el análisis detallado de proveedores, recursos humanos o logística internacional;
- la optimización integral de todas las operaciones de la empresa;
- la optimización simultánea de inventario y políticas de descuento en esta primera versión;
- la incorporación de ciudades o categorías diferentes de las aprobadas sin una decisión formal del equipo.

Los descuentos seguirán siendo una variable explicativa y predictiva, pero el problema prescriptivo se concentrará en la reposición de inventario.

---

## 6. Preocupaciones estratégicas

La solución responderá a cuatro preocupaciones de la Gerencia General:

1. Comprender el comportamiento de ventas, tickets y clientes.
2. Explicar los patrones históricos y diagnosticar la caída de margen en Trujillo.
3. Anticipar la demanda y el riesgo de inactividad de los clientes.
4. Recomendar decisiones de inventario y comunicar los resultados mediante tableros ejecutivos.

---

## 7. Preguntas de negocio

### 7.1 Parte 1 — Técnicas estadísticas

**Pregunta principal:**

> ¿Cómo se distribuyen las ventas, los tickets y los clientes, y existen diferencias estadísticamente significativas entre canales, ciudades o categorías?

Preguntas complementarias:

- ¿El ticket promedio difiere entre el canal físico y los canales digitales?
- ¿El margen presenta diferencias significativas entre ciudades?
- ¿Existe asociación entre la categoría comprada y el método de pago?
- ¿Qué relación existe entre el descuento aplicado y la cantidad vendida?

### 7.2 Parte 2 — Analítica descriptiva y diagnóstica

**Pregunta principal:**

> ¿Qué patrones históricos, tendencias y factores explican el desempeño de AndinaRetail?

Preguntas complementarias:

- ¿Qué tendencias y estacionalidades presentan las ventas y los márgenes?
- ¿Qué productos, clientes y categorías concentran la mayor parte de los resultados?
- ¿Qué segmentos de clientes pueden identificarse mediante RFM o clustering?
- ¿Por qué cae el margen operativo de Trujillo desde el segundo trimestre de 2025?
- ¿Qué participación tienen los descuentos, la mezcla de productos y los costos de almacenamiento en esa caída?

### 7.3 Parte 3 — Modelos predictivos

**Preguntas principales:**

> ¿Qué demanda de unidades se espera por nodo, categoría y mes?

> ¿Qué clientes presentan mayor probabilidad de no comprar durante los siguientes 90 días?

El proyecto abordará:
 - regresión de demanda mensual por nodo y categoría, con horizonte de un mes; - clasificación de churn mediante observaciones cliente-fecha de corte y una ventana futura de 90 días.

El pronóstico operativo final corresponderá a enero de 2026 y servirá como insumo de la Parte 4.

El churn predictivo se diferenciará del indicador descriptivo calculado al cierre de 2025. Todas las variables
deberán utilizar exclusivamente información conocida antes del corte o del inicio del periodo objetivo.

### 7.4 Parte 4 — Modelo prescriptivo

**Pregunta principal:**

> ¿Cuánto inventario debería reponerse para atender la demanda esperada y controlar los costos operativos?

La optimización se concentrará en la reposición de inventario y considerará, como mínimo:

- demanda pronosticada;
- inventario disponible;
- presupuesto;
- capacidad de almacenamiento;
- costos de adquisición y almacenamiento;
- nivel de servicio.

La función objetivo, las variables de decisión y las restricciones se definirán en F0-07.

### 7.5 Parte 5 — Power BI

**Pregunta principal:**

> ¿Cómo integrar y monitorear los principales resultados del proyecto en tableros que faciliten la toma de decisiones gerenciales?

El tablero deberá permitir revisar:

- indicadores ejecutivos;
- ventas, ticket y márgenes;
- tendencias por ciudad, categoría, canal y tiempo;
- segmentos de clientes y riesgo de churn;
- pronósticos de demanda;
- recomendaciones de reposición y escenarios.

---

## 8. Relación entre preguntas y partes

| Parte | Propósito | Pregunta central | Resultado esperado |
|---|---|---|---|
| Parte 1 | Caracterizar y contrastar | ¿Existen diferencias relevantes entre grupos? | Estadísticos, pruebas e intervalos de confianza |
| Parte 2 | Explicar qué pasó y por qué | ¿Qué patrones y causas explican el desempeño? | Tendencias, Pareto, segmentos y diagnóstico del margen |
| Parte 3 | Anticipar | ¿Qué demanda habrá y qué clientes pueden quedar inactivos? | Pronósticos y probabilidades de churn |
| Parte 4 | Recomendar | ¿Cuánto inventario conviene reponer? | Plan de reposición y análisis de escenarios |
| Parte 5 | Comunicar | ¿Cómo monitorear los resultados para decidir? | Tableros ejecutivos de Power BI |

---

## 9. Decisiones aprobadas

- Se mantiene el caso AndinaRetail S.A.C.
- Se mantiene el sector retail omnicanal.
- Se consideran Lima, Arequipa, Trujillo, Cusco y Piura.
- Se mantienen las seis categorías oficiales.
- El periodo de ventas será 2023–2025.
- Trujillo será la ciudad principal del diagnóstico de margen desde 2025-Q2.
- Se desarrollará un modelo de demanda y un modelo de churn.
- El umbral de inactividad será de 90 días.
- El problema prescriptivo se concentrará en reposición de inventario.
- Los descuentos se utilizarán como variable explicativa y predictiva, pero no se optimizarán directamente en esta versión.
- Los resultados se integrarán en Power BI.
- Se utilizarán únicamente datos sintéticos y reproducibles.
- `config/escenarios.yaml` será la fuente canónica de los parámetros numéricos de generación y validación del dataset.
- El dataset incluirá 15 nodos de venta: 13 tiendas físicas, un nodo Web y un nodo App.
- Se generarán 800 productos, 15 000 clientes, aproximadamente 100 000 tickets y 250 000 líneas de venta.
- Los nodos Web y App mantendrán inventario propio y tendrán alcance nacional.
- El deterioro de margen de Trujillo afectará únicamente a sus tiendas físicas desde el 1 de abril de 2025.
- La caída de Trujillo se evaluará mediante el margen operativo porcentual, incorporando descuentos, mezcla de productos y costos de almacenamiento.
- Los criterios automáticos de aceptación del dataset se definirán y ejecutarán a partir de los rangos establecidos en `config/escenarios.yaml`.
- La demanda se pronosticará en unidades por mes, nodo de venta y categoría.
- El horizonte de demanda será de un mes.
- El pronóstico operativo final corresponderá a enero de 2026.
- La evaluación predictiva utilizará particiones temporales; no se permitirán particiones aleatorias de filas.
- El churn se construirá por cliente y fecha de observación.
- La ventana histórica principal de churn será de 365 días.
- La ventana objetivo de churn será de 90 días posteriores al corte.
- El conjunto de prueba final de churn utilizará el corte 2025-09-30.
- Los conjuntos de prueba permanecerán aislados hasta la evaluación final.
- No se decidirá anticipadamente qué modelo será el ganador.
- Los resultados predictivos se generarán como archivos derivados en la carpeta `resultados/`.

---

## 10. Aspectos reservados para tareas posteriores

F0-05 cerró la planificación estadística de la Parte 1 y F0-06 cierra la definición de los problemas predictivos
de la Parte 3.

Las siguientes decisiones permanecen reservadas para tareas posteriores:
 - reglas definitivas de construcción e interpretación de la segmentación RFM o clustering de la Parte 2; - variables de decisión, función objetivo y restricciones del modelo prescriptivo; - método de desagregación del pronóstico de categoría a producto, si F0-07 lo requiere; - estructura definitiva del modelo de datos, medidas DAX y páginas de Power BI; - archivos de salida analíticos específicos de las Partes 2, 4 y 5.

Las tareas posteriores deberán respetar las granularidades, targets, ventanas temporales y reglas contra fuga de
información aprobadas en esta especificación.

---

## 11. Contrato de datos

### 11.1 Fuente canónica

El detalle completo del esquema físico se encuentra en [`datos/data_dictionary.md`](../datos/data_dictionary.md). Ese archivo es la referencia oficial para:

- campos y tipos;
- dominios y nulabilidad;
- claves y relaciones;
- fórmulas derivadas;
- reglas de integridad;
- trazabilidad técnica hacia las cinco partes.

Esta sección resume únicamente las decisiones estructurales necesarias para relacionar el contrato con el alcance analítico.

### 11.2 Principios estructurales

- Las tablas oficiales son `tiendas`, `productos`, `clientes`, `ventas` e `inventario`.
- Cada fila de `ventas` es una línea de producto; `id_venta` agrupa las líneas de un ticket.
- Se añade `id_linea` como clave primaria de la tabla de ventas.
- `tiendas` incluye nodos físicos y virtuales, distinguidos mediante `tipo` y `canal`.
- `clientes.segmento` representa un segmento comercial inicial y no reemplaza la segmentación RFM.
- El inventario se registra mensualmente por producto y nodo que mantenga stock.
- La ciudad de una venta física proviene de la tienda; la de una venta digital, del cliente.
- Las métricas financieras se calculan con fórmulas únicas en Python y Power BI.

### 11.3 Tablas oficiales

| Tabla | Granularidad | Uso principal |
|---|---|---|
| `tiendas` | 1 fila por nodo físico o virtual | Ciudad, región, tipo y canal |
| `productos` | 1 fila por SKU | Categoría, precio y costo |
| `clientes` | 1 fila por cliente | Perfil, ciudad y comportamiento histórico |
| `ventas` | 1 fila por línea de producto | Hechos de venta, tickets, descuentos y demanda |
| `inventario` | 1 fila mensual por producto–nodo | Stock, reposición y costo de almacenamiento |

### 11.4 Métricas financieras oficiales

```text
venta_bruta          = cantidad * precio_unitario
descuento_monto      = venta_bruta * descuento_pct
monto_total          = venta_bruta - descuento_monto
costo_mercaderia     = cantidad * costo_unitario
margen_bruto         = monto_total - costo_mercaderia
margen_bruto_pct     = margen_bruto / monto_total
```

En el nivel nodo–periodo:

```text
margen_operativo     = SUM(margen_bruto) - SUM(costo_almacenamiento)
margen_operativo_pct = margen_operativo / SUM(monto_total)
```

El diagnóstico de Trujillo utilizará principalmente el margen operativo, porque debe reflejar simultáneamente el efecto de los descuentos y del almacenamiento.

### 11.5 Inventario y nodos digitales

- El proyecto utilizará 13 tiendas físicas y exactamente dos nodos virtuales nacionales: `WEB` y `APP`.
- Los nodos Web y App se modelan como nodos de cumplimiento con inventario propio.
- Las ventas físicas se relacionan con el inventario de la tienda donde se efectúa la transacción.
- Las ventas digitales se relacionan con el inventario del nodo Web o App que atiende la compra.
- La ciudad comercial de una venta digital se obtiene mediante `clientes.ciudad`; no se obtiene de `tiendas.ciudad`, que será nula para los nodos virtuales.
- El escenario de deterioro de Trujillo se aplicará únicamente a las tiendas físicas ubicadas en esa ciudad.
- Los costos de almacenamiento se atribuyen al nodo que mantiene el inventario, independientemente de la ciudad del cliente.
- La continuidad mensual exige que el stock final de un mes sea igual al stock inicial del mes siguiente para una misma combinación producto–nodo.
- Las unidades vendidas registradas en inventario deben conciliar con las ventas agregadas por producto, nodo y mes.
- El stock final nunca puede ser negativo.

### 11.6 Trazabilidad resumida

| Elemento | P1 | P2 | P3 | P4 | P5 |
|---|---:|---:|---:|---:|---:|
| Ventas, tickets y márgenes | ✓ | ✓ | ✓ | — | ✓ |
| Ciudad, canal y categoría | ✓ | ✓ | ✓ | ✓ | ✓ |
| Descuentos y precios | ✓ | ✓ | ✓ | — | ✓ |
| Historial por cliente | — | ✓ | ✓ | — | ✓ |
| Inventario y almacenamiento | — | ✓ | — | ✓ | ✓ |
| Demanda agregada | — | ✓ | ✓ | ✓ | ✓ |

### 11.7 Continuidad después de F0-04

F0-04 establece en `config/escenarios.yaml` los volúmenes, distribuciones, patrones controlados, tolerancias y criterios de aceptación del dataset.

El diccionario de datos continúa siendo la fuente canónica del esquema físico, mientras que el archivo YAML es la fuente canónica de los valores numéricos de generación.

Las tareas F0-05, F0-06 y F0-07 deberán utilizar ambos archivos sin redefinir unilateralmente sus campos, fórmulas o parámetros. Cualquier modificación posterior deberá evaluar su impacto sobre el generador, las validaciones, los notebooks y Power BI.

---

## 12. Parámetros de generación y escenarios controlados

### 12.1 Fuente canónica y propósito

Los parámetros numéricos utilizados por el generador de datos sintéticos se encuentran en [`config/escenarios.yaml`](../config/escenarios.yaml).

El archivo YAML es la **fuente canónica de los valores de generación y validación**. Esta sección proporciona su interpretación funcional y de negocio, pero no debe mantener copias independientes de todos los valores.

Ante cualquier diferencia entre esta sección y el archivo YAML, deberá revisarse la modificación más reciente y sincronizar ambos documentos antes de ejecutar nuevamente el generador.

### 12.2 Reproducibilidad

La generación utilizará la semilla global `2026`, aplicada de manera consistente a:

- `numpy.random`;
- `random`;
- `Faker`.

Se utilizará `Faker` con configuración regional `es_PE`, moneda PEN y zona horaria `America/Lima`.

La misma versión del código, el mismo archivo de configuración y la misma semilla deberán producir los mismos archivos CSV.

### 12.3 Periodo y volúmenes

El periodo de ventas comprenderá desde el 1 de enero de 2023 hasta el 31 de diciembre de 2025.

Los volúmenes aprobados son:

| Elemento | Valor |
|---|---:|
| Tiendas físicas | 13 |
| Nodos virtuales | 2 (`WEB` y `APP`) |
| Nodos totales | 15 |
| Productos | 800 |
| Clientes | 15 000 |
| Tickets objetivo | 100 000 |
| Líneas de venta objetivo | 250 000 |
| Tolerancia de líneas | ±2 % |

Las tiendas físicas se distribuirán de la siguiente forma:

| Ciudad | Tiendas |
|---|---:|
| Lima | 5 |
| Arequipa | 2 |
| Trujillo | 2 |
| Cusco | 2 |
| Piura | 2 |

Cada ticket tendrá una o más líneas de producto. El promedio objetivo será de 2.5 líneas por ticket, con un máximo ordinario de ocho líneas.

### 12.4 Productos y categorías

El catálogo contendrá 800 productos distribuidos entre las seis categorías oficiales.

| Categoría | Participación del catálogo |
|---|---:|
| Abarrotes | 25 % |
| Bebidas | 20 % |
| Limpieza | 15 % |
| Cuidado Personal | 15 % |
| Electrohogar | 15 % |
| Hogar | 10 % |

Las subcategorías y marcas ficticias autorizadas están declaradas en `config/escenarios.yaml`. El generador no deberá introducir categorías, subcategorías o marcas fuera de esos catálogos sin actualizar previamente la configuración y el contrato.

### 12.5 Precios, costos y margen base

Los rangos de precios y los márgenes base serán diferentes por categoría, evitando asumir que todos los productos tienen la misma rentabilidad.

| Categoría | Margen bruto base | Rango de precio de lista |
|---|---:|---:|
| Abarrotes | 18 % | S/ 2 – S/ 80 |
| Bebidas | 22 % | S/ 3 – S/ 60 |
| Limpieza | 30 % | S/ 5 – S/ 120 |
| Cuidado Personal | 35 % | S/ 8 – S/ 200 |
| Electrohogar | 28 % | S/ 50 – S/ 2 500 |
| Hogar | 32 % | S/ 10 – S/ 500 |

El costo unitario base se calculará mediante:

```text
costo_unitario = precio_lista * (1 - margen_bruto_base_categoria)
````

`precio_unitario` representará el precio vigente antes de aplicar el descuento de la línea. El descuento promocional se representará únicamente mediante `descuento_pct`, evitando aplicar dos veces la misma reducción de precio.

### 12.6 Descuentos

El descuento máximo permitido será de 35 %.

Las distribuciones variarán por canal:

| Canal  | Descuento promedio | Proporción sin descuento |
| ------ | -----------------: | -----------------------: |
| Tienda |                6 % |                     45 % |
| Web    |                9 % |                     30 % |
| App    |               10 % |                     25 % |

Las distribuciones deberán truncarse para impedir descuentos negativos o superiores al máximo aprobado.

### 12.7 Estacionalidad y crecimiento

El volumen mensual incorporará estacionalidad controlada.

Los principales picos serán:

* julio: multiplicador de 1.20;
* diciembre: multiplicador de 1.40.

El resto de los multiplicadores mensuales se encuentra en `config/escenarios.yaml` y se normalizará para conservar el volumen anual objetivo.

Se aplicará un crecimiento interanual de 7 % sobre el volumen base.

El dataset deberá cumplir los siguientes rangos de aceptación:

| Patrón                             | Rango esperado |
| ---------------------------------- | -------------: |
| Pico de julio sobre meses base     |    15 % – 25 % |
| Pico de diciembre sobre meses base |    30 % – 45 % |

### 12.8 Crecimiento del canal digital

La participación combinada de Web y App crecerá gradualmente durante el periodo:

```text
20 % al inicio de 2023
38 % al cierre de 2025
```

El crecimiento utilizará una curva lineal.

Dentro del canal digital:

* Web representará inicialmente 60 % del bloque digital;
* Web representará finalmente 45 %;
* App crecerá de 40 % a 55 % del bloque digital.

Los rangos de aceptación serán:

| Indicador                     |       Rango |
| ----------------------------- | ----------: |
| Participación digital en 2023 | 18 % – 23 % |
| Participación digital en 2025 | 35 % – 42 % |

### 12.9 Escenario diagnóstico de Trujillo

El deterioro de margen comenzará el 1 de abril de 2025 y afectará únicamente a las tiendas físicas de Trujillo.

El generador aplicará tres mecanismos causales:

1. incremento de seis puntos porcentuales en el descuento promedio;
2. incremento de 30 % en el costo de almacenamiento;
3. desplazamiento de 15 % de las ventas hacia Abarrotes y Bebidas, categorías de menor margen base.

El resultado no se forzará modificando directamente la métrica final. El generador aplicará las causas y el validador comprobará el resultado.

El criterio de aceptación será una caída de entre seis y nueve puntos porcentuales en:

```text
margen_operativo_pct
```

La comparación principal se realizará entre 2025-Q1 y 2025-Q2.

### 12.10 Relación entre descuento y demanda

La cantidad vendida deberá depender parcialmente del descuento aplicado.

Como referencia, un incremento de diez puntos porcentuales de descuento producirá un aumento esperado de entre 8 % y 12 % en la demanda, incorporando ruido aleatorio moderado.

La relación deberá ser detectable mediante análisis estadístico, pero no determinística ni perfectamente lineal.

### 12.11 Inventario

El inventario tendrá periodicidad mensual y se registrará por producto y nodo.

Parámetros principales:

| Parámetro                      |                  Valor |
| ------------------------------ | ---------------------: |
| Tasa de almacenamiento mensual | 2 % del costo unitario |
| Cobertura media de stock       |                2 meses |
| Nivel de servicio objetivo     |                   95 % |
| Frecuencia de reposición       |                Mensual |

Las fórmulas principales serán:

```text
stock_promedio = (stock_inicial + stock_final) / 2

costo_almacenamiento =
stock_promedio * tasa_holding_mensual * costo_unitario
```

El generador deberá preservar:

* continuidad mensual del inventario;
* conciliación con las ventas;
* stock final no negativo;
* inventario propio para los nodos Web y App.

### 12.12 Clientes

Las edades seguirán una distribución normal truncada con:

```text
media = 38
desviación estándar = 12
mínimo = 18
máximo = 80
```

La distribución comercial inicial será:

| Segmento   | Participación |
| ---------- | ------------: |
| Masivo     |          70 % |
| Preferente |          22 % |
| Premium    |           8 % |

Este segmento comercial no sustituye a la segmentación RFM de la Parte 2.

La distribución del canal preferido será:

| Canal  | Participación |
| ------ | ------------: |
| Tienda |          60 % |
| Web    |          23 % |
| App    |          17 % |

Las distribuciones de género, ciudad y métodos de pago por canal se encuentran declaradas en el archivo YAML.


### 12.13 Churn

El proyecto distingue dos conceptos relacionados, pero no equivalentes.

#### Indicador descriptivo final

Para la validación general y el tablero, un cliente será considerado inactivo si no realizó compras durante los 90
días anteriores al 31 de diciembre de 2025.

El denominador se limitará a clientes registrados antes del inicio de esa ventana y con al menos una compra
histórica.

La proporción objetivo del indicador descriptivo será de 25 % a 35 %.

#### Target predictivo prospectivo

Para cada fecha de observación histórica:

```text
churn_90d = 1
si el cliente no realiza compras durante los 90 días posteriores al corte

churn_90d = 0
si realiza al menos una compra durante esa ventana
```
Las variables predictoras se calcularán exclusivamente con información disponible hasta la fecha de observación.

#### Señal incorporada por el generador

El generador actualizará trimestralmente un score de riesgo conceptual basado en:

```text
score_riesgo =
0.50 * recencia_alta_normalizada
+ 0.30 * frecuencia_baja_normalizada
+ 0.20 * valor_bajo_normalizado
+ ruido
```

El score afectará de forma probabilística la posibilidad de compras futuras. Los clientes de riesgo alto tendrán
menor propensión futura de compra; los de riesgo bajo, mayor propensión. La relación conservará ruido para evitar
un target determinístico.

El score no se almacenará en `clientes.csv`, no se utilizará directamente como predictor y no garantizará una
métrica específica. El generador calibrará el nivel base para mantener el indicador descriptivo dentro del rango
aprobado.

### 12.14 Calidad de datos

El dataset incluirá faltantes y outliers controlados.

#### Valores faltantes

Se introducirá aproximadamente 2 % de valores faltantes sobre las celdas elegibles, con un rango aceptable entre 1 % y 3 %.

Los nulos solo podrán introducirse en:

* `clientes.edad`;
* `clientes.distrito`;
* `clientes.canal_preferido`;
* `productos.subcategoria`;
* `productos.marca`.

No podrán introducirse nulos en claves, campos derivados, ventas o inventario.

#### Outliers

El 0.5 % de las líneas de venta contendrá cantidades atípicas.

Las cantidades ordinarias estarán entre 1 y 8; las cantidades atípicas estarán entre 9 y 20.

Después de modificar `cantidad`, el generador deberá recalcular:

* `venta_bruta`;
* `descuento_monto`;
* `monto_total`;
* `costo_mercaderia`;
* márgenes derivados.

No se alterará `monto_total` de manera independiente, porque eso rompería las fórmulas oficiales.

### 12.15 Archivos de salida

El generador producirá en la carpeta `datos/`:

```text
tiendas.csv
productos.csv
clientes.csv
ventas.csv
inventario.csv
```

Los nombres y rutas se encuentran declarados en `config/escenarios.yaml`.

### 12.16 Criterios automáticos de aceptación

El script de validación deberá comprobar, como mínimo:

| Criterio                               | Resultado esperado |
| -------------------------------------- | -----------------: |
| Nodos totales                          |                 15 |
| Productos                              |                800 |
| Clientes                               |             15 000 |
| Líneas de ventas                       |  245 000 – 255 000 |
| Pico de julio                          |        15 % – 25 % |
| Pico de diciembre                      |        30 % – 45 % |
| Participación digital 2023             |        18 % – 23 % |
| Participación digital 2025             |        35 % – 42 % |
| Caída del margen operativo de Trujillo |        6 pp – 9 pp |
| Tasa de churn                          |        25 % – 35 % |
| Valores faltantes elegibles            |          1 % – 3 % |
| Líneas con cantidad mayor que ocho     |      0.3 % – 0.8 % |

También deberá verificar:

* ausencia de claves primarias duplicadas;
* ausencia de claves foráneas huérfanas;
* coherencia temporal de clientes, productos, tiendas y ventas;
* cumplimiento de las fórmulas monetarias con tolerancia de S/ 0.01;
* continuidad mensual del inventario;
* conciliación entre ventas e inventario;
* ausencia de stock final negativo.

---

### 12.17 Aptitud predictiva del dataset

El script de validación deberá comprobar que el dataset pueda sostener los dos problemas predictivos sin forzar el
resultado de los modelos.

Para demanda deberá verificarse:
 - existencia del panel mensual por nodo y categoría; - conservación de combinaciones activas con cero ventas; - al menos 24 meses objetivo evaluables; - representación de los 15 nodos y las seis categorías; - variación temporal distinta de cero; - disponibilidad de los rezagos definidos; - separación correcta entre información histórica y mes objetivo.

Para churn deberá verificarse:
 - construcción de todas las fechas de observación aprobadas; - ventana futura completa de 90 días para cada corte; - presencia de ambas clases en cada fecha de observación; - al menos 100 observaciones por clase y corte; - tasa positiva entre 15 % y 60 % por corte; - relación imperfecta entre comportamiento RFM histórico y churn futuro; - ausencia de información posterior al corte en las variables.

Estas validaciones determinan que los problemas puedan construirse y evaluarse. No se fijará una métrica mínima,
no se regenerarán datos únicamente para mejorar resultados y no se predeterminará qué modelo debe ganar.

## 13. Hipotesis estadisticas y variables requeridas

### 13.1 Objetivo y alcance

Esta seccion define la planificacion estadistica de la Parte 1 del proyecto. Su proposito es garantizar que el dataset sintetico permita:

- caracterizar las ventas, los tickets y los clientes;
- calcular medidas descriptivas e intervalos de confianza;
- formular y contrastar hipotesis reproducibles;
- comparar canales y ciudades;
- analizar asociaciones entre variables categoricas;
- evaluar relaciones entre variables numericas;
- interpretar los resultados en terminos del negocio.

Las hipotesis se formulan antes de observar los CSV definitivos. El generador debera proporcionar variables, variacion y representacion suficientes para ejecutar las pruebas, pero no debera modificarse repetidamente hasta obtener resultados estadisticamente significativos.

Los patrones obligatorios del caso -como la caida del margen operativo de Trujillo y la relacion controlada entre descuento y demanda- se validaran como propiedades del dataset. Las demas hipotesis conservaran un caracter inferencial y podran concluir a favor o en contra de la hipotesis nula.

### 13.2 Convenciones estadisticas generales

La Parte 1 utilizara las siguientes convenciones:

| Elemento | Decision |
|---|---|
| Nivel de significancia nominal | `alpha = 0.05` |
| Nivel de confianza | 95 % |
| Tipo de contraste | Bilateral, salvo justificacion documentada |
| Correccion por comparaciones multiples | Metodo de Holm |
| Redondeo monetario | Dos decimales |
| Semilla de procedimientos remuestreados | 2026 |
| Numero recomendado de remuestras bootstrap | 5 000 |
| Unidad de analisis | Se definira por cada hipotesis |
| Criterio de decision | Valor p ajustado, intervalo de confianza y tamano del efecto |

Para las cuatro hipotesis principales se reportaran:

- estadistico de prueba;
- valor p original;
- valor p ajustado mediante Holm;
- intervalo de confianza;
- tamano del efecto;
- interpretacion estadistica;
- interpretacion de negocio.

Debido al volumen aproximado de 100 000 tickets y 250 000 lineas de venta, un valor p pequeno no sera considerado suficiente para afirmar que una diferencia es relevante. Toda conclusion debera considerar tambien la magnitud del efecto y su importancia practica.

### 13.3 Preparacion de los niveles de analisis

El notebook estadistico construira cuatro vistas derivadas sin modificar los CSV originales.

#### Vista a nivel de linea

Cada observacion corresponde a una fila de `ventas.csv`.

Se utilizara para:

- distribucion de cantidades;
- distribucion de montos por linea;
- distribucion de descuentos;
- correlacion entre descuento y cantidad;
- analisis de precios y margenes brutos.

#### Vista a nivel de ticket

Cada observacion corresponde a un unico `id_venta`.

```text
ticket_total =
SUM(monto_total) agrupado por id_venta
```

Las variables constantes dentro del ticket seran:

- fecha;
- cliente;
- nodo de venta;
- canal;
- metodo de pago.

Se derivara:

```text
grupo_canal =
    "Fisico"  si canal = "Tienda"
    "Digital" si canal in ("Web", "App")
```

#### Vista a nivel de cliente

Cada observacion corresponde a un unico `id_cliente`.

Se utilizara para:

- distribucion de edad;
- distribucion de genero;
- distribucion de ciudad;
- distribucion del segmento comercial;
- frecuencia descriptiva de clientes por canal preferido.

Esta vista no incluira todavia los segmentos RFM, que corresponden a la Parte 2.

#### Vista a nivel de ciudad-mes

Cada observacion correspondera a una combinacion de ciudad fisica y mes.

Solo se incluiran tiendas con:

```text
tipo = "Fisica"
```

Las metricas seran:

```text
ventas_netas_ciudad_mes =
SUM(monto_total)

margen_bruto_ciudad_mes =
SUM(margen_bruto)

costo_almacenamiento_ciudad_mes =
SUM(costo_almacenamiento)

margen_operativo_ciudad_mes =
margen_bruto_ciudad_mes - costo_almacenamiento_ciudad_mes

margen_operativo_pct_ciudad_mes =
margen_operativo_ciudad_mes / ventas_netas_ciudad_mes
```

Esta vista permitira comparar las ciudades sin asignar artificialmente los costos de los nodos nacionales `WEB` y `APP` a una ciudad concreta.

### 13.4 Plan de estadistica descriptiva

La Parte 1 calculara, como minimo, las siguientes medidas.

| Variable | Nivel | Medidas principales |
|---|---|---|
| `monto_total` | Linea | Media, mediana, desviacion estandar, IQR, asimetria y curtosis |
| `ticket_total` | Ticket | Media, mediana, moda cuando sea interpretable, desviacion estandar, IQR y percentiles |
| `cantidad` | Linea | Media, mediana, moda, frecuencias, dispersion, asimetria y curtosis |
| `edad` | Cliente | Media, mediana, moda, desviacion estandar, IQR y distribucion |
| `descuento_pct` | Linea | Media, mediana, percentiles y proporcion sin descuento |
| `margen_bruto_pct` | Linea | Media, mediana, dispersion y valores extremos |
| `margen_operativo_pct` | Ciudad-mes | Media, mediana y dispersion por ciudad |
| `canal` | Ticket | Frecuencias absolutas y relativas |
| `categoria` | Linea | Frecuencias absolutas y relativas |
| `metodo_pago` | Ticket | Frecuencias absolutas y relativas |

Las visualizaciones minimas seran:

- histogramas de `monto_total`, `ticket_total`, `edad` y `cantidad`;
- boxplots de ticket por grupo de canal;
- boxplots de margen operativo por ciudad;
- grafico de dispersion o jitter de descuento frente a cantidad;
- tabla o mapa de calor de categoria del ticket frente a metodo de pago;
- barras de frecuencias para canal, ciudad, categoria y metodo de pago;
- intervalos de confianza de las metricas principales por grupo;
- matriz descriptiva de correlaciones numericas.

### 13.5 Hipotesis H1 - Ticket fisico frente a digital

#### Pregunta

¿El valor promedio de los tickets difiere entre las compras realizadas en tiendas fisicas y las compras realizadas mediante canales digitales?

#### Unidad de analisis

Un ticket identificado por `id_venta`.

No se utilizaran lineas individuales como observaciones independientes.

#### Variables

| Rol | Variable |
|---|---|
| Variable cuantitativa | `ticket_total` |
| Variable de agrupacion | `grupo_canal` |
| Grupo 1 | `Fisico` |
| Grupo 2 | `Digital` |

#### Formulacion

```text
H0: media_ticket_fisico = media_ticket_digital

H1: media_ticket_fisico != media_ticket_digital
```

#### Prueba principal

Prueba t de Welch para muestras independientes.

Se utilizara Welch porque no requiere igualdad de varianzas entre los dos grupos.

#### Alternativa robusta

Prueba U de Mann-Whitney si:

- existen distribuciones extremadamente asimetricas;
- los valores extremos dominan las medias;
- los diagnosticos desaconsejan una comparacion parametrica.

#### Supuestos y diagnosticos

Se revisara:

- independencia aproximada entre tickets;
- forma de las distribuciones;
- graficos Q-Q;
- asimetria;
- valores extremos;
- varianzas mediante Levene o Brown-Forsythe.

La normalidad no se decidira unicamente mediante una prueba de Shapiro-Wilk, porque con muestras grandes puede rechazar desviaciones pequenas sin importancia practica.

#### Tamano del efecto

Se reportara Hedges `g`.

#### Intervalos de confianza

Se calcularan:

- IC 95 % del ticket promedio fisico;
- IC 95 % del ticket promedio digital;
- IC 95 % de la diferencia entre medias.

Cuando la distribucion sea muy asimetrica, se utilizara ademas un intervalo bootstrap reproducible.

#### Analisis de sensibilidad

Como comprobacion adicional, podra repetirse la comparacion utilizando el ticket promedio por cliente y grupo de canal, reduciendo la influencia de clientes con un numero muy alto de compras.

#### Interpretacion

La prueba determinara si existe evidencia de una diferencia, pero no se fijara anticipadamente cual canal debe presentar el mayor ticket.

### 13.6 Hipotesis H2 - Margen operativo entre ciudades

#### Pregunta

¿Existen diferencias en el margen operativo porcentual de las tiendas fisicas entre Lima, Arequipa, Trujillo, Cusco y Piura durante el periodo afectado por el escenario diagnostico?

#### Periodo principal

```text
2025-04-01 a 2025-12-31
```

Este periodo corresponde al inicio y desarrollo del deterioro controlado de las tiendas fisicas de Trujillo.

#### Unidad de analisis

Una combinacion ciudad-mes.

La metrica sera:

```text
margen_operativo_pct_ciudad_mes
```

La comparacion tendra cinco ciudades observadas durante nueve meses.

#### Formulacion

```text
H0:
media_Lima = media_Arequipa = media_Trujillo = media_Cusco = media_Piura

H1:
al menos una ciudad presenta un margen operativo porcentual diferente
```

#### Modelo principal

Se utilizara un diseno por bloques mediante un modelo lineal aditivo:

```text
margen_operativo_pct ~ ciudad + mes
```

- `ciudad` sera el factor principal.
- `mes` funcionara como bloque para controlar variaciones mensuales comunes.
- Se evaluara el efecto de ciudad mediante ANOVA de tipo II.

No se utilizaran lineas de venta individuales como observaciones del ANOVA, porque el costo de almacenamiento se encuentra en una granularidad mensual.

#### Diagnosticos

Se revisara:

- normalidad aproximada de los residuos;
- grafico Q-Q;
- homogeneidad de la dispersion;
- observaciones influyentes;
- coherencia temporal de las metricas.

#### Alternativa no parametrica

Si los supuestos del modelo no son razonables, se utilizara la prueba de Friedman:

- ciudades como tratamientos;
- meses como bloques.

#### Comparaciones posteriores

Si el contraste global resulta relevante, se realizaran comparaciones emparejadas por mes entre ciudades, aplicando correccion de Holm.

El contraste de mayor interes sera:

```text
Trujillo frente a las demas ciudades
```

#### Tamano del efecto

Se reportara:

- eta cuadrado parcial para el efecto global de ciudad;
- diferencia media mensual entre Trujillo y cada ciudad;
- tamano del efecto estandarizado para las comparaciones posteriores.

#### Intervalos de confianza

Se calculara el IC 95 % del margen operativo promedio de cada ciudad y de las diferencias mensuales relevantes.

#### Interpretacion

El generador si debera producir la caida de margen operativo de Trujillo definida en `config/escenarios.yaml`, pero no se fijara previamente el valor exacto del estadistico ni del valor p.

### 13.7 Hipotesis H3 - Categoria principal del ticket y metodo de pago

#### Pregunta

¿Existe asociacion entre la categoria principal de una compra y el metodo de pago utilizado?

#### Unidad de analisis

Un ticket identificado por `id_venta`.

El metodo de pago pertenece al ticket, mientras que la categoria pertenece a cada linea. Para evitar contar varias veces la misma compra, se derivara:

```text
categoria_ticket =
categoria con el mayor SUM(monto_total) dentro de cada id_venta
```

Si dos categorias tienen exactamente el mismo monto agregado, se seleccionara de forma deterministica la primera segun orden alfabetico.

#### Variables

| Rol | Variable |
|---|---|
| Variable categorica 1 | `categoria_ticket` |
| Variable categorica 2 | `metodo_pago` |

#### Formulacion

```text
H0:
categoria_ticket y metodo_pago son estadisticamente independientes

H1:
existe asociacion entre categoria_ticket y metodo_pago
```

#### Prueba principal

Prueba chi-cuadrado de independencia.

#### Supuestos

Se verificara que:

- cada ticket aparezca una sola vez;
- las categorias sean mutuamente excluyentes;
- ninguna frecuencia esperada sea menor que uno;
- como maximo el 20 % de las celdas tenga frecuencia esperada menor que cinco.

Si las condiciones no se cumplen, se evaluara:

- agrupar categorias escasas;
- utilizar una estimacion Monte Carlo del valor p;
- analizar tablas estratificadas por canal.

#### Tamano del efecto

Se reportara `V` de Cramer.

#### Analisis posterior

Se examinaran residuos estandarizados ajustados para identificar que combinaciones contribuyen mas a la asociacion global.

Los analisis por celda utilizaran correccion por comparaciones multiples.

#### Analisis de sensibilidad

Debido a que los metodos de pago tienen distribuciones diferentes por canal, se presentaran tambien tablas descriptivas separadas para:

- Tienda;
- Web;
- App.

Esto permitira detectar si una asociacion global esta explicada principalmente por el canal.

#### Interpretacion

El dataset debera garantizar representacion suficiente de categorias y metodos de pago, pero no se forzara una asociacion significativa entre ambas variables.

### 13.8 Hipotesis H4 - Descuento y cantidad vendida

#### Pregunta

¿Existe una relacion monotonica entre el porcentaje de descuento y la cantidad vendida por linea?

#### Unidad de analisis

Una linea de `ventas.csv`.

#### Variables

| Rol | Variable |
|---|---|
| Variable 1 | `descuento_pct` |
| Variable 2 | `cantidad` |

#### Formulacion

```text
H0:
rho(descuento_pct, cantidad) = 0

H1:
rho(descuento_pct, cantidad) != 0
```

#### Prueba principal

Correlacion de Spearman.

Se selecciona Spearman porque:

- `cantidad` es discreta;
- su distribucion esta concentrada en valores bajos;
- existen cantidades atipicas controladas;
- no se asume una relacion lineal perfecta;
- la relacion esperada es monotonica con ruido.

#### Diagnosticos

Se revisara:

- grafico de dispersion con jitter;
- tendencia monotonica;
- presencia de valores extremos;
- resultados generales y por canal;
- resultados generales y por categoria.

#### Tamano del efecto

El propio coeficiente `rho` de Spearman sera la medida del efecto.

#### Intervalo de confianza

Se calculara un IC 95 % mediante bootstrap con semilla 2026.

#### Analisis de sensibilidad

La correlacion se calculara:

1. con todas las lineas validas;
2. excluyendo temporalmente las lineas con `cantidad > 8`;
3. separada por canal;
4. separada por categoria cuando exista representacion suficiente.

Los outliers no se eliminaran del dataset original. La comparacion servira unicamente para evaluar cuanto influyen en el resultado.

#### Interpretacion

El generador incorpora una relacion controlada entre descuento y demanda, por lo que se espera una senal positiva detectable, pero no una correlacion perfecta ni un valor p predeterminado.

### 13.9 Intervalos de confianza adicionales

Ademas de los intervalos vinculados a las hipotesis, se calcularan IC 95 % para indicadores relevantes como:

- ticket promedio general;
- ticket promedio por canal;
- venta media por linea;
- edad promedio de clientes;
- descuento promedio por canal;
- margen bruto promedio;
- margen operativo promedio por ciudad;
- proporcion de tickets digitales;
- proporcion de clientes por segmento comercial.

Para medias con distribuciones fuertemente asimetricas se preferiran intervalos bootstrap.

Para proporciones se utilizara un metodo apropiado, como Wilson, evitando depender exclusivamente de la aproximacion normal cuando la frecuencia sea baja.

### 13.10 Tratamiento de faltantes y valores atipicos

#### Valores faltantes

Antes del analisis se reportara:

- cantidad de nulos por campo;
- porcentaje de nulos por campo;
- patron de faltantes por tabla;
- diferencia entre nulos estructurales y faltantes introducidos artificialmente.

Las variables principales de las cuatro hipotesis son no nulables. Por tanto, no se preve imputacion para los contrastes principales.

Para `clientes.edad` se utilizaran observaciones disponibles y se informara el numero de casos excluidos. No se imputara edad unicamente para mejorar el resultado de una prueba.

#### Valores atipicos

Los valores atipicos controlados forman parte del diseno del dataset y no seran eliminados automaticamente.

Se realizara:

- identificacion mediante reglas del YAML;
- comparacion de estadisticas con y sin outliers;
- uso de medidas robustas como mediana e IQR;
- analisis de sensibilidad cuando puedan afectar una conclusion.

Cualquier exclusion debera quedar explicitamente justificada y no modificara los CSV originales.

### 13.11 Criterios de aptitud estadistica del dataset

Antes de ejecutar las pruebas se verificara que:

1. existan tickets fisicos y digitales suficientes para realizar H1;
2. cada `id_venta` mantenga fecha, cliente, nodo, canal y metodo de pago constantes;
3. las cinco ciudades tengan observaciones mensuales durante el periodo de H2;
4. ventas e inventario puedan conciliarse para calcular el margen operativo;
5. las seis categorias tengan representacion en los tickets;
6. los metodos de pago tengan frecuencias suficientes para construir la tabla de contingencia;
7. `descuento_pct` y `cantidad` presenten variabilidad distinta de cero;
8. los outliers no rompan las formulas monetarias;
9. las variables derivadas se construyan de forma deterministica;
10. los datos permitan ejecutar las pruebas, aunque no todas produzcan significancia estadistica.

Si alguno de estos requisitos no se cumple, se revisara el proceso generador por insuficiencia metodologica. No se modificaran los datos unicamente para obtener valores p favorables.

### 13.12 Matriz resumida de hipotesis

| ID | Pregunta | Unidad | Prueba principal | Alternativa | Tamano del efecto |
|---|---|---|---|---|---|
| H1 | ¿Difiere el ticket entre fisico y digital? | Ticket | t de Welch | Mann-Whitney U | Hedges `g` |
| H2 | ¿Difiere el margen operativo entre ciudades? | Ciudad-mes | Modelo bloqueado + ANOVA tipo II | Friedman | Eta cuadrado parcial |
| H3 | ¿Existe asociacion entre categoria y pago? | Ticket | Chi-cuadrado | Monte Carlo / analisis estratificado | V de Cramer |
| H4 | ¿Existe relacion entre descuento y cantidad? | Linea | Spearman | Analisis estratificado | `rho` de Spearman |

### 13.13 Variables requeridas y disponibilidad

| Hipotesis | Campos fisicos requeridos | Variables derivadas |
|---|---|---|
| H1 | `id_venta`, `monto_total`, `canal` | `ticket_total`, `grupo_canal` |
| H2 | `fecha`, `id_tienda`, `id_producto`, `monto_total`, `cantidad`, `costo_unitario`, `costo_almacenamiento`, `ciudad`, `tipo` | `periodo_mes`, `margen_bruto`, `margen_operativo_pct_ciudad_mes` |
| H3 | `id_venta`, `id_producto`, `monto_total`, `metodo_pago`, `categoria` | `categoria_ticket` |
| H4 | `descuento_pct`, `cantidad` | No requiere variable adicional |

La revision de F0-05 concluye que el contrato actual contiene todos los campos fisicos necesarios. No se requiere anadir nuevas columnas a los CSV.

### 13.14 Reproducibilidad del analisis

El notebook de la Parte 1 debera:

- ejecutarse de principio a fin sin intervencion manual;
- cargar unicamente los CSV oficiales;
- construir las variables derivadas mediante codigo;
- utilizar semilla 2026 en procedimientos bootstrap o aleatorios;
- mostrar las salidas de las pruebas;
- documentar cada decision mediante celdas Markdown;
- separar claramente objetivo, metodo, resultado e interpretacion;
- registrar en la bitacora los prompts de IA relevantes;
- evitar editar manualmente los resultados producidos por el codigo.

### 13.15 Resultado esperado de F0-05

F0-05 deja definidos:

- cuatro problemas inferenciales;
- sus hipotesis nulas y alternativas;
- las unidades de analisis;
- las variables fisicas y derivadas;
- las pruebas principales y alternativas;
- los supuestos;
- los tamanos del efecto;
- los intervalos de confianza;
- el tratamiento de faltantes y outliers;
- los criterios de aptitud estadistica del dataset;
- los requisitos de reproducibilidad.

La Parte 1 debera implementar esta especificacion sobre el dataset oficial, sin redefinir unilateralmente las hipotesis o sus granularidades.

## 14. Problemas predictivos de demanda y churn

### 14.1 Objetivo y alcance

Esta sección define la planificación de la Parte 3. Su propósito es establecer de forma reproducible:
 - los dos problemas predictivos; - sus variables objetivo y unidades de análisis; - las ventanas y particiones temporales; - las variables permitidas y prohibidas; - los baselines y modelos candidatos; - el preprocesamiento y la optimización de hiperparámetros; - las métricas de evaluación; - la interpretación de los modelos; - las salidas que consumirán F0-07 y Power BI.
La Parte 3 implementará un problema de regresión para demanda y un problema de clasificación para churn. La
especificación se formula antes de observar los resultados definitivos y no predetermina qué modelo será el
ganador.

### 14.2 Principios comunes de modelado

Los dos problemas respetarán estas reglas:

1. Las particiones serán temporales; no se dividirán filas aleatoriamente.
2. Los conjuntos de prueba permanecerán aislados hasta la evaluación final.
3. Las imputaciones, codificaciones y escalados se ajustarán únicamente con datos de entrenamiento mediante
pipelines.
4. Los identificadores técnicos no se utilizarán como predictores.
5. Todo procedimiento aleatorio utilizará la semilla 2026.
6. Cada modelo se comparará contra al menos un baseline simple.
7. La selección de hiperparámetros utilizará únicamente entrenamiento y validación temporal.
8. No se modificará el dataset para obtener métricas favorables.
9. La selección final considerará métricas, estabilidad, interpretabilidad y utilidad de negocio.
10. Los resultados serán reproducibles y se exportarán sin edición manual.

### 14.3 Problema de pronóstico de demanda

#### Pregunta

> ¿Cuántas unidades se venderán en cada nodo y categoría durante el siguiente mes?

#### Tipo de problema

Regresión supervisada sobre un panel temporal.

#### Variable objetivo

```text
demanda_unidades = SUM(ventas.cantidad)
```

#### Granularidad

```text
periodo_objetivo × id_tienda × categoria
```

Se conservarán las combinaciones activas sin ventas con `demanda_unidades = 0`.

#### Horizonte

Un mes hacia adelante.

Para pronosticar el mes `t`, solo se utilizará información disponible hasta el final del mes `t-1`, además de
variables de calendario conocidas anticipadamente.

#### Pronóstico operativo

Después de seleccionar el modelo mediante los periodos históricos, se reentrenará con toda la información
disponible hasta diciembre de 2025 y se generará el pronóstico de enero de 2026.

### 14.4 Variables predictoras de demanda

#### Variables estáticas
 - `id_tienda` tratado como categoría;
 - ciudad;
 - región;
 - tipo de nodo;
 - canal;
 - categoría.

#### Variables de calendario conocidas
 - año;
 - mes;
 - trimestre;
 - tendencia temporal;
 - `mes_sin` y `mes_cos`;
 - indicador de julio;
 - indicador de diciembre.
#### Variables históricas
 - demanda rezagada 1, 2, 3, 6 y 12 meses;
 - media móvil de demanda de 3, 6 y 12 meses;
 - desviación móvil de 3 meses;
 - número de tickets del mes anterior;
 - descuento promedio del mes anterior;
 - precio promedio del mes anterior;
 - proporción de líneas promocionadas del mes anterior.

Las medias móviles se calcularán después de desplazar la serie un mes, de modo que no incluyan el target del
periodo que se intenta predecir.

No se utilizarán el descuento real, el precio real, el número de tickets real ni la cantidad real del mes
objetivo.

### 14.5 Partición y validación temporal de demanda

Los targets se dividirán así:

| Conjunto | Periodos objetivo |
|---|---|
| Entrenamiento | 2024-01 a 2025-06 |
| Validación final | 2025-07 a 2025-09 |
| Prueba final | 2025-10 a 2025-12 |

El año 2023 se utilizará como historia para construir rezagos, especialmente el rezago de 12 meses.

La optimización interna utilizará cuatro folds de ventana expansiva. Todas las filas del mismo `periodo_objetivo`
permanecerán juntas en un mismo fold.

### 14.6 Baselines, modelos y métricas de demanda

#### Baselines obligatorios

1. Pronóstico igual a la demanda del mes anterior.
2. Pronóstico igual a la demanda del mismo mes del año anterior.

#### Modelos base
 - Ridge Regression; - DecisionTreeRegressor.

#### Modelos avanzados
 - RandomForestRegressor; - HistGradientBoostingRegressor.

No se decidirá anticipadamente cuál modelo será el ganador.

#### Métricas

Se reportarán:
 - MAE; - RMSE; - R²; - WAPE.

```text
WAPE = SUM(|y_real - y_pred|) / SUM(|y_real|)
```

MAE será la métrica principal de selección por su interpretación directa en unidades. En caso de resultados muy
cercanos se considerarán RMSE, estabilidad temporal, WAPE e interpretabilidad.

Las predicciones negativas se truncarán a cero únicamente en la salida final; las métricas deberán reportarse de
forma coherente indicando si se calcularon antes o después del truncamiento.

### 14.7 Definición del problema de churn
#### Pregunta
> ¿Qué clientes presentan mayor probabilidad de no realizar compras durante los 90 días posteriores a una fecha de
observación?

#### Tipo de problema

Clasificación binaria.

#### Unidad de análisis

```text
id_cliente × fecha_observacion
```

#### Elegibilidad

Un cliente será incluido cuando:
 - se encuentre registrado a la fecha de observación; - tenga al menos una compra histórica hasta esa fecha.

#### Target

```text
churn_90d = 1
si no existe ninguna compra en
(fecha_observacion, fecha_observacion + 90 días]

churn_90d = 0
en caso contrario
```

#### Fechas de observación

```text
2023-12-31
2024-03-31
2024-06-30
2024-09-30
2024-12-31
2025-03-31
2025-06-30
2025-09-30
```

La última ventana objetivo termina dentro del periodo disponible del dataset.

### 14.8 Variables predictoras de churn

#### Variables RFM y de comportamiento
 - recencia en días al corte;
 - frecuencia de tickets en los últimos 365 días;
 - valor monetario en los últimos 365 días;
 - ticket promedio;
 - unidades compradas;
 - meses activos;
 - número de categorías distintas;
 - categoría dominante;
 - proporción de compras digitales;
 - proporción Web;
 - proporción App;
 - descuento promedio;
 - días desde la penúltima compra;
 - indicador de cliente con una sola compra;
 - frecuencia de los últimos 90 días;
 - frecuencia de los 90 días anteriores;
 - tendencia reciente de frecuencia.

#### Variables de perfil disponibles al corte
 - edad;
 - género;
 - ciudad;
 - segmento comercial;
 - canal preferido;
 - antigüedad del cliente.
La recencia utilizará toda la historia disponible hasta el corte. Las demás variables de comportamiento utilizarán
principalmente la ventana de 365 días.

No se utilizarán `id_cliente`, nombre, compras futuras, el indicador descriptivo final, el target ni segmentos
calculados con información posterior al corte.

### 14.9 Partición y validación temporal de churn

| Conjunto | Fechas de observación |
|---|---|
| Entrenamiento | 2023-12-31, 2024-03-31, 2024-06-30, 2024-09-30 y 2024-12-31 |
| Validación | 2025-03-31 y 2025-06-30 |
| Prueba final | 2025-09-30 |

Un mismo cliente puede aparecer en distintos cortes porque el objetivo es simular evaluaciones periódicas del
mismo negocio. Cada fila deberá respetar su propia fecha de observación y no podrá usar datos futuros.

La validación interna avanzará por fechas de observación completas. No se mezclarán filas de una misma fecha entre
entrenamiento y validación.

### 14.10 Baselines, modelos y métricas de churn

#### Baselines obligatorios

1. Clasificador de clase mayoritaria.
2. Regla de recencia: predecir churn cuando `recencia_dias > 60`.

#### Modelos base
 - LogisticRegression; - DecisionTreeClassifier.

#### Modelos avanzados
 - RandomForestClassifier; - HistGradientBoostingClassifier.

#### Métricas obligatorias
 - accuracy; - precision; - recall; - F1; - AUC-ROC; - matriz de confusión.

También se reportará PR-AUC por su utilidad cuando la clase positiva no esté equilibrada.

F1 será la métrica principal para seleccionar el umbral de clasificación sobre validación. Si varios umbrales
obtienen el mismo F1 redondeado a cuatro decimales, se elegirá el de mayor recall. El umbral se congelará antes de
evaluar el conjunto de prueba.

El valor 0.50 no se asumirá automáticamente como umbral final.

### 14.11 Preprocesamiento y pipelines

Se utilizarán `Pipeline` y `ColumnTransformer` para evitar fuga de información.

#### Variables numéricas
 - imputación con mediana; - escalamiento con StandardScaler para modelos lineales; - sin escalamiento obligatorio para modelos de árboles.

#### Variables categóricas
 - imputación con la categoría más frecuente o `Desconocido`; - OneHotEncoder con manejo de categorías desconocidas.
Cada pipeline se ajustará únicamente con el conjunto de entrenamiento correspondiente.

Los valores faltantes no se rellenarán antes de realizar la partición temporal.
### 14.12 Optimización de hiperparámetros

La búsqueda se realizará únicamente sobre entrenamiento mediante folds temporales.

Se utilizará `RandomizedSearchCV` como opción principal por eficiencia. `GridSearchCV` podrá utilizarse cuando el
espacio de búsqueda sea pequeño.

El conjunto de prueba no se consultará para:
 - seleccionar variables; - elegir modelos; - ajustar hiperparámetros; - seleccionar el umbral; - corregir el generador.

### 14.13 Interpretación de modelos

La Parte 3 deberá explicar qué variables influyen en las predicciones.

Se utilizarán:
 - coeficientes estandarizados para modelos lineales; - permutation importance como método común de comparación; - SHAP para el modelo avanzado seleccionado cuando sea compatible y ejecutable en el entorno.

Las interpretaciones deberán traducirse a lenguaje de negocio y no presentarse como causalidad demostrada.

### 14.14 Salidas predictivas

#### `resultados/predicciones_demanda.csv`

```text
periodo_pronostico
id_tienda
categoria
demanda_predicha
demanda_baja
demanda_alta
modelo
```

`demanda_baja` y `demanda_alta` formarán un intervalo empírico central del 80 %, calculado con los cuantiles 10 %
y 90 % de los residuos de validación. El límite inferior se truncará en cero.

#### `resultados/predicciones_churn.csv`

```text
fecha_observacion
id_cliente
probabilidad_churn
prediccion_churn
nivel_riesgo
modelo
```

`nivel_riesgo` se derivará únicamente para comunicación:

```text
Bajo: probabilidad < 0.30
Medio: 0.30 <= probabilidad < 0.60
Alto: probabilidad >= 0.60
```

La clasificación operativa seguirá utilizando el umbral seleccionado en validación, aunque no coincida con los
límites descriptivos de nivel de riesgo.

#### `resultados/metricas_predictivas.csv`

```text
problema
modelo
conjunto
metrica
valor
``
#### `resultados/importancia_variables.csv`

```text
problema
modelo
variable
importancia
metodo
```

### 14.15 Relación con F0-07

La salida principal hacia la Parte 4 será el pronóstico de enero de 2026 por nodo y categoría.

F0-07 deberá:
 - formular la optimización en esa misma granularidad; o - documentar un método reproducible para desagregar la demanda a producto-nodo mediante participaciones
históricas.

F0-06 no asignará silenciosamente la demanda de una categoría a productos individuales.

Los límites bajo y alto permitirán evaluar escenarios de demanda conservador, central y alto.

### 14.16 Reproducibilidad

El notebook de la Parte 3 deberá:
 - ejecutarse de principio a fin sin intervención manual; - cargar únicamente los CSV oficiales y la configuración aprobada; - construir targets y features mediante código; - utilizar semilla 2026; - aplicar particiones temporales declaradas en el YAML; - conservar el conjunto de prueba aislado; - exportar los cuatro archivos de resultados; - mostrar métricas, gráficos e interpretación; - registrar prompts de IA relevantes en la bitácora; - documentar las versiones de librerías y el entorno; - evitar editar manualmente predicciones o métricas.

### 14.17 Resultado esperado de F0-06

F0-06 deja definidos:
 - un problema de regresión de demanda; - un problema de clasificación de churn; - sus targets y granularidades; - horizontes, ventanas y cortes temporales; - variables permitidas y prohibidas; - reglas de elegibilidad; - baselines y modelos candidatos; - preprocesamiento mediante pipelines; - validación cruzada temporal; - métricas y reglas de selección; - prevención de fuga de información; - interpretación de variables; - salidas hacia F0-07 y Power BI; - criterios de aptitud predictiva del dataset.

La Parte 3 deberá implementar esta especificación sin redefinir unilateralmente los problemas o consultar los
conjuntos de prueba durante el desarrollo.
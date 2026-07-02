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

> ¿Qué demanda se espera por categoría y periodo?

> ¿Qué clientes presentan mayor probabilidad de volverse inactivos?

El proyecto abordará:

- un problema de regresión para pronosticar demanda;
- un problema de clasificación para predecir churn o inactividad.

Inicialmente se propone pronosticar demanda por periodo, ciudad, canal y categoría. La granularidad y el horizonte definitivos se validarán en F0-06.

El umbral de inactividad será de 90 días. F0-06 definirá la fecha de observación, el periodo objetivo y la construcción del target para evitar fuga de información.

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

---

## 10. Aspectos reservados para tareas posteriores

F0-04 cierra los parámetros de generación, los volúmenes, los patrones controlados y los criterios básicos de aceptación del dataset. Las siguientes decisiones permanecen reservadas para tareas posteriores:

- formulación definitiva de las hipótesis y pruebas estadísticas de la Parte 1;
- criterios de segmentación RFM o clustering de la Parte 2;
- fecha de observación, ventana de variables y periodo objetivo del modelo de churn, evitando fuga de información;
- granularidad y horizonte definitivos del pronóstico de demanda;
- variables predictoras, particiones temporales y métricas de evaluación de los modelos;
- variables de decisión, función objetivo y restricciones del modelo prescriptivo;
- estructura definitiva del modelo de datos, medidas DAX y páginas de Power BI;
- archivos de salida analíticos específicos de cada una de las cinco partes.

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

Un cliente será considerado inactivo si no realizó compras durante los 90 días anteriores al 31 de diciembre de 2025.

La proporción objetivo de clientes inactivos será de 25 % a 35 %.

La generación utilizará un score basado en RFM con los siguientes pesos:

| Componente      | Peso |
| --------------- | ---: |
| Recencia        | 50 % |
| Frecuencia      | 30 % |
| Valor monetario | 20 % |

Estos pesos se utilizarán para generar un patrón aprendible, pero no se almacenarán como una etiqueta explicativa en `clientes.csv`.

La construcción definitiva del dataset de entrenamiento, la ventana histórica y la prevención de fuga de información se definirán en F0-06.

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

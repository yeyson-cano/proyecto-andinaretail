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

---

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

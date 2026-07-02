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

---

## 10. Aspectos reservados para tareas posteriores

- Volúmenes exactos de registros por tabla.
- Distribuciones de productos, clientes, precios, costos y cantidades.
- Magnitud de los picos de julio y diciembre.
- Evolución cuantitativa del canal digital.
- Magnitud de la caída de margen operativo en Trujillo.
- Rangos de descuentos y costos de almacenamiento.
- Fecha de observación y construcción temporal del target de churn.
- Granularidad y horizonte definitivos del pronóstico de demanda.
- Función objetivo y restricciones del modelo prescriptivo.
- Criterios automáticos de aceptación del dataset.
- Archivos de salida analíticos de cada fase.

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

- Los nodos virtuales Web y App se modelan como nodos de cumplimiento que pueden mantener inventario.
- La cantidad exacta de nodos digitales se definirá en F0-04.
- Las ventas digitales se atribuyen comercialmente a la ciudad del cliente.
- Los costos de almacenamiento digital se atribuyen al nodo virtual que atiende la venta.
- La continuidad mensual exige que el stock final de un mes sea el stock inicial del siguiente.
- Las unidades vendidas del inventario deben conciliar con las ventas agregadas por producto, nodo y mes.

### 11.6 Trazabilidad resumida

| Elemento | P1 | P2 | P3 | P4 | P5 |
|---|---:|---:|---:|---:|---:|
| Ventas, tickets y márgenes | ✓ | ✓ | ✓ | — | ✓ |
| Ciudad, canal y categoría | ✓ | ✓ | ✓ | ✓ | ✓ |
| Descuentos y precios | ✓ | ✓ | ✓ | — | ✓ |
| Historial por cliente | — | ✓ | ✓ | — | ✓ |
| Inventario y almacenamiento | — | ✓ | — | ✓ | ✓ |
| Demanda agregada | — | ✓ | ✓ | ✓ | ✓ |

### 11.7 Pendientes después de F0-03

F0-04 deberá parametrizar los volúmenes, distribuciones, patrones y tolerancias. F0-05 a F0-07 deberán cerrar las definiciones estadísticas, predictivas y prescriptivas que todavía dependen del contrato.

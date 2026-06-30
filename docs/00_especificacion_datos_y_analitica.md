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
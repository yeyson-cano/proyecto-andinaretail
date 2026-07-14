# Proyecto AndinaRetail

Proyecto grupal de la asignatura **Analítica de Datos** de la Escuela Profesional de Ingeniería de Software — FISI, UNMSM.

## Caso de estudio

AndinaRetail S.A.C. es una empresa ficticia del sector retail omnicanal peruano. El proyecto desarrolla una solución integral de analítica de datos utilizando información sintética, reproducible y validada.

El trabajo abarca el ciclo completo de analítica:

1. Generación y validación de datos sintéticos.
2. Análisis estadístico descriptivo e inferencial.
3. Análisis descriptivo, segmentación y diagnóstico de negocio.
4. Modelos predictivos de demanda y churn.
5. Modelo prescriptivo de reposición de inventario.
6. Tablero integrado en Power BI.
7. Presentación final para la defensa del proyecto.

## Integrantes y responsabilidades

| Integrante | Responsabilidad principal |
|---|---|
| Yeyson Samir Cano Carbajo | Líder de proyecto / Data PM / integración final |
| Daniel Huber Triveño Ruffner | Ingeniería de datos, generación y validación |
| Carlos Alberto Castillo Bernal | Análisis estadístico, descriptivo y diagnóstico |
| Adrian Castillo Santa Cruz | Ciencia de datos, demanda y churn |
| Deysi Anali Ostos Torres | Optimización prescriptiva y Power BI |

## Estructura del repositorio

```text
config/        Parámetros y escenarios de generación, modelado y optimización.
datos/         Script generador, validaciones, CSV oficiales y diccionario de datos.
docs/          Especificación, bitácora de prompts y documentación complementaria.
notebooks/     Notebooks de las Partes 1 a 4.
powerbi/       Tablero Power BI y exportación revisable.
presentacion/  Presentación final del proyecto.
resultados/    Resultados analíticos reutilizables y archivos para Power BI.
```

Archivos principales de documentación:

- `docs/00_especificacion_datos_y_analitica.md`
- `datos/data_dictionary.md`
- `datos/DATASET_VERSION.md`
- `docs/bitacora_prompts.md`

## Entorno de trabajo

El proyecto debe ejecutarse con **Python 3.11.x**. Se recomienda usar Python 3.11.9 si está disponible. Cada integrante debe crear su propio entorno virtual local; la carpeta `.venv/` no debe subirse al repositorio.

### Crear entorno virtual

En Windows con Git Bash:

```bash
py -3.11 -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

En Windows con PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Registrar kernel para notebooks

```bash
python -m ipykernel install --user --name andinaretail --display-name "Python 3.11 - AndinaRetail"
```

Al abrir los notebooks, seleccionar el kernel:

```text
Python 3.11 - AndinaRetail
```

## Dataset oficial v1

El dataset oficial v1 queda versionado en `datos/` y debe utilizarse como fuente para los notebooks, resultados derivados, Power BI y presentación final.

Archivos oficiales:

- `datos/tiendas.csv`
- `datos/productos.csv`
- `datos/clientes.csv`
- `datos/ventas.csv`
- `datos/inventario.csv`

La versión y regla de congelamiento se documentan en:

```text
datos/DATASET_VERSION.md
```

Los CSV oficiales no deben modificarse manualmente después de congelarlos. Si se requiere regenerar datos, debe ejecutarse el generador y luego el validador.

## Orden de ejecución del proyecto

Todos los comandos deben ejecutarse desde la raíz del repositorio.

### 1. Generar datos sintéticos

```bash
python datos/generar_datos.py
```

Este script genera las cinco tablas fuente en `datos/`.

### 2. Validar dataset

```bash
python datos/validar_datos.py
```

El validador revisa integridad, llaves, fórmulas, volúmenes, patrones, calidad de datos y aptitud analítica. El reporte se genera en:

```text
resultados/reporte_validacion_datos.txt
```

### 3. Ejecutar notebooks

La forma recomendada para revisión académica es abrir cada notebook y ejecutar todas sus celdas en orden usando la opción **Run All / Ejecutar todo**.

Orden de ejecución:

1. `notebooks/01_estadistica.ipynb`
2. `notebooks/02_descriptivo_diagnostico.ipynb`
3. `notebooks/03_predictivo.ipynb`
4. `notebooks/04_prescriptivo.ipynb`

Opcionalmente, también pueden ejecutarse por terminal:

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/01_estadistica.ipynb --ExecutePreprocessor.kernel_name=python3
jupyter nbconvert --to notebook --execute --inplace notebooks/02_descriptivo_diagnostico.ipynb --ExecutePreprocessor.kernel_name=python3
jupyter nbconvert --to notebook --execute --inplace notebooks/03_predictivo.ipynb --ExecutePreprocessor.kernel_name=python3
jupyter nbconvert --to notebook --execute --inplace notebooks/04_prescriptivo.ipynb --ExecutePreprocessor.kernel_name=python3
```

### 4. Revisar tablero Power BI

Abrir el archivo:

```text
powerbi/andinaretail_dashboard.pbix
```

El tablero integra las cinco tablas fuente y los resultados analíticos generados. Sus páginas son:

1. Ejecutivo.
2. Ventas y margen.
3. Clientes, segmentación y churn.
4. Predicción de demanda y reposición.

La exportación revisable se encuentra en:

```text
powerbi/andinaretail_dashboard.pdf
```

### 5. Revisar presentación final

La presentación final del proyecto se encuentra en:

```text
presentacion/AndinaRetail_presentacion_final.pptx
```

## Partes del proyecto y entregables

| Parte | Responsable principal | Archivo principal | Salidas principales |
|---|---|---|---|
| Datos y validación | Daniel | `datos/generar_datos.py`, `datos/validar_datos.py` | CSV base y `reporte_validacion_datos.txt` |
| P1 Estadística | Carlos | `notebooks/01_estadistica.ipynb` | `resumen_estadistico.csv`, `pruebas_hipotesis.csv` |
| P2 Descriptivo | Carlos | `notebooks/02_descriptivo_diagnostico.ipynb` | `segmentacion_clientes.csv`, `diagnostico_trujillo.csv` |
| P3 Predictivo | Adrian | `notebooks/03_predictivo.ipynb` | demanda, churn, métricas e importancia de variables |
| P4 Prescriptivo | Deysi | `notebooks/04_prescriptivo.ipynb` | reposición, escenarios y uso de capacidad |
| P5 Power BI | Deysi | `powerbi/andinaretail_dashboard.pbix` | tablero integrado y exportación PDF |
| Final | Yeyson | `README.md`, presentación final | documentación e integración para defensa |

## Archivos generados

### Validación

```text
resultados/reporte_validacion_datos.txt
```

### Parte 1 — Estadística

```text
resultados/resumen_estadistico.csv
resultados/pruebas_hipotesis.csv
```

### Parte 2 — Descriptivo, segmentación y diagnóstico

```text
resultados/segmentacion_clientes.csv
resultados/diagnostico_trujillo.csv
```

### Parte 3 — Modelos predictivos

```text
resultados/predicciones_demanda.csv
resultados/predicciones_churn.csv
resultados/metricas_predictivas.csv
resultados/importancia_variables.csv
```

### Parte 4 — Modelo prescriptivo

```text
resultados/recomendaciones_reposicion.csv
resultados/resumen_escenarios_optimizacion.csv
resultados/uso_capacidad_optimizacion.csv
```

### Parte 5 — Power BI

```text
powerbi/andinaretail_dashboard.pbix
powerbi/andinaretail_dashboard.pdf
```

### Presentación final

```text
presentacion/AndinaRetail_presentacion_final.pptx
```

## Resumen de componentes analíticos

### Parte 1 — Estadística descriptiva e inferencial

El notebook `notebooks/01_estadistica.ipynb` resume el comportamiento general de ventas, clientes, tickets, descuentos y márgenes. También desarrolla pruebas de hipótesis para contrastar diferencias o relaciones relevantes del negocio.

### Parte 2 — Análisis descriptivo, segmentación y diagnóstico

El notebook `notebooks/02_descriptivo_diagnostico.ipynb` analiza tendencias, Pareto, comportamiento por ciudad, canal y categoría. Además, construye segmentación RFM y desarrolla el diagnóstico del deterioro de margen operativo en Trujillo.

### Parte 3 — Modelos predictivos de demanda y churn

El notebook `notebooks/03_predictivo.ipynb` contiene dos bloques:

- **Demanda:** pronóstico mensual por `periodo_objetivo × id_tienda × categoria`.
- **Churn:** estimación de probabilidad de inactividad a 90 días por cliente.

Las salidas de demanda alimentan el modelo prescriptivo de reposición y Power BI. Las salidas de churn se usan como insumo para el análisis de clientes y riesgo de abandono.

### Parte 4 — Modelo prescriptivo de reposición

El notebook `notebooks/04_prescriptivo.ipynb` utiliza `resultados/predicciones_demanda.csv`, stock final de diciembre 2025, costos, capacidad y escenarios definidos en `config/escenarios.yaml`.

El modelo se formula con PuLP/CBC y define variables de reposición, faltante e inventario final. Las salidas permiten interpretar la reposición recomendada, sensibilidad por escenario, nivel de servicio y uso de capacidad.

### Parte 5 — Power BI integrado

El tablero Power BI integra datos fuente y resultados analíticos para presentar la solución de forma visual. Sus cuatro páginas permiten revisar el estado ejecutivo, ventas y margen, clientes y churn, y la integración entre predicción de demanda y reposición.

## Reproducibilidad y trazabilidad

- Los datos son sintéticos y reproducibles.
- Los parámetros de generación, validación, modelado y optimización se centralizan en `config/escenarios.yaml`.
- El dataset oficial v1 está congelado y documentado en `datos/DATASET_VERSION.md`.
- Las reglas de negocio, campos y patrones analíticos se documentan en `docs/00_especificacion_datos_y_analitica.md` y `datos/data_dictionary.md`.
- El uso de IA generativa se registra en `docs/bitacora_prompts.md`.
- Las salidas analíticas se guardan en `resultados/` para facilitar revisión, trazabilidad y consumo desde Power BI.

## Consideraciones para el evaluador

Para revisar el proyecto de forma rápida:

1. Leer este `README.md`.
2. Revisar `datos/DATASET_VERSION.md`.
3. Ejecutar `python datos/validar_datos.py`.
4. Abrir y ejecutar los notebooks en orden.
5. Revisar los CSV generados en `resultados/`.
6. Abrir `powerbi/andinaretail_dashboard.pbix` o revisar su PDF exportado.
7. Revisar `presentacion/AndinaRetail_presentacion_final.pptx`.

Si solo se desea revisar resultados sin regenerar todo, pueden utilizarse directamente los CSV oficiales versionados en `datos/` y `resultados/`.

## Consideraciones adicionales

- No subir `.venv/` al repositorio.
- Instalar dependencias únicamente desde `requirements.txt`.
- Ejecutar scripts y notebooks desde la raíz del repositorio.
- Si se cambia el entorno del proyecto, actualizar primero `requirements.txt` y luego este README.
- En algunas instalaciones, Faker puede no reconocer el locale `es_PE`. En ese caso, el generador usa `es_ES` como respaldo local y continúa la ejecución sin modificar los parámetros del proyecto.

## Estado final

Proyecto finalizado con dataset oficial v1, Partes 1 a 5 implementadas, tablero Power BI integrado, documentación de ejecución y presentación final para defensa.

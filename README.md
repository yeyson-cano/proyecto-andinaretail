# Proyecto AndinaRetail

Proyecto grupal de la asignatura **Analítica de Datos** de la Escuela Profesional de Ingeniería de Software — FISI, UNMSM.

## Caso de estudio

AndinaRetail S.A.C. es una empresa ficticia del sector retail omnicanal peruano. El proyecto desarrollará una solución integral de analítica de datos utilizando información sintética y reproducible.

El trabajo abarcará:

1. Análisis estadístico.
2. Análisis descriptivo y diagnóstico.
3. Modelos predictivos de demanda y churn.
4. Optimización de inventario.
5. Tableros de control en Power BI.

## Integrantes y roles

| Integrante | Rol principal |
|---|---|
| Yeyson Samir Cano Carbajo | Líder de proyecto / Data PM |
| Daniel Huber Triveño Ruffner | Ingeniería de datos |
| Carlos Alberto Castillo Bernal | Análisis estadístico y descriptivo |
| Adrian Castillo Santa Cruz | Ciencia de datos |
| Deysi Anali Ostos Torres | Optimización y Power BI |

## Estructura del repositorio

- `config/`: parámetros y escenarios de generación.
- `datos/`: script generador, validaciones, CSV y diccionario de datos.
- `notebooks/`: notebooks correspondientes a las Partes 1 a 4.
- `resultados/`: resultados analíticos reutilizables y archivos para Power BI.
- `powerbi/`: archivo PBIX y exportación del tablero.
- `docs/`: especificaciones, bitácora de prompts y autoevaluación.
- `presentacion/`: presentación utilizada en la defensa final.

## Entorno de trabajo

El proyecto debe ejecutarse con Python 3.11.x. Se recomienda usar Python 3.11.9 si está disponible. Cada integrante debe crear su propio entorno virtual local; la carpeta `.venv/` no debe subirse al repositorio.

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

### Ejecutar generación de datos

Desde la raíz del repositorio:

```bash
python datos/generar_datos.py
```
### Validar dataset

Después de generar los CSV, ejecutar:

```bash
python datos/validar_datos.py
```

El validador revisa integridad, fórmulas, volúmenes, patrones, calidad de datos y aptitud analítica. El reporte se genera en:

```text
resultados/reporte_validacion_datos.txt
```

### Consideraciones

- No subir `.venv/` al repositorio.
- Instalar dependencias únicamente desde `requirements.txt`.
- Ejecutar los comandos desde la raíz del repositorio.
- Si se cambia el entorno del proyecto, actualizar primero `requirements.txt` y luego este README.

## Flujo previsto de ejecución
1. Instalar las dependencias de requirements.txt.
2. Generar los datos sintéticos o usar el dataset oficial v1 ya congelado.
3. Validar la integridad y los patrones del dataset.
4. Ejecutar los notebooks en orden numérico:
   - notebooks/01_estadistica.ipynb
   - notebooks/02_descriptivo_diagnostico.ipynb
   - notebooks/03_predictivo.ipynb
5. Utilizar los resultados generados en resultados/ como insumo para optimización, Power BI y presentación final.
6. Actualizar y abrir el tablero de Power BI.

> La guía de ejecución se completará conforme se implementen los componentes.
> Los patrones analíticos y las reglas de calidad implementadas por el generador se documentan en `datos/data_dictionary.md` y `docs/00_especificacion_datos_y_analitica.md`. Los valores numéricos de generación y validación se mantienen en `config/escenarios.yaml`.
> En algunas instalaciones, Faker puede no reconocer el locale `es_PE`. En ese caso, el generador usa `es_ES` como respaldo local y continúa la ejecución sin modificar los parámetros del proyecto.

### Dataset oficial v1

El dataset oficial v1 queda versionado en `datos/` y debe utilizarse como fuente para los notebooks, resultados derivados y Power BI.

Archivos oficiales:

- `datos/tiendas.csv`
- `datos/productos.csv`
- `datos/clientes.csv`
- `datos/ventas.csv`
- `datos/inventario.csv`

La versión y regla de congelamiento se documentan en `datos/DATASET_VERSION.md`. Los CSV oficiales no deben modificarse manualmente después de congelarlos.

### Modelos predictivos P3
El notebook notebooks/03_predictivo.ipynb contiene la Parte 3 del proyecto:
- **Parte 3A – Modelo predictivo de demanda:** pronostica demanda mensual por periodo_objetivo x id_tienda x categoria.
- **Parte 3B – Modelo predictivo de churn:** estima la probabilidad de inactividad a 90 días por cliente usando snapshots cliente x fecha observación.

Salidas generadas en resultados/:
- resultados/predicciones_demanda.csv
- resultados/predicciones_churn.csv
- resultados/metricas_predictivas.csv
- resultados/importancia_variables.csv

Ejecución recomendada desde la raíz del repositorio:
```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/03_predictivo.ipynb --ExecutePreprocessor.kernel_name=python3
```
### Parte 4 — Modelo prescriptivo de reposición

La Parte 4 se implementa en `notebooks/04_prescriptivo.ipynb` y utiliza como input principal `resultados/predicciones_demanda.csv`, generado por la Parte 3.

El notebook usa el stock final de diciembre de 2025 desde `datos/inventario.csv`, costos derivados de `datos/productos.csv` y `datos/ventas.csv`, y los escenarios configurados en `config/escenarios.yaml`.

Para ejecutar la Parte 4 desde la raíz del repositorio:

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/04_prescriptivo.ipynb --ExecutePreprocessor.kernel_name=python3
```

Salidas oficiales:

- `resultados/recomendaciones_reposicion.csv`
- `resultados/resumen_escenarios_optimizacion.csv`
- `resultados/uso_capacidad_optimizacion.csv`

Estas salidas son consumidas por Power BI y por la presentación final para explicar reposición recomendada, sensibilidad por escenario, nivel de servicio y uso de capacidad.


## Estado

Proyecto con dataset oficial v1 y Partes 1, 2, 3 y 4 implementadas. Pendiente la integración final en Power BI, exportación del tablero y presentación.
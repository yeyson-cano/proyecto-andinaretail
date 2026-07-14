# Checklist de entrega final — AndinaRetail S.A.C.

## Estado general

- Rama revisada: `main`
- Fecha de revisión: 2026-07-14
- Responsable de revisión: Equipo AndinaRetail
- Estado final: Repositorio completo para entrega y revisión académica.

## Checklist de aceptación

| Criterio | Estado | Evidencia |
|---|---|---|
| Los notebooks están ejecutados | Cumplido | `notebooks/01_estadistica.ipynb`, `notebooks/02_descriptivo_diagnostico.ipynb`, `notebooks/03_predictivo.ipynb`, `notebooks/04_prescriptivo.ipynb` |
| Los CSV oficiales existen | Cumplido | Cinco CSV oficiales en `datos/` y `datos/DATASET_VERSION.md` |
| Los resultados en `resultados/` existen | Cumplido | Reporte de validación y resultados de P1, P2, P3 y P4 |
| El `.pbix` y la exportación están en `powerbi/` | Cumplido | Tablero Power BI y exportación revisable |
| El README está actualizado | Cumplido | `README.md` documenta caso, ejecución, responsables y entregables |
| La bitácora está completa | Cumplido | `docs/bitacora_prompts.md` registra prompts relevantes y revisión humana |
| La presentación existe | Cumplido | Presentación final en `presentacion/` |
| No hay rutas locales rotas | Cumplido | Revisión manual y búsqueda de rutas absolutas en archivos de texto |
| El repositorio está integrado en `main` | Cumplido | Entrega consolidada en rama `main` |
| La entrega puede revisarse sin depender del chat | Cumplido | README, notebooks, CSV, Power BI, bitácora y presentación están versionados |

## Archivos principales revisados

### Dataset oficial v1
- `datos/DATASET_VERSION.md`
- `datos/tiendas.csv`
- `datos/productos.csv`
- `datos/clientes.csv`
- `datos/ventas.csv`
- `datos/inventario.csv`

### Resultados analíticos
- `resultados/reporte_validacion_datos.txt`
- `resultados/resumen_estadistico.csv`
- `resultados/pruebas_hipotesis.csv`
- `resultados/segmentacion_clientes.csv`
- `resultados/diagnostico_trujillo.csv`
- `resultados/predicciones_demanda.csv`
- `resultados/predicciones_churn.csv`
- `resultados/metricas_predictivas.csv`
- `resultados/importancia_variables.csv`
- `resultados/recomendaciones_reposicion.csv`
- `resultados/resumen_escenarios_optimizacion.csv`
- `resultados/uso_capacidad_optimizacion.csv`

### Entregables finales
- `powerbi/andinaretail_dashboard.pbix`
- `powerbi/andinaretail_dashboard.pdf`
- `presentacion/AndinaRetail_presentacion_final.pptx`
- `README.md`
- `docs/bitacora_prompts.md`

## Observaciones finales

El repositorio contiene el flujo completo desde generación de datos sintéticos hasta visualización ejecutiva. La entrega puede revisarse mediante `README.md`, notebooks ejecutados, resultados CSV, tablero Power BI, bitácora de prompts y presentación final.
# Dataset oficial v1 — AndinaRetail S.A.C.

## Estado

Dataset oficial congelado para las Partes 1 a 5 del proyecto.

## Versión

- Versión del dataset: v1
- Semilla de generación: 2026
- Versión de configuración: 1.3.0
- Estado de validación: APROBADO

## Archivos congelados

- `datos/tiendas.csv`
- `datos/productos.csv`
- `datos/clientes.csv`
- `datos/ventas.csv`
- `datos/inventario.csv`

## Evidencia de validación

Reporte asociado:

- `resultados/reporte_validacion_datos.txt`

Resumen del reporte:

- Validaciones correctas: 121
- Advertencias: 1
- Errores críticos: 0

## Advertencia aceptada

El reporte indica que `predicciones_demanda.csv` aún no existe. Esta advertencia se acepta porque dicho archivo corresponde a la Parte 3 predictiva y no forma parte del dataset fuente oficial v1.

## Regla de congelamiento

A partir de esta versión, los CSV oficiales no deben modificarse manualmente.

Cualquier cambio futuro deberá realizarse modificando el generador, ejecutando nuevamente el validador y registrando una nueva versión del dataset.

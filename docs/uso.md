# Guía de uso

## Formato del CSV de entrada

El archivo CSV debe tener exactamente estas columnas:

| Columna         | Tipo    | Ejemplo        |
|-----------------|---------|----------------|
| fecha           | fecha   | 2024-01-15     |
| producto        | texto   | Laptop         |
| cantidad        | entero  | 3              |
| precio_unitario | decimal | 1200.00        |
| vendedor        | texto   | Ana García     |

## Ejemplos de uso

**Reporte en consola:**
```bash
python main.py --input data/ventas_ejemplo.csv
```

**Reporte exportado a archivo:**
```bash
python main.py --input data/ventas_ejemplo.csv --output output/reporte.txt
```

## Manejo de errores

- Las filas con datos inválidos se omiten con una advertencia
- Si el CSV está vacío o le faltan columnas, el script termina con error
- La carpeta `output/` debe existir antes de exportar

## Qué muestra el reporte

1. Total de transacciones procesadas
2. Facturación total ($)
3. Ranking de vendedores por monto facturado
4. Ranking de productos por unidades vendidas

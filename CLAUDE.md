# Procesador de Ventas — Contexto para Claude Code

## ¿Qué hace este proyecto?
Script Python que lee CSVs de ventas y genera reportes de resumen con rankings por vendedor y producto.

## Estructura
- `main.py` — punto de entrada CLI con argparse
- `src/procesador.py` — lectura, validación y procesamiento del CSV
- `src/reporte.py` — generación y exportación del reporte
- `src/config.py` — constantes (columnas requeridas, formato de fecha)
- `tests/` — tests unitarios con pytest
- `data/` — CSVs de ejemplo
- `output/` — reportes generados (no versionado)

## Cómo correr el proyecto
```bash
python main.py --input data/ventas_ejemplo.csv
python main.py --input data/ventas_ejemplo.csv --output output/reporte.txt
```

## Cómo correr los tests
```bash
pytest
pytest -v  # verbose
```

## Convenciones
- Nombres de variables y funciones en español
- Un módulo por responsabilidad (procesador, reporte, config)
- Filas inválidas se omiten con advertencia, no rompen el script

## Branching (GitFlow)
- `main` — producción, solo merges desde `release/` o `hotfix/`
- `develop` — integración de features
- `feature/nombre` — nuevas funcionalidades
- `release/x.x.x` — preparación de release
- `hotfix/descripcion` — fixes urgentes en producción

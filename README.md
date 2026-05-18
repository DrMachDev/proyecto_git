# Procesador de Ventas

Script de automatización que procesa archivos CSV de ventas y genera reportes de resumen.

## ¿Qué hace?

- Lee archivos CSV con datos de ventas
- Valida y limpia los datos
- Calcula totales, promedios y rankings por vendedor y producto
- Genera un reporte en consola y en archivo `.txt`

## Estructura del proyecto

```
procesador-ventas/
├── .github/              # Templates de Issues y PRs
├── src/                  # Código fuente
│   ├── procesador.py     # Lógica de procesamiento
│   ├── reporte.py        # Generación de reportes
│   └── config.py         # Configuración
├── tests/                # Pruebas unitarias
├── data/                 # Datos de ejemplo
├── output/               # Reportes generados (no versionado)
├── docs/                 # Documentación
├── main.py               # Punto de entrada
├── requirements.txt
└── CHANGELOG.md
```

## Instalación

```bash
git clone <url-del-repo>
cd procesador-ventas
pip install -r requirements.txt
```

## Uso

```bash
python main.py --input data/ventas_ejemplo.csv
python main.py --input data/ventas_ejemplo.csv --output output/reporte.txt
```

## Versión

Ver [CHANGELOG.md](CHANGELOG.md) para historial de versiones.

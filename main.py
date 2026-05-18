import argparse
import sys
from src.procesador import procesar, calcular_resumen
from src.reporte import imprimir, exportar


def main():
    parser = argparse.ArgumentParser(description="Procesador de ventas CSV")
    parser.add_argument("--input", required=True, help="Ruta al archivo CSV de ventas")
    parser.add_argument("--output", help="Ruta de salida para el reporte (opcional)")
    args = parser.parse_args()

    print(f"Procesando: {args.input}")
    ventas = procesar(args.input)

    if not ventas:
        print("No se encontraron ventas válidas.")
        sys.exit(1)

    resumen = calcular_resumen(ventas)
    imprimir(resumen)

    if args.output:
        exportar(resumen, args.output)


if __name__ == "__main__":
    main()

import csv
from datetime import datetime
from src.config import COLUMNAS_REQUERIDAS, SEPARADOR_CSV, FORMATO_FECHA


def leer_csv(ruta_archivo):
    """Lee el CSV y retorna lista de filas como dicts."""
    with open(ruta_archivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=SEPARADOR_CSV)
        filas = list(reader)
    return filas


def validar_columnas(filas):
    """Verifica que el CSV tenga las columnas requeridas."""
    if not filas:
        raise ValueError("El archivo CSV está vacío.")
    columnas = set(filas[0].keys())
    faltantes = set(COLUMNAS_REQUERIDAS) - columnas
    if faltantes:
        raise ValueError(f"Columnas faltantes: {faltantes}")


def limpiar_fila(fila, numero):
    """Parsea y valida una fila individual. Retorna None si es inválida."""
    try:
        return {
            "fecha": datetime.strptime(fila["fecha"].strip(), FORMATO_FECHA),
            "producto": fila["producto"].strip(),
            "cantidad": int(fila["cantidad"]),
            "precio_unitario": float(fila["precio_unitario"]),
            "vendedor": fila["vendedor"].strip(),
            "total": int(fila["cantidad"]) * float(fila["precio_unitario"]),
        }
    except (ValueError, KeyError):
        print(f"  [ADVERTENCIA] Fila {numero} inválida, se omite: {dict(fila)}")
        return None


def procesar(ruta_archivo):
    """Flujo principal: lee, valida y limpia el CSV. Retorna ventas limpias."""
    filas_raw = leer_csv(ruta_archivo)
    validar_columnas(filas_raw)

    ventas = []
    for i, fila in enumerate(filas_raw, start=2):
        limpia = limpiar_fila(fila, i)
        if limpia:
            ventas.append(limpia)

    return ventas


def calcular_resumen(ventas):
    """Calcula totales y rankings a partir de las ventas limpias."""
    total_general = sum(v["total"] for v in ventas)

    por_vendedor = {}
    for v in ventas:
        por_vendedor.setdefault(v["vendedor"], 0)
        por_vendedor[v["vendedor"]] += v["total"]

    por_producto = {}
    for v in ventas:
        por_producto.setdefault(v["producto"], 0)
        por_producto[v["producto"]] += v["cantidad"]

    return {
        "total_ventas": len(ventas),
        "total_general": total_general,
        "por_vendedor": dict(sorted(por_vendedor.items(), key=lambda x: x[1], reverse=True)),
        "por_producto": dict(sorted(por_producto.items(), key=lambda x: x[1], reverse=True)),
    }

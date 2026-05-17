from datetime import datetime


def generar_texto(resumen):
    """Genera el reporte como string formateado."""
    lineas = [
        "=" * 50,
        "        REPORTE DE VENTAS",
        f"  Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 50,
        f"\nTotal de transacciones: {resumen['total_ventas']}",
        f"Facturación total:      ${resumen['total_general']:,.2f}",
        "\n--- Ranking por Vendedor ---",
    ]
    for vendedor, total in resumen["por_vendedor"].items():
        lineas.append(f"  {vendedor:<20} ${total:>10,.2f}")

    lineas.append("\n--- Ranking por Producto (unidades) ---")
    for producto, cantidad in resumen["por_producto"].items():
        lineas.append(f"  {producto:<20} {cantidad:>6} unidades")

    lineas.append("=" * 50)
    return "\n".join(lineas)


def imprimir(resumen):
    print(generar_texto(resumen))


def exportar(resumen, ruta_salida):
    contenido = generar_texto(resumen)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"Reporte guardado en: {ruta_salida}")

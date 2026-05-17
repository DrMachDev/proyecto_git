import pytest
from src.procesador import validar_columnas, limpiar_fila, calcular_resumen


def test_validar_columnas_correctas():
    filas = [{"fecha": "2024-01-01", "producto": "X", "cantidad": "1",
              "precio_unitario": "10.0", "vendedor": "Ana"}]
    validar_columnas(filas)  # no debe lanzar excepción


def test_validar_columnas_faltantes():
    filas = [{"fecha": "2024-01-01", "producto": "X"}]
    with pytest.raises(ValueError, match="Columnas faltantes"):
        validar_columnas(filas)


def test_validar_csv_vacio():
    with pytest.raises(ValueError, match="vacío"):
        validar_columnas([])


def test_limpiar_fila_valida():
    fila = {"fecha": "2024-01-05", "producto": "Laptop",
            "cantidad": "2", "precio_unitario": "1200.00", "vendedor": "Ana"}
    resultado = limpiar_fila(fila, 2)
    assert resultado is not None
    assert resultado["total"] == 2400.0
    assert resultado["producto"] == "Laptop"


def test_limpiar_fila_invalida():
    fila = {"fecha": "no-es-fecha", "producto": "X",
            "cantidad": "abc", "precio_unitario": "10", "vendedor": "Ana"}
    resultado = limpiar_fila(fila, 5)
    assert resultado is None


def test_calcular_resumen():
    ventas = [
        {"vendedor": "Ana", "producto": "Laptop", "cantidad": 2, "total": 2400.0},
        {"vendedor": "Carlos", "producto": "Mouse", "cantidad": 5, "total": 127.5},
        {"vendedor": "Ana", "producto": "Mouse", "cantidad": 3, "total": 76.5},
    ]
    resumen = calcular_resumen(ventas)
    assert resumen["total_ventas"] == 3
    assert resumen["total_general"] == pytest.approx(2604.0)
    assert list(resumen["por_vendedor"].keys())[0] == "Ana"
    assert list(resumen["por_producto"].keys())[0] == "Mouse"

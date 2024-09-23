def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Ejemplo de uso
monto = 200  # monto total de la compra
descuento = calcular_descuento(monto)
print(f"El descuento es: {descuento}")

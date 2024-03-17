def calcular_descuento(monto_total, porcentaje_descuento=15):

    descuento = monto_total * porcentaje_descuento / 100
    monto_final = monto_total - descuento
    return monto_final

# Solicitar al usuario que ingrese el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))

# Calcular el descuento por defecto del 15%
descuento = monto_total * 0.15
monto_final = calcular_descuento(monto_total)
print(f"descuento: ${descuento:.2f}")
# Mostrar el monto final a pagar
print(f"El monto final a pagar después del descuento es: ${monto_final:.2f}")
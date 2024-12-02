pago = 10
total = 0
for i in range(20):
    print(F"el pago {i + 1} es de ${ pago }")
    total += pago
    pago *= 2
print(f"en total pagara ${ total }")
print("programa que calcula la potencia n de un numero")

base = float(input("ingresa la base: "))
exponente = int(input("ingresa el exponente: "))

potencia = base
for i in range(1,  exponente + 1):
    potencia *= base
    print("el  numero {base} elevado a la potencia {exponente} es {potencia}")
def convertitabinarioconciclos(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
        return binario
    
numero = int(input("introduce un numero entero: "))
binario = convertitabinarioconciclos(numero)
print(f"El numero {numero} en binario es: {binario}")
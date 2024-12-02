def esprimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrarprimos(n):
    contadorprimos = 0
    numactual = 2

    while contadorprimos < n:
        if esprimo(numactual):
            print(numactual)
            contadorprimos += 1
        numactual += 1
cantidad = int(input("introduce la cantidad de numeros primos que quieres mostrar: "))
mostrarprimos(cantidad)
'''Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.'''
def mostrar_tablas_multiplicar():
    # Primer ciclo: recorre los números del 1 al 5
    for numero in range(1, 6):
        print(f"\nTabla de multiplicar del {numero}:")
        # Segundo ciclo: genera los múltiplos de cada número
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

# Llamar a la función
mostrar_tablas_multiplicar()
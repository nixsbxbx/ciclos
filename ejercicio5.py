'''Programa que pida 10 números e imprima el promedio de estos.'''
def calcular_promedio():
    suma = 0  # Acumulador para la suma de los números
    contador = 0  # Contador para llevar el número de entradas

    print("Introduce 10 números para calcular el promedio:")

    for i in range(10):  # Repetir 10 veces
        try:
            numero = float(input(f"Introduce el número {i + 1}: "))
            suma += numero  
            contador += 1  
        except ValueError:
            print("Por favor, introduce un número válido.")
            return

    # Calcular el promedio
    promedio = suma / contador
    print(f"\nEl promedio de los 10 números introducidos es: {promedio:.2f}")

# Llamar a la función
calcular_promedio()
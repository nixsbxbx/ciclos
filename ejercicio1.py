'''Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)'''
def calcular_factorial():
    while True:
        try:
            # Pedir al usuario que ingrese un número
            numero = int(input("Introduce un número entero positivo (Presione 0 para salir): "))
             # Salir del ciclo si el usuario ingresa 0
            if numero == 0:
                print("Programa terminado.")
                break
            # Verificar si el número es no negativo
            if numero < 0:
                print("El factorial no está definido para números negativos. Intenta de nuevo.")
                continue
             # Calcular el factorial usando un ciclo
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            
            # Mostrar el resultado
            print(f"El factorial de {numero} es: {factorial}")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

# Llamar a la función
calcular_factorial()
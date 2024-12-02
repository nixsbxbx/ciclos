'''Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.'''
def contar_numeros():
    try:
        cantidad = int(input("¿Cuántos números deseas introducir? "))  
        mayores_que_cero = 0
        menores_que_cero = 0
        iguales_a_cero = 0

        # Ciclo para pedir los números
        for i in range(cantidad):
            numero = float(input(f"Introduce el número {i + 1}: "))

            # Contar si el número es mayor, menor o igual a 0
            if numero > 0:
                mayores_que_cero += 1
            elif numero < 0:
                menores_que_cero += 1
            else:
                iguales_a_cero += 1

        # Imprimir los resultados
        print(f"\nNúmeros mayores que 0: {mayores_que_cero}")
        print(f"Números menores que 0: {menores_que_cero}")
        print(f"Números iguales a 0: {iguales_a_cero}")

    except ValueError:
        print("Por favor, introduce un número entero válido.")

# Llamar a la función
contar_numeros()
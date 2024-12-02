'''Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)'''
import random

def adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    intentos_totales = 10  # Número de intentos disponibles
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")
    
    for intento in range(1, intentos_totales + 1):
        try:
            # Pedir al usuario que ingrese un número
            numero = int(input(f"Intento {intento}/{intentos_totales}. Introduce un número: "))
            
            # Verificar si el número es el correcto
            if numero == numero_aleatorio:
                print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intento} intento(s).")
                break
            elif numero < numero_aleatorio:
                print("El número que buscas es mayor.")
            else:
                print("El número que buscas es menor.")
            
            # Indicar los intentos restantes
            intentos_restantes = intentos_totales - intento
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intento(s).")
            else:
                print(f"Lo siento, te has quedado sin intentos. El número era {numero_aleatorio}.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
            
# Llamar a la función
adivinar_numero()
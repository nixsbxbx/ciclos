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
    #Numero aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    intentos_totales =10 #Intentos disponibles
    print("¡Bienvenido al juego de adivinar el numero que estoy pensando!")
    print("Pense un numero que esta entre el 1 y el 100, tines solo 10 intentos para adivinar")
    for intento in range(1, intentos_totales + 1 ):
        try:
            #Pedir al usuario que ingrese el numero que crea que estoy pensando
            numero = int(input(f"Intento {intento}/{intentos_totales}. Introduce un numero: "))
            #Verificar si el numero es correcto
            if numero == numero_aleatorio:
                print(f"¡Felicidades! Has adivinado el numero {numero_aleatorio} en {intento} intento(s).")
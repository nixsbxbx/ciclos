'''Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.'''
def intervalo():
    # Solicitar límites del intervalo
    while True:
        limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
        limite_superior = int(input("Introduce el límite superior del intervalo: "))
        
        if limite_inferior < limite_superior:
            break  # Si el límite inferior es menor que el superior, salimos del bucle
        else:
            print("El límite inferior debe ser menor que el límite superior. Intenta de nuevo.")

    suma_intervalo = 0  # Acumulador para la suma de los números dentro del intervalo
    fuera_intervalo = 0  # Contador para los números fuera del intervalo
    limite_igual = False  # Indicador para saber si se introdujo un número igual a los límites

    print("Introduce números hasta que pongas 0 (el programa terminará cuando ingreses 0):")
    
    while True:
        numero = int(input("Introduce un número: "))
        
        if numero == 0:
            break  # Termina el ciclo si se introduce un 0
        
        # Verificar si el número está dentro del intervalo (excluyendo los límites)
        if limite_inferior < numero < limite_superior:
            suma_intervalo += numero  # Acumula la suma de los números dentro del intervalo
        else:
            fuera_intervalo += 1  # Incrementa el contador de números fuera del intervalo
        
        # Verificar si el número es igual a los límites del intervalo
        if numero == limite_inferior or numero == limite_superior:
            limite_igual = True  # Se ha introducido un número igual a un límite

    # Mostrar los resultados
    print(f"\nLa suma de los números dentro del intervalo (abierto) es: {suma_intervalo}")
    print(f"Cantidad de números fuera del intervalo: {fuera_intervalo}")
    if limite_igual:
        print("Se ha introducido un número igual a uno de los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.")

# Llamar a la función
intervalo()
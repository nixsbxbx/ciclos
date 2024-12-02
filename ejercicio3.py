'''Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador'''
def calcular_suma_y_media():
    acumulador = 0  # Inicializar acumulador para la suma
    contador = 0    # Inicializar contador para contar los números introducidos

    print("Introduce números para calcular la suma y la media. Introduce 0 para terminar.")
    
    while True:
        try:
            numero = float(input("Introduce un número: "))
            
            if numero == 0:  # Condición para salir del bucle
                break
            
            acumulador += numero  # Sumar el número al acumulador
            contador += 1         # Incrementar el contador en 1
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    # Calcular la media solo si se introdujeron números
    if contador > 0:
        media = acumulador / contador
        print(f"\nSuma total: {acumulador}")
        print(f"Media de los números: {media}")
    else:
        print("\nNo se introdujeron números.")

# Llamar a la función
calcular_suma_y_media()
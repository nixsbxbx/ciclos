'''Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.'''
def imprimir_pares():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # Asegurarse de que el primer número sea menor que el segundo
    if num1 > num2:
        num1, num2 = num2, num1  # Intercambiar los números si es necesario
    
    # Ciclo para imprimir los números pares entre num1 y num2
    print(f"Los números pares entre {num1} y {num2} son:")
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

# Llamar a la función
imprimir_pares()
'''Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio'''
def verificar_vocales():
    print("Introduce caracteres. El programa terminará cuando se ingrese un espacio.")
    
    while True:
        caracter = input("Introduce un carácter: ")
        
        # Verificar si el carácter es un espacio
        if caracter == " ":
            print("Programa terminado.")
            break
        
        # Verificar si el carácter es una vocal (mayúscula o minúscula)
        if caracter.lower() in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")

# Llamar a la función
verificar_vocales()
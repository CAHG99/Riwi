#1. Contar del 1 al 10: #Usa un while para imprimir los números del 1 al 10.
i=1
while i<=10:
    print(i)
    i+=1

#2. Contar hacia atrás: #Usa un while para imprimir los números del 10 al 1 en orden descendente.
i=10
while i>=0:
    print(i)
    i-=1

#3. Suma de los primeros 10 números: Usa un while para sumar los números del 1 al 10 e imprimir el resultado.
suma = 0
i=1
while i<=10:
    suma+=i
    i+=1
print(suma)

#4. Solicitar número positivo: Pide al usuario un número y usa un while para seguir pidiendo hasta que ingrese un número positivo.
num = int(input("ingresa un numero positivo "))


while num <=0:
    print("El numero debe ser positivo")
    num = int(input("ingresa un numero positivo "))
else:
    print("el numero es positivo")
    
#5. Menú interactivo: Crea un menú con while que permita al usuario elegir entre opciones (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y solo termine cuando elija la opción de salir.
# Menú interactivo
while True:
    # Mostrar el menú
    print("""  Elige entre estas opciones:
 
    1. Saludar
    2. Despedirse
    3. Salir
    """)
    
    # Solicitar al usuario que elija una opción
    opciones = input("Elige entre estas opciones (1/2/3): ")
    
    # Acción según la opción elegida
    if opciones == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opciones == "2":
        print("¡Adiós! Que tengas un buen día.")
    elif opciones == "3" or opciones.upper() == "SALIR":
        print("¡Hasta luego!")
        break  # Salir del bucle
    else:
        print("Opción no válida, por favor ingresa 1, 2 o 3.")
        
print("Has salido del bucle.")


#6. Adivina el número: Genera un número secreto (puedes usar una variable fija) y usa un while para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor.
# Generamos un número secreto entre 1 y 100
import random

numero_secreto = random.randint(1, 100)

# Pedir al usuario que adivine el número
intentos = 0
while True:
    # Solicitar al usuario que ingrese un número
    intento_usuario = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1  # Contar los intentos

    # Comprobar si el número ingresado es correcto
    if intento_usuario < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    elif intento_usuario > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
        break  # Salir del bucle si el número es correcto
#7. Contar vocales en una palabra: Pide al usuario una palabra y usa un while para contar cuántas vocales tiene.
palabra = input("Ingresa una palabra: ")

# Inicializar variables para contar las vocales
vocales = "aeiouAEIOU"
contador_vocales = 0
i = 0

# Usar un bucle while para recorrer la palabra
while i < len(palabra):
    # Verificar si el caracter actual es una vocal
    if palabra[i] in vocales:
        contador_vocales += 1
    i += 1

# Imprimir el número de vocales
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")


#8. Validar contraseña: Pide al usuario una contraseña y usa un while para seguir pidiendo hasta que ingrese "python123".
while True:
    contraseña = input("Ingresa la contraseña: ")
    
    # Verificar si la contraseña es correcta
    if contraseña == "python123":
        print("¡Acceso permitido!")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")
        
        
        
#9. Sumar hasta detenerse: Pide números al usuario y súmalos hasta que ingrese "0", momento en el que se imprimirá el total.
while True:
    try:
        numero = int(input("Ingresa un número (o ingresa 0 para terminar): "))
        
        if numero == 0:
            break
    
        total += numero
    
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

print(f"La suma total es: {total}")



#10. Número de intentos: Pide al usuario que ingrese un número entre 1 y 10. Si no lo hace, sigue pidiéndolo hasta que lo haga correctamente.
while True:
    try:
        numero = int(input("Ingresa un número entre 1 y 10: "))
        
        # Verificar que el número esté en el rango correcto
        if 1 <= numero <= 10:
            print(f"¡Número {numero} ingresado correctamente!")
            break  # Salir del bucle si el número es correcto
        else:
            print("El número debe estar entre 1 y 10. Intenta de nuevo.")
    
    except ValueError:
        # Si el usuario no ingresa un número válido
        print("Eso no es un número válido. Intenta de nuevo.")
    
    
    
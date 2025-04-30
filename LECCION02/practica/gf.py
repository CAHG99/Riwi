# 1 #Contador de numeros positivos
# contador = 0
# cont = 0

# while contador < 10:
#     num = int(input("Escribe un número: "))
#     contador += 1
#     if num > 0:
#         cont += 1

# print(f"Se han ingresado {cont} números mayores que 0.")


# #2 Sumatoria hasta alcanzar un mínimo
# print("suma de numeros hasta llegar a 100\n")

# num = int(input("Ingresa un 1er número: "))


# while num <= 100: #se ejecuta el ciclo mientras la condicion sea verdadera
#     num2 = int(input("Ingresa un número: "))
#     num += num2
#     print(num)


# 3 generador de tabla de multiplicar
# num = int(input("Escribe un número: "))

# for i in range(1, num+1):
#     resultado = num *i
#     print(f"{num} x {i} = {resultado}")


# 4 contador de intentos
# numeroSecreto = 7
# contador = 0
# intentos = 5

# while contador < intentos:
#     num = int(input("Adivina el número secreto (entre 1 y 10): "))
#     contador += 1
#     if num == numeroSecreto:
#         print("¡Felicidades! Adivinaste el número secreto.")
#         break
#     elif contador == intentos:
#         print("Lo siento, has agotado tus intentos.")
#     else:
#         print("Intenta de nuevo.")


# #5 Vericador de edad
# while True:
#     edad = int(input("Por favor, ingresa tu edad: "))
#     if edad < 18:
#         print("Eres menor de edad,regresa cuando seas mayor.")
#     else:
#         print("Eres mayor de edad, bienvenido.")
#         break


# #6 conteo de numeros pares en un rango
# num1 = int(input("Ingresa un número de inicio: "))
# num2 = int(input("Ingresa un número final: "))
# numPares = []

# for i in range(num1, num2+1):
#     if i % 2 == 0:
#         numPares.append(i)
#     else:
#        continue
# print(f"Los números pares entre {num1} y {num2} son: {numPares}")


# #7 contador de letras "a"
# palabra = input("Por favor, ingresa una palabra: ")
# contador = {}

# for i in palabra.lower():
#     if i in contador:
#         contador[i] += 1
#     else:
#         contador[i] = 1
#     print(contador)


# #8 calculadora de factorial
# num = int(input("Escribe un número para calcular su factorial: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"El factorial de {num} es: {factorial}")


# 9 sumar numeros hasta cancelar
numeros = []
num = (input("Ingresa un número: "))
while True:
    if num == "salir":
        break
    else:
        num = int(num)
        numeros.append(num)
      

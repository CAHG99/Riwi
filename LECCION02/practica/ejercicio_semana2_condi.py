#1. Número positivo, negativo o cero
num = float(input("porfavor, ingresa un numero: "))
if num >0:
    print("el número es positivo") 
elif num == 0:
    print('el numero es cero')
else:
    print("el número es negativo")
    
    
#2. Mayor de dos números    
num1 = float(input("porfavor, ingresa un primer numero: "))
num2 = float(input("porfavor, ingresa un segundo numero: "))
if num1 > num2:
    print(f"el número {num1} es mayor que {num2}") 
elif num1 == num2:
    print('los numeros son iguales')
else:
    print(f"el número {num2} es mayor que {num1}")

#3. Número par o impar
num3 = float(input("por favor, ingresa un primer numero: "))

if num3 % 2 == 0:
    print("el numero es par") 
else:
    print('el numero es impar')
    
    
#4. Aprobado o reprobado
nota = float(input("por favor, ingresa tu nota de 0 a 100: "))

if nota >= 60:
    print("Aprobado") 
else:
    print('Reprobado')
    
    
#5. Edad para votar
edad = input("por favor, ingresa tu edad: ")

if edad >= "18":
    print("Puedes votar") 
else:
    print('No puedes votar')
    

#6. Clasificación por edad
edad = int(input("por favor, ingresa tu edad: "))

if edad > 65:
    print("Eres un adulto mayor") 
elif edad >= 18 or edad == 65:
    print("Eres un adulto")
elif edad < 18:
    print("eres menor de edad")
else:
    print("por favor, ingresa datos valido")
    
    
#7. Divisible entre 3 y 5
num4 = float(input("por favor, ingresa un numero: "))  

if num4 % 3 == 0 and num4 % 5 == 0:
    print("Divisible entre 3 y 5")
elif num4 % 3 == 0:
    print("Divisible solo entre 3")
elif num4 % 5 == 0:
    print("Divisible solo entre 5")
else:
    print("No divisible ni entre 3 ni 5")
    


#8. Calculadora simple
num6 = int(input("por favor, ingresa un prime numero: "))
num7 = int(input("por favor, ingresa un segundo numero: "))
operacion = input("ingresa una operacion: ")

if operacion == "suma":
    print(num6 + num7)
elif operacion == "resta":   
    print(num6 - num7)
elif operacion == "multiplicacion":  
    print(num6 * num7)
elif operacion == "division":  
    print(num6 / num7)
else: 
    print ("ingresa un valor valido")    
    

#9. Comparar contraseñas
clave = input("por favor, ingresa tu clave: ")
clave1 = input("por favor, confirma tu clave: ")

if clave == clave1:
    print("Acceso permitido") 
else: 
    print ("Contraseña incorrecta")


#10. Número dentro de un rango
num8 = float(input("ingresa un numero entre 10 y 20: "))
if 10 <= num8 <= 20:
    print("Dentro del rango") 
else:
    print("Fuera del rango")

try: 
    num1 = int(input("ingresa el primer numero: "))
    num2 = int(input("ingresa el segundo numero: "))
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    if num2 <= 0:
        print("no se puede realizar la division.")         
    else:
        print(num1/num2)
except ValueError:
    print("ingresa un numero valido")        
  
  
    
try:    
    nota = float(input("ingresa tu nota entre 1 y 10: "))
    if 9 <= nota <= 10:
        print("A") 
    elif 7 <= nota < 9:
        print("B")
    elif 5 <= nota < 7:
        print("C")
    elif nota < 5:
        print("F")    
    else:
        print("ingresa una nota valida")
except ValueError:
    print("porfavor, ingresa un numero valido.")
   
    
    
try:    
    num1 = int(input("ingresa un numero: "))
    if num1 % 2 == 0:
        print("el numero es par")
    else: 
        print("el numero es impar")
    if num1 > 10:
        print("el numero es mayor que 10")    
except ValueError:
    print("ingrese un numero valido")
  
  
  
suma = 0

for numero in range (1,101):

    if numero % 2 != 0:
        suma += numero
    
print(f"la suma de los numeros impares entre 1 y 100 es: {suma}")



nom = input("ingresa tu nombre. ")          
ape = input("ingresa tu apellido.")

print(f"{nom}  {ape}")

    

try:    
    num = float(input("ingresa un numero entre 10 y 20: "))
    if 10 <= num <= 20:
        print("l número está en el rango") 
    else:
        print("l número no está en el rango")
except ValueError:
    print("porfavor, ingresa un numero valido.")
 
 
    
try:
    num2 = int(input("ingresa el primer numero: "))
    for i in range (1,num2+1):
        print(i)
except ValueError:
    print("ingresa un numero valido")
  
  
    
try:
    edad = int(input("ingresa tu edad:"))
    print(edad*12)
except ValueError:
    print("Ingresa un numero valido ")
  
  
try:
    fact = int(input("ingresa un numero positivo:"))
    for i in range (1,num1+1):
        fact *= i
except ValueError:
    print("Ingresa un numero valido ")  
  
  
    
try:
    num1 = int(input("ingresa un numero para la base:"))
    num2 = int(input("ingresa un numero para el exponente:"))
    print(num1**num2)
except ValueError:
    print("Ingresa un numero valido ")



try:
    num1 = float(input("ingresa el primer numero positivo:"))
    num2 = float(input("ingresa el segundo numero positivo:"))
    if num1 <= 0 or num2 <= 0:
        print("por favor, ingresa solo numeros positivos")
    else:
        if num1 > num2:
            print(f"el numero mayor es {num1}")
        elif num2 > num1:
            print(f"el numero mayo es {num2}")   
        else:
            print("los numero son iguales") 
except ValueError:
    print("Ingresa un numero valido ")



for i in range (1,11):
    print(i)
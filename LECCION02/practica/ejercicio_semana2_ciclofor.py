1#Contar del 1 al 10
for i in range (1,11):
    print(i)
    


2#Contar hacia atrás:
for i in range (10,0,-1):
    print(i)
    
    
    
3#Sumar los primeros 10 números
suma = 0

for i in range (1,11):
    suma+=i

print(suma)



4#Números pares del 1 al 20:
for i in range (1,21):
    if i % 2 ==0:
        print(i)
        
    
        
5#Detectar múltiplos de 3:
for i in range (1,31):
    if i % 3 ==0:
        print(i)
        
        
            
6#Contar letras "a"
palabra = input("por favor, ingresa una palabra: ")
contador=0

for i in palabra:
    if i == "a":
        contador +=1
        
print(f"la palabra a aparece {contador}")     



7#Tabla de multiplicar del 5
for i in range (1,11):
    resultado = 5*i
    print(f"5x{i} = {resultado}")
   
    

8#Números positivos en una lista
lista= [3,-1,5,-2,7,-8]

for i in lista:
    if i>0:
        print(i)  
        
        
        
9#Mayúsculas y minúsculas:
palabra = input("por favor, ingresa una palabra ")
mayuscula = 0
minuscula = 0

for i in palabra:
    if i.isupper():
        mayuscula+=1
    elif i.islower():
        minuscula+=1
print(f"las letras en mayuscula son {mayuscula}")     
print(f"las letras en mayuscula son {minuscula}") 



10#Simulación de contraseña:

intmax= 3

for i in range (1,intmax+1):
    clave=input("ingresa una contraseña: ")
    if clave == "python123":
        print("Acceso permitido")
        break
    else: 
        if i == intmax:
            print("contraseña incorrecta") 
        else: 
            print("contraseña incorrecta")  


#suma condicional de numeros
suma=0
for i in range(1, 101):
    if i % 3 != 0 and i % 2 != 0:
        suma += i   
          
print(suma)
        
        
#Reemplazar vocales por un simbolo en una palabra 
palabra = input("Escribe una palabra: ")
lista = ["a","e","i","o","u"]
nuevaPalabra = ""

for i in palabra:
    if i.lower() in lista:
        nuevaPalabra += "*"
    else:
        nuevaPalabra += i
        
print(f"la palabra contiene la letra {nuevaPalabra}")
        


#Buscar el caracter mas frecuente en una cadena sin usar collections
letra = input("Escribe una letra: ")
contador = {}

for i in letra:
    if i in contador:
        contador[i] += 1
        print(contador)
    else:
        contador[i] = 1

letra_max = ""
max_repeticiones = 0

for i in contador:
    if contador[i] > max_repeticiones:
        letra_max = i
        max_repeticiones = contador[i]

if letra_max:
    print(f"La letra que más se repite es '{letra_max}' con {max_repeticiones} repeticiones.")
else:
    print("No se ingresaron letras.")



 #Generar una lista de los primeros n numeros primos
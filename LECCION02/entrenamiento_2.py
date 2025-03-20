import os
os.system("clear")

# Variables de control
lista_De_Calificacion = []
calificion = 0
aprobado = 60
suma = 0
indice = 0
count = 0
contador = 0

# Bucle para validar la calificacion especifica
while True:
    try:
        calificacion_Especifica = float(
    input("Por favor, ingresa una nota específica para comparar: "))
        if calificacion_Especifica >= 0:
            print("")
            break
        else:
            print("por favor, ingresa un numero valido. Intente nuevamente.")
    except ValueError:
        print("por favor, ingresa un dato valido.")


# Bucle para ingresar la cantidad de notas
while True:
    try:
        cantidad = int(input("Por favor, ingresa la cantidad de notas: "))
        if cantidad > 0:
            print("")
            break
        else:
            print("la cantidad debe ser un numero mayor que 0. Intente nuevamente.")
    except ValueError:
        print("por favor, ingresa un dato valido.")

# Ingreso de las calificaciones
for i in range(1, cantidad+1):
    while True:
        try:
            calificion = float(
                input(f"Por favor, ingresa tu calificacion #{i} en el rango de 0 a 100: "))
            if 0 <= calificion <= 100:
                lista_De_Calificacion.append(calificion)
                break
            else:
                print(
                    "la cantidad debe ser un numero entre el rango de 0 a 100. Intente nuevamente.")
        except ValueError:
            print("por favor, ingresa un dato valido.")
            
            
# Calcular el promedio de las calificaciones
for i in lista_De_Calificacion:
    suma += i

promedio = suma/len(lista_De_Calificacion)
print(f"Tu promedio es {promedio:.2f}")

# Evaluar si aprobaste o reprobaste
if promedio >= aprobado:
    print(f"Felicitaciones has aprobado con un promedio de {promedio:.2f}")
else:
    print(f"Lo sentimos, has reprobrado con un promedio de {promedio:.2f}")


# Contar las calificaciones mayores a la calificación específica
while indice < len(lista_De_Calificacion):

    if lista_De_Calificacion[indice] > calificacion_Especifica:
        count += 1
    indice += 1
print(
    f"La cantidad de calificaciones que son mayores a {calificacion_Especifica} es {count}")

# Contar cuántas veces aparece la calificación específica
for i in lista_De_Calificacion:
    if calificacion_Especifica == i:
        contador += 1
        continue
    if i < 60:
        break

print(f"La calificación {calificacion_Especifica} aparece {contador} {'veces' if contador > 1 else 'vez'}.")


            


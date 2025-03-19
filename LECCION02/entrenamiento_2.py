lista_De_Calificacion=[]
calificion=0
Aprobado=60

while True:
    try:
        cantidad = int(input("Cuantas calificaciones deseas ingresar: "))
        if cantidad >0:
            print("")
            break
        else:
            print("la cantidad debe ser un numero mayor que 0. Intente nuevamente.")
    except ValueError:
        print("por favor, ingresa un dato valido.")

for i in range(1,cantidad+1):
    while True:
        try:
            calificion = float(input("Por favor, ingresa tu calificacion entre el rango de 0 a 100: "))
            if 0 <= calificion <=100:   
                lista_De_Calificacion.append(calificion)
                break
            else:
                print("la cantidad debe ser un numero entre el rango de 0 a 100. Intente nuevamente.")
        except ValueError:
            print("por favor, ingresa un dato valido.")
    
print(f"Las calificaciones ingresadas son: {lista_De_Calificacion}")      
            


            


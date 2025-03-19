# Función para solicitar una calificación válida
def obtener_calificacion():
    while True:
        try:
            calificacion = float(input("Ingresa una calificación (número entre 0 y 10): "))
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 10. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

# Solicitar una lista de calificaciones
def obtener_lista_calificaciones():
    calificaciones = []
    while True:
        try:
            cantidad = int(input("¿Cuántas calificaciones deseas ingresar? "))
            if cantidad > 0:
                for i in range(cantidad):
                    calificacion = obtener_calificacion()
                    calificaciones.append(calificacion)
                break
            else:
                print("La cantidad debe ser un número mayor que 0. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número entero para la cantidad.")
    
    return calificaciones

# Función para comparar calificaciones
def comparar_calificaciones(lista_calificaciones, valor):
    mayores = [calif for calif in lista_calificaciones if calif > valor]
    menores = [calif for calif in lista_calificaciones if calif < valor]
    
    print(f"Calificaciones mayores que {valor}: {mayores}")
    print(f"Calificaciones menores que {valor}: {menores}")
    print(f"Calificaciones iguales a {valor}: {[calif for calif in lista_calificaciones if calif == valor]}")

# Ingreso de datos
calificaciones = obtener_lista_calificaciones()

# Solicitar el valor específico para comparar
while True:
    try:
        valor_comparar = float(input("Ingresa un valor para comparar con las calificaciones: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor ingresa un número.")

# Comparar las calificaciones con el valor dado
comparar_calificaciones(calificaciones, valor_comparar)

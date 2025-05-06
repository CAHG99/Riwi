# 1. Calculadora de Notas Estudiantiles
# def validation(average):
#     if average >= 3:
#         print(
#             f"Felicidades {name}, has aprobado con un promedio de {promedio:.2f}")
#     else:
#         print(
#             f"Lo siento {name}, has reprobado con un promedio de {promedio:.2f}")


# name = input("Por favor, ingresa tu nombre: ")
# subjects = int(input("Por favor, ingresa la cantidad de materias: "))
# califications = []

# for i in range(subjects):
#     subject = input(f"Ingrese el nombre de la materia {i+1}: ")
#     calification = float(
#         input(f"Ingrese la calificación entre 0 y 5  de {materia} {i+1}: "))
#     califications.append(calification)
# promedio = sum(calification) / len(califications)
# validations(average)

# Sistema de Pedido en Cafetería
def buscar_producto(nombre):
    for producto in menu:
        if producto['nombre'].lower() == nombre.lower():
            return producto['precio']
    return None  # Si no se encuentra el producto


def descuento(total):
    if total > 50:
        total = total - (total * 0.10)
        print(f"El total de tu pedido con descuentro es: ${total}")
    else:
        print(f"No se aplico un descuento, el total de tu pedido es: ${total}")


menu = [{"nombre": "Cafe", "precio": "4"},
        {"nombre": "Te", "precio": "3"},
        {"nombre": "Pastel", "precio": "5"},
        {"nombre": "Galleta", "precio": "2"},
        {"nombre": "Sandwich", "precio": "6"}]

cantidad = int(input("¿Cuántos productos deseas pedir? "))
total = 0

for i in range(1, cantidad+1):
    nombre = input(f"Por favor, ingresa el nombre del {i} producto: ")
    cant = int(input(f"¿Cuántas unidades de {nombre} deseas? "))
    precio = buscar_producto(nombre)
    cuenta = precio * cant
    total += cuenta


descuento(total)

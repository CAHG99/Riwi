# Lista de productos
productos = [
    {"nombre": "Producto1", "precio": 100, "cantidad": 50},
    {"nombre": "Producto2", "precio": 200, "cantidad": 30},
    {"nombre": "Producto3", "precio": 150, "cantidad": 70}
]

# Función para buscar un producto por nombre
def buscar_producto(nombre):
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():  # Comparación insensible a mayúsculas/minúsculas
            return producto['precio'], producto['cantidad']
    return None  # Si no se encuentra el producto

# Solicitar al usuario que ingrese el nombre del producto
nombre = input("Por favor, ingresa el nombre del producto: ")

# Buscar el producto
resultado = buscar_producto(nombre)

if resultado:
    precio, cantidad = resultado
    print(f'Producto encontrado: {nombre}')
    print(f'Precio: ${precio}')
    print(f'Cantidad disponible: {cantidad}')
else:
    print(f'No se encontró el producto: {nombre}')


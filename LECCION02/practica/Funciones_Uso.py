import os
os.system("clear")

def pedir_numero(mensaje, tipo=float, condicion=lambda x: True, error="Valor inválido."):
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("No puedes dejar el campo vacío.")
            continue
        try:
            valor = tipo(entrada)
            if condicion(valor):
                return valor
            else:
                print(error)
        except ValueError:
            print("Ingresa un número válido.")
            
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("El nombre del producto no puede estar vacío.")


compras = []
                  
while True:
    # Usamos la función para pedir cada dato
    nombre = pedir_texto(
        "Ingresa el nombre del productos :"
        )
    
    cantidad = pedir_numero(
        "Ingresa la cantidad de productos adquiridos: ",
        tipo=int,
        condicion=lambda x: x > 0,
        error="La cantidad debe ser un número mayor que 0."
    )
    
    precio = pedir_numero(
        "Ingresa el precio unitario: ",
        tipo=float,
        condicion=lambda x: x > 0,
        error="El precio debe ser un número mayor que 0."
    )

    descuento = pedir_numero(
        "Ingresa el porcentaje de descuento que se aplicará: ",
        tipo=float,
        condicion=lambda x: 0 <= x <= 100,
        error="El descuento debe estar entre 0 y 100."
    )

    # Cálculo final
    total = cantidad * precio * (1 - descuento / 100)
    print(f"El total a pagar es: ${total:,.2f}")

  # Guardar en historial
    compra = {
        "nombre":nombre,
        "cantidad": cantidad,
        "precio": precio,
        "descuento": descuento,
        "total": total
    }
    compras.append(compra)
    
    # Preguntar si quiere hacer otro cálculo
    otra_vez = input("¿Deseas calcular otra compra? (s/n): ").strip().lower()
    if otra_vez != "s":
        print("\nResumen de compras realizadas:\n")
        for i, compra in enumerate(compras, 1):
            resumen = (
                f"Compra {i}:\n"
                f"nombre {compra['nombre']}\n"
                f"Cantidad: {compra['cantidad']}\n"
                f"Precio unitario: ${compra['precio']:,.2f}\n"
                f"Descuento: {compra['descuento']}%\n"
                f"Total: ${compra['total']:,.2f}\n"
                )
            print(resumen)
        break
        
 










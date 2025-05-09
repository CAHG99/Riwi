stock = [
    {"detergente": (10000, 40)},
    {"esponja": (5000, 25)},
    {"olla": (80000, 20)},
    {"papel": (20000, 22)},
    {"shampoo": (18000, 12)},
    {"aspiradora": (350000, 3)},
    {"refrigerador": (1200000, 2)},
    {"sarten": (40000, 8)},
    {"tostadora": (45000, 4)},
    {"microonda": (250000, 2)},
    {"sofa": (800000, 3)},
    {"ventilador": (120000, 6)},
]

def addProduct(name, price, amount):
    for product in stock:
        if name in product:
            price, amount = product[name]
            print(
                f"El producto '{name}' ya existe en el inventario.")
            return product
    else:
        newProduct = {name: (price, amount)}
        stock.append(newProduct)
        print(f"Producto agregado: {newProduct}")
        return


def searchProduct(name, list_products):
    for product in list_products:
        nameReal = next(iter(product))
        if nameReal.lower() == name:
            price, amount = product[nameReal]
            print(f"\nProducto encontrado: {nameReal}")
            print(f"Precio: ${price}")
            print(f"cantidad: {amount} unidades")
            return product
    else:
        print("Producto no encontrado.")
        return


def updatePrice(name, nprice):
    for product in stock:
        if name in product:
            precio, amount = product[name]
            product[name] = (nprice, amount)
            print(
                f"El producto '{name}'fue modificado.")
            return product
    else:
        print(f"Producto no encontrado {name}")
        return


def removeProduct(name):
    for i, product in enumerate(stock):
        if name in product:
            del stock[i]
            print(f"Producto '{name}' eliminado del inventario.")
            return product
    print(f"El producto '{name}' no fue encontrado en el inventario.")


def calculationProduct(listInve):
    totalValue = sum(
        (lambda price, amount: price *
         amount)(*list(product.values())[0])
        for product in listInve
    )
    print(f"Valor total del inventario: ${totalValue}")


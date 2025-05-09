from main import stock, name

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


def searchProduct(list_products):
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


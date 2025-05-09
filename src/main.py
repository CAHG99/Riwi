from menu import menu
from inventory import *
from utils import validation, requestText

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
bool = True

while bool:
    menu()
    operation = input("Elige la operacion que desea realizar: ")

    match operation:
        case "1":
            name = requestText(
                "\nPor favor, ingresa el nombre del producto: ")

            price = validation("\nPor favor, ingresa un precio: ",
                               float,
                               lambda x: x > 0,
                               "\n📚 Por favor, ingresa un número válido.")

            amount = validation("\nPor favor,ingresa una cantidad: ",
                                float,
                                lambda x: x > 0,
                                "\n📚 Por favor, ingresa un número válido.")

            addProduct(name, price, amount)

        case "2":
            print("")
            for i, p in enumerate(stock, start=1):
                for inde in p:
                    print(f"{i}. {inde}")
            name = requestText(
                "\nPor favor, ingresa el nombre del producto que deseas consultar: ")

            searchProduct(stock)

        case "3":
            name = requestText(
                "\nPor favor, ingresa el nombre del producto que deseas actualizar: ")

            price = validation("\nPor favor, ingresa un precio: ",
                               float,
                               lambda x: x > 0,
                               "\n📚 Por favor, ingresa un número válido.")

            updatePrice(name, price)

        case "4":
            name = requestText(
                "\nPor favor, ingresa el nombre del producto que deseas eliminar: ")
            removeProduct(name)

        case "5":
            for i, p in enumerate(stock, start=1):
                name = list(p.keys())[0]
                value = list(p.values())[0]
                print(
                    f"{i}.{name:<12} Precio:{value[0]:<12} Cantidad:{value[1]:<12}")
            calculationProduct(stock)

        case "6":
            print("\nRegresa pronto")
            bool = False
        case _:
            print("\nPor favor, ingresa un dato valido")
            bool = True
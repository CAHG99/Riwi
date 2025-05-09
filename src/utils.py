def validation(menssage, type=float, condition=lambda x: x > 0, bug="El valor no es válido"):
    while bool:
        try:
            value = type(input(menssage))
            if condition(value):
                return value
            else:
                print(bug)
        except ValueError:
            print("Ingresa un número válido.")


def requestText(menssage):
    while bool:
        text = input(menssage).strip()
        if text:
            return text
        else:
            print("El nombre del producto no puede estar vacío.")


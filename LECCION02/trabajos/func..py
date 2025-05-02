def validation ( menssage, type = float, condition = lambda x: x > 0, bug = "El valor no es válido"):
    while True:
        try:
            value = type(input(menssage))
            if condition(value):
                return value
            else:
                print(bug)
        except ValueError:
            print("Ingresa un número válido.")
 
 
 
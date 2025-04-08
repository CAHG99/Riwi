#No se recomienda usar una variable global

saludo = 25


def saludar():
    global saludo
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "hola chanchito"
    print(saludo)


resultado1 = saludo +3
print(resultado1)
saludar()
resultado2 = saludo +3
print(resultado2)

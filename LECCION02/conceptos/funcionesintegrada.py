# print

print("¿Sigue", [0, 1, 1, 2, 3, 5], "la sucesión de Fibonacci?", end=" R: ")
print("No lo sé", "No me importa", sep=" y ")

print("F", "i", "b", "o", "n", "a", "c", "c", "i", sep="", end=": ")
print(0, 1, 1, 2, 3, 5, sep=", ", end=", ...")

# input

variable = input("Escriba su nombre: ")
print(variable + ", eres una persona de dudosa inteligencia.")


# type

print(type("Palabra"))
print(type(3))
print(type(2.3))
print(type(True))
print(type([]))
print(type(()))
print(type({0}))
print(type({}))

# list tuple set dict
lista = list((1, 2, 3))
tupla = tuple((1, 2, 3))
conjunto = set((1, 2, 3))
diccionario = dict((("Uno", 1), ("Dos", 2), ("Tres", 3)))

print(lista, type(lista))
print(tupla, type(tupla))
print(conjunto, type(conjunto))
print(diccionario, type(diccionario))

print(list("Deletrea"))
print(dict(Uno=1, Dos=2, Tres=3))

# pow round

print("El valor absoluto de -3:", abs(-3))
print("Potencia 2^3:", pow(2, 3))

print("Redondeo de 10.50:", round(10.50))
print("Redondeo de 10.51:", round(10.51))

print("Redondeo de 10.55 con 0 cifras decimales:", round(10.55, 0))
print("Redondeo de 10.55 con 1 cifra decimal:", round(10.55, 1))
print("Redondeo de 10.55 con 2 cifras decimales:", round(10.55, 2))

# sum max min
print("Suma lista:", sum(list((1, 2, 3))))
print("Suma tupla:", sum(tuple((1, 2, 3))))
print("Suma conjunto:", sum(set((1, 2, 3))))
print("Suma diccionario:", sum(dict(((1, "Uno"), (2, "Dos"), (3, "Tres")))))

print("Máximo:", max(list((1, 2, 3))))
print("Mínimo:", min(set((1, 2, 3))))

# len sorted

lista = [2, 1, 4, 3]
diccionario = {"Clave_1": "Valor_1", "Clave_2": "Valor_2"}

print("El tamaño de la lista es:", len(lista))
print("El tamaño del diccionario es:", len(diccionario))

print("Lista ordenada", sorted(lista))
print("Lista ordenada inversa:", sorted(lista, reverse=True))


# range enumerate zip

print(list(range(2, 5)))

print(list(enumerate(["Uno", "Dos", "Tres"], start=2)))

print(list(zip([1, 2, 3], ["Uno", "Dos", "Tres", "Cuatro"])))
usuarios = [
    ["chancho", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# nombres = [expresion for item in items:]

#Transformar-map
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Filtrar-filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

#Filtrar y Transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# # print(nombres)

# nombres = list(map(lambda usuario: usuario [0], usuarios))
# print(nombres)

menos_Usuarios = list(filter(lambda usuario: usuario [1] > 2, usuarios))
print(menos_Usuarios)
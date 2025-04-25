numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()
# print(numeros)

# numeros.sort(reverse=True)
# print(numeros)

# numeros2 = sorted(numeros, reverse=True)
# print(numeros2)                                                 

# numeros2 = sorted(numeros)
# sorted(numeros)
# print(numeros)
# print(numeros2)


# usuarios = [
#     [4,"chancho"],
#     [2,"felipe"],
#     [5, "pulga"]
#     ]
     
# usuarios.sort()
# print(usuarios)

usuarios = [
    ["chancho",4],
    ["felipe",1],
    ["pulga",5]
    ]

def ordena(elemento):
    return elemento[1]
     
usuarios.sort(key=ordena)
print(usuarios)

# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)

# usuarios.sort(key=lambda el:el[1],reverse=True)
# print(usuarios)  
     

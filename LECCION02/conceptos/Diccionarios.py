punto = {"x": 25,
         "y": 50
         }

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto,punto["lala"])
if "lala" in punto:
    print("encontre lala",punto["lala"])
    
print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

# for valor in punto:
#     print (valor)
for valor in punto:
    print (valor, punto[valor]) #acceder al valor del diccionario
    
# for valor in punto.items(): #acceder tanto al diccionario como a su valor
#     print(valor)

for llave, valor in punto.items(): #acceder tanto al diccionario como a su valor pero desempaquetando listas
    print(llave, valor)
    
usuarios = [
    {"id":1, "nombre": "chancho"},
    {"id":2, "nombre": "feliz"},
    {"id":3, "nombre": "nico"},
    {"id":4, "nombre": "felipe"},
    
]

for usuario in usuarios:
    print(usuario["nombre"])
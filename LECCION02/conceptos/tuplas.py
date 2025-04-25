#Las tuplas no son mutables

numeros = (1,2,3) + (4,5,6)
print(numeros)

punto = tuple([1,2])
print(punto)
menos_Numeros = numeros[:2]
print(menos_Numeros)
primero, segundo, *otros = numeros
print(primero,segundo,otros)
for n in numeros:
    print(n)

lista_Numero = list(numeros)
lista_Numero[0]= "chancho"
print(lista_Numero)

letra = input("Escribe una letra: ")
contador = {}

for i in letra:
    if i in contador:
        contador[i] += 1
        print(contador)
    else:
        contador[i] = 1

letra_max = ""
max_repeticiones = 0

for i in contador:
    if contador[i] > max_repeticiones:
        letra_max = i
        max_repeticiones = contador[i]

if letra_max:
    print(f"La letra que más se repite es '{letra_max}' con {max_repeticiones} repeticiones.")
else:
    print("No se ingresaron letras.")

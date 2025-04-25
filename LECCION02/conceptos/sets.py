# set significa grupo o conjuntos
# primer = {1,1,2,2,3,4}
# primer.add(5)
# primer.remove(1)
# print(primer)

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
# print(primer | segundo) Operador union,devuelve el primer set y el segundo set sin agregar duplicados
# print(primer & segundo) Operador intercepcion, devuelve  elementos en comun entre el primer y segundo set
# print(primer - segundo) Operador diferencia, elimina elementos que se encuentren repetidos en el segundo set con respecto al primero
# print(primer ^ segundo) Operador diferencia simetrica, devuelve elementos que no se repiten entre los 2 set

if 5 in segundo:
    print("Hola mundo")
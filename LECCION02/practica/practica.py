list_3 = []
list_5 = []
list_all = []

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        list_all.append(i)
        
    elif i % 3 == 0:
        list_3.append(i)

    elif i % 5 == 0:
        list_5.append(i)


print(f"multiplos de 3 => 'Fizz'{list_3}")
print(f"multiplos de 5 => 'Buzz'{list_5}")
print(f"multiplos de 3 y 5 => 'fizzbuzz' {list_all}")


Palabra = input("ingresa una palabra: ")
np = ""
np2 = ""

for i in Palabra:
    if i != " ":
        np += i
        
for i in np:
    np2 = i + np2

print(np2)
        
if np.lower() == np2.lower():
    print(f"{np} Es palindromos")
else:
    print(f"{np} no es palindromos")
    
    
n =4
n2 = 6
n3 = 15

if n > n2 and n > n3:
    print(f"el numero  mayor es este {n}")
elif n2 > n and n2 > n3:
    print(f"el numero  mayor es este {n2}")
else:
    print(f"el numero  mayor es este {n3}")

n = 2


if n == 2 : 
    print(f"el numero {n} es primo ")
elif n % 2 == 0:
    print(f"el numero {n} no es primo ") 
else:
    print(f" El numero {n}  es primo")



palabra = "celular"
Vocales = ["a", "e" , "i" , "o" ,"u"]
contador = 0

for i in palabra:
    if i in list(Vocales):    
        contador += 1
        
print(contador) 

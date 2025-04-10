palabra = "astronomia"
Vocales = ["a", "e" , "i" , "o" ,"u"]
contador = 0

for i in palabra:
    if i in list(Vocales):    
        contador += 1
        
print(contador) 

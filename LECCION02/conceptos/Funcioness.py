def no_space(texto):
    nuevo_Texto = ""
    for i in texto:
        if i != " ":
            nuevo_Texto += i
    return nuevo_Texto

def reverse (texto):
    texto_al_reves = ""
    for i in texto:
        texto_al_reves = i + texto_al_reves
    return texto_al_reves
    
    
     

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()
    
print("amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo")) 
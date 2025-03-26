print("Hola, buen dia, bienvenido a su cajero")

print("""Hola que quieres hacer hoy?
                
1. Ingresar dinero
2. Retirar dinero"
3. Transacion
4. Cambiar clave

""")

usuario = input("")

if usuario == "Ingresar dinero" or usuario == "1":
    print("Monto a ingresar")
elif usuario == "Retirar dinero" or usuario == "2":
    print("Monto a retirar")
elif usuario == "Transacion"  or usuario ==  "3":
    print("Monto a transferir")
elif usuario == "Cambiar clave" or usuario == "4":
    print("porfavor ingresa una clave nueva")
else:
    print ("operacion incorrecta, ingresa nuevamente")


  #ingresar, retirar, transacion, cambiar clave

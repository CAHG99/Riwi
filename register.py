users = []

username = input('Ingresar su usuario: ')
password = input('Ingrese su contraseña: ')

def register_user(username, password, users):
    users.append({ 'user': username, 'password': password })

register_user(username,password, users)

print(users)
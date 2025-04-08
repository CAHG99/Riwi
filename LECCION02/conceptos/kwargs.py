import os
os.system("clear")


def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="id", 
            name="iphone", 
            Desc="esto es un iphone")

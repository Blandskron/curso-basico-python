# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, Mundo\n")
    archivo.write("Bienvenido a Python.")

# Leer desde un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
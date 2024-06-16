# Lectura de archivo
try:
    with open("datos.txt", "r") as archivo_entrada:
        contenido = archivo_entrada.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")

# Escritura en archivo
with open("resultados.txt", "w") as archivo_salida:
    archivo_salida.write("Estos son los resultados obtenidos.\n")
    archivo_salida.write("Segunda línea de texto.")
    archivo_salida.write("\nTercera línea añadida.\n")
    archivo_salida.write("¡Fin!")

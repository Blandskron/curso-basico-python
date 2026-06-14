# Conteo de líneas en un archivo
nombre_archivo = "ejemplo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        cantidad_lineas = len(lineas)
        print(f"El archivo '{nombre_archivo}' tiene {cantidad_lineas} líneas.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")

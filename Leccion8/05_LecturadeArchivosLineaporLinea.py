# Lectura de archivo línea por línea
nombre_archivo = "datos.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            print(linea.strip())  # strip() elimina espacios en blanco al inicio y final de la línea
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

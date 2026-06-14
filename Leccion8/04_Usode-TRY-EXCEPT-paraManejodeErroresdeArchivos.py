# Uso de try-except para manejo de errores de archivo
nombre_archivo = "datos.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except PermissionError:
    print(f"No tienes permisos para abrir el archivo '{nombre_archivo}'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

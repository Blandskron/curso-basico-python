# Uso de la librería os
import os

# Obtener el directorio actual de trabajo
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar archivos y directorios en el directorio actual
contenido_directorio = os.listdir()
print("Contenido del directorio actual:")
for item in contenido_directorio:
    print(item)

### Ejemplo 1: Entrada de Usuario y Salida en Consola

```python
# Entrada de usuario y salida en consola
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print(f"Hola, {nombre}! Tu edad es {edad} años.")
```

En este ejemplo, el programa solicita al usuario que ingrese su nombre y edad, luego imprime un mensaje personalizado utilizando f-strings para formatear la salida.

### Ejemplo 2: Lectura y Escritura de Archivos

#### Lectura de Archivo

```python
# Lectura de archivo
try:
    with open("datos.txt", "r") as archivo_entrada:
        contenido = archivo_entrada.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
```

En este ejemplo, el programa intenta abrir y leer el archivo "datos.txt". Si el archivo no existe, maneja la excepción `FileNotFoundError` e imprime un mensaje indicando que el archivo no está presente.

#### Escritura en Archivo

```python
# Escritura en archivo
with open("resultados.txt", "w") as archivo_salida:
    archivo_salida.write("Estos son los resultados obtenidos.\n")
    archivo_salida.write("Segunda línea de texto.")
    archivo_salida.write("\nTercera línea añadida.\n")
    archivo_salida.write("¡Fin!")
```

En este ejemplo, el programa abre el archivo "resultados.txt" en modo escritura (`'w'`) y escribe varias líneas de texto. Cada llamada a `write()` agrega una nueva línea al archivo.

### Ejemplo 3: Manipulación de Archivos con Iteración

#### Conteo de Líneas en un Archivo

```python
# Conteo de líneas en un archivo
nombre_archivo = "ejemplo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        cantidad_lineas = len(lineas)
        print(f"El archivo '{nombre_archivo}' tiene {cantidad_lineas} líneas.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
```

En este ejemplo, el programa intenta abrir el archivo "ejemplo.txt" para contar el número de líneas que contiene. Utiliza `readlines()` para obtener una lista de todas las líneas y luego calcula la longitud de la lista para determinar el número de líneas.

### Ejemplo 4: Uso de `try-except` para Manejo de Errores de Archivo

```python
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
```

En este ejemplo, el programa utiliza `try-except` para manejar posibles errores al intentar abrir y leer el archivo "datos.txt". Puede manejar errores específicos como `FileNotFoundError` y `PermissionError`, y también captura cualquier otro tipo de excepción genérica usando `Exception`.

### Ejemplo 5: Lectura de Archivo Línea por Línea

```python
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
```

En este ejemplo, el programa lee el archivo "datos.txt" línea por línea usando un bucle `for`. Cada línea se imprime después de eliminar los espacios en blanco al inicio y al final con `strip()`.

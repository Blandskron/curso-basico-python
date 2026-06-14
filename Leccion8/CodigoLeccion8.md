# Guía Práctica de Código: Lección 8 (Entrada y Salida / Archivos)

Esta guía detalla los scripts prácticos correspondientes a la **Lección 8**, orientados a interactuar con consolas y realizar lectura/escritura de archivos planos de texto en disco.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_EntradadeUsuariosySalidaenConsola.py` | Interactividad básica y personalización de print | `python 01_EntradadeUsuariosySalidaenConsola.py` |
| `02_LecturayEscrituradeArchivos.py` | Apertura básica de archivos (modos `w` y `r`) | `python 02_LecturayEscrituradeArchivos.py` |
| `03_ManipulaciondeArchivosconIteracion.py` | Escritura de arreglos de datos en archivos | `python 03_ManipulaciondeArchivosconIteracion.py` |
| `04_Usode-TRY-EXCEPT-paraManejodeErroresdeArchivos.py` | Control de errores al abrir archivos inexistentes | `python 04_Usode-TRY-EXCEPT-paraManejodeErroresdeArchivos.py` |
| `05_LecturadeArchivosLineaporLinea.py` | Lectura eficiente de archivos grandes | `python 05_LecturadeArchivosLineaporLinea.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Entrada de Usuario y Salida en Consola (`01_EntradadeUsuariosySalidaenConsola.py`)
```python
# Entrada de datos
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

# Salida formateada
print("Hola,", nombre, "tienes", edad, "años.", sep=" - ", end="\n\n")
print("Fin de la sección.")
```
* **Explicación:** Se capturan los datos. Usamos el parámetro `sep` para definir que las comas del print se representen con `" - "` en lugar del espacio convencional y un final de impresión con doble salto de línea `end="\n\n"`.
* **Salida:** *(Con entradas "Bastian" y 24)*
  ```text
  Introduce tu nombre: Bastian
  Introduce tu edad: 24
  Hola, - Bastian - tienes - 24 - años.

  Fin de la sección.
  ```

---

### Ejemplo 2: Lectura y Escritura de Archivos (`02_LecturayEscrituradeArchivos.py`)
```python
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, Mundo\n")
    archivo.write("Bienvenido a la programación en Python.")

# Leer desde un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
```
* **Explicación:** El bloque `with` asegura el guardado de los cambios y el cierre inmediato del archivo `ejemplo.txt`.

---

### Ejemplo 3: Manipulación de Archivos con Iteración (`03_ManipulaciondeArchivosconIteracion.py`)
```python
lineas = ["Primera línea de datos\n", "Segunda línea de datos\n", "Tercera línea de datos\n"]

# Escribir una lista de líneas en lote
with open("iteracion.txt", "w") as archivo:
    archivo.writelines(lineas)

print("Datos escritos correctamente.")
```
* **Explicación:** El método `.writelines()` recibe un iterable (como una lista) y escribe secuencialmente cada elemento de texto en el archivo.

---

### Ejemplo 4: Uso de `try-except` para Manejo de Errores de Archivos (`04_Usode-TRY-EXCEPT-paraManejodeErroresdeArchivos.py`)
```python
nombre_archivo = "archivo_inexistente.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se pudo encontrar en el disco.")
```
* **Explicación:** Protege la ejecución del programa contra fallos inesperados. Al buscar un archivo que no existe en el sistema local, el error `FileNotFoundError` es capturado y tratado en el bloque `except`.
* **Salida:**
  ```text
  Error: El archivo 'archivo_inexistente.txt' no se pudo encontrar en el disco.
  ```

---

### Ejemplo 5: Lectura de Archivos Línea por Línea (`05_LecturadeArchivosLineaporLinea.py`)
```python
# Escribir contenido inicial
with open("lineas.txt", "w") as archivo:
    archivo.write("Línea A\nLínea B\nLínea C\n")

# Iterar sobre el objeto archivo línea por línea
with open("lineas.txt", "r") as archivo:
    print("Lectura iterada:")
    for linea in archivo:
        # Usamos strip() para no duplicar los saltos de línea \n
        print("-", linea.strip())
```
* **Explicación:** Iterar directamente sobre el objeto `archivo` con un bucle `for` lee el contenido línea por línea bajo demanda, evitando cargar todo el archivo completo en la memoria RAM (una práctica recomendada para archivos de gran volumen).
* **Salida:**
  ```text
  Lectura iterada:
  - Línea A
  - Línea B
  - Línea C
  ```

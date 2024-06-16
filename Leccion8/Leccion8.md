## Lección 8: Entrada y Salida

### 1. Entrada de Usuario

#### Objetivos
- Aprender cómo recibir datos del usuario durante la ejecución de un programa.
- Utilizar la función `input()` para capturar datos desde el teclado.

#### Función `input()`
- La función `input()` permite al usuario ingresar datos desde la consola.
- Retorna una cadena de texto que puede ser asignada a una variable.

```python
# Ejemplo de entrada de usuario
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")
```

### 2. Salida de Datos en Consola

#### Objetivos
- Comprender cómo imprimir datos en la consola para interactuar con el usuario.
- Utilizar la función `print()` para mostrar información formateada y resultados.

#### Función `print()`
- La función `print()` es utilizada para mostrar datos en la consola.
- Puede imprimir múltiples valores y realizar formateo básico.

```python
# Ejemplo de salida en consola
edad = 25
print("La edad es:", edad)
```

### 3. Archivos: Lectura y Escritura

#### Objetivos
- Explorar cómo interactuar con archivos para leer y escribir datos.
- Utilizar los modos de apertura de archivos en Python.

#### Lectura de Archivos
- Para abrir y leer un archivo en Python, se usa el modo `'r'`.

```python
# Ejemplo de lectura de archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

#### Escritura en Archivos
- Para escribir en un archivo, se usa el modo `'w'` (crea uno nuevo) o `'a'` (añade al final).

```python
# Ejemplo de escritura en archivo
with open("salida.txt", "w") as archivo_salida:
    archivo_salida.write("Datos escritos en el archivo.")
```

### Ejemplos de Código

#### Ejemplo 1: Entrada de Usuario y Salida en Consola

```python
# Entrada de usuario y salida en consola
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print(f"Hola, {nombre}! Tu edad es {edad} años.")
```

#### Ejemplo 2: Lectura y Escritura de Archivos

```python
# Lectura de archivo
with open("datos.txt", "r") as archivo_entrada:
    contenido = archivo_entrada.read()
    print("Contenido del archivo:")
    print(contenido)

# Escritura en archivo
with open("resultados.txt", "w") as archivo_salida:
    archivo_salida.write("Estos son los resultados obtenidos.")
    archivo_salida.write("\nSegunda línea de texto.")
```

### Resumen y Tareas

- Hoy aprendiste sobre cómo interactuar con la entrada y salida en Python.
- Practicaste la captura de datos del usuario, la impresión de información en consola y la manipulación de archivos.
- **Tarea:** Crea un programa que:
  1. Pida al usuario que ingrese su dirección de correo electrónico y lo imprima.
  2. Lea un archivo de texto existente y cuente cuántas líneas contiene.
  3. Escriba una lista de nombres en un archivo nuevo, cada nombre en una línea.

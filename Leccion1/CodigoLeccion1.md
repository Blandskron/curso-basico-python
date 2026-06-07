# Guía Práctica de Código: Lección 1 (Introducción y Vista Rápida)

Esta guía contiene los ejemplos prácticos correspondientes a la **Lección 1**. En esta lección inicial se presenta una vista rápida ("cheat sheet") de las diferentes capacidades de Python que se explorarán a fondo a lo largo del curso.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_HolaMundo.py` | Salida básica de texto | `python 01_HolaMundo.py` |
| `02_OperacionesAritmeticas.py` | Cálculos numéricos elementales | `python 02_OperacionesAritmeticas.py` |
| `03_UsodeVariables.py` | Almacenamiento y reuso de datos | `python 03_UsodeVariables.py` |
| `04_EntradadeUsuario.py` | Interactividad básica (`input`) | `python 04_EntradadeUsuario.py` |
| `05_CondicionalesBasicos.py` | Estructura de toma de decisiones (`if/else`) | `python 05_CondicionalesBasicos.py` |
| `06_CiclosBasicos.py` | Bucles iterativos (`for` y `while`) | `python 06_CiclosBasicos.py` |
| `07_ListasBasicas.py` | Manipulación de colecciones ordenadas | `python 07_ListasBasicas.py` |
| `08_FuncionesBasicas.py` | Creación de bloques reutilizables | `python 08_FuncionesBasicas.py` |
| `09_ManejodeCadenas.py` | Métodos esenciales de texto | `python 09_ManejodeCadenas.py` |
| `10_ManejodeArchivosBasicos.py` | Lectura y escritura en disco | `python 10_ManejodeArchivosBasicos.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Hola, Mundo (`01_HolaMundo.py`)
Muestra cómo desplegar texto básico en la terminal del sistema.

```python
# Este es tu primer programa en Python
print("Hola, Mundo")
```
* **Explicación:** La función `print()` envía la cadena de caracteres literal `"Hola, Mundo"` a la pantalla.
* **Salida en consola:**
  ```text
  Hola, Mundo
  ```

---

### Ejemplo 2: Operaciones Aritméticas (`02_OperacionesAritmeticas.py`)
Introduce los operadores aritméticos básicos nativos de Python.

```python
# Suma
print(5 + 3)

# Resta
print(10 - 4)

# Multiplicación
print(7 * 2)

# División
print(8 / 2)
```
* **Explicación:** Python evalúa las expresiones matemáticas dentro de los paréntesis y luego imprime el resultado final numérico. Observa que el resultado de la división (`8 / 2`) es un flotante (`4.0`).
* **Salida en consola:**
  ```text
  8
  6
  14
  4.0
  ```

---

### Ejemplo 3: Uso de Variables (`03_UsodeVariables.py`)
Uso de etiquetas de almacenamiento para reutilizar valores en memoria.

```python
# Definición de variables
nombre = "Juan"
edad = 25

# Uso de variables
print("Nombre:", nombre)
print("Edad:", edad)

# Operaciones con variables
edad_futura = edad + 5
print("Edad en 5 años:", edad_futura)
```
* **Explicación:** Se asignan valores a las variables `nombre` y `edad`. Luego se concatenan automáticamente en la salida de `print` separados por un espacio, y se realiza una operación matemática utilizando la variable de tipo entero.
* **Salida en consola:**
  ```text
  Nombre: Juan
  Edad: 25
  Edad en 5 años: 30
  ```

---

### Ejemplo 4: Entrada de Usuario (`04_EntradadeUsuario.py`)
Interactividad en la consola para capturar datos externos.

```python
# Pedir el nombre del usuario
nombre_usuario = input("¿Cómo te llamas? ")

# Saludar al usuario
print("Hola, " + nombre_usuario + "! Bienvenido a Python.")
```
* **Explicación:** La función `input()` suspende la ejecución hasta que el usuario teclea su entrada y pulsa Enter. Devuelve el texto capturado como una cadena. Usamos el operador `+` para unir (concatenar) las partes del texto.
* **Salida en consola:** *(Dependerá de lo ingresado por el usuario)*
  ```text
  ¿Cómo te llamas? Bastian
  Hola, Bastian! Bienvenido a Python.
  ```

---

### Ejemplo 5: Condicionales Básicos (`05_CondicionalesBasicos.py`)
Bifurcaciones de código basadas en la veracidad de condiciones lógicas.

```python
# Pedir una edad al usuario
edad = int(input("¿Cuántos años tienes? "))

# Usar una estructura condicional
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```
* **Explicación:** Dado que `input()` siempre devuelve texto, usamos la función `int()` para convertir la cadena a un número entero. Si la comparación lógica de la línea 5 resulta verdadera (`True`), se ejecuta la primera indentación; de lo contrario, se ejecuta la sección `else`.
* **Salida en consola:**
  ```text
  ¿Cuántos años tienes? 20
  Eres mayor de edad.
  ```

---

### Ejemplo 6: Ciclos Básicos (`06_CiclosBasicos.py`)
Automatización de operaciones repetitivas.

```python
# Bucle for
print("Números del 1 al 5 usando for:")
for i in range(1, 6):
    print(i)

# Bucle while
print("Números del 1 al 5 usando while:")
i = 1
while i <= 5:
    print(i)
    i += 1
```
* **Explicación:** `for i in range(1, 6)` recorre una secuencia numérica que va desde el inicio (1) hasta el límite superior exclusivo (6 - 1 = 5). En contraste, el bucle `while` se ejecuta continuamente siempre que la variable control `i` cumpla con ser menor o igual a 5.
* **Salida en consola:**
  ```text
  Números del 1 al 5 usando for:
  1
  2
  3
  4
  5
  Números del 1 al 5 usando while:
  1
  2
  3
  4
  5
  ```

---

### Ejemplo 7: Listas Básicas (`07_ListasBasicas.py`)
Manipulación de conjuntos de elementos ordenados.

```python
# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza"]

# Imprimir la lista completa
print("Lista de frutas:", frutas)

# Acceder a elementos de la lista
print("Primera fruta:", frutas[0])

# Agregar una nueva fruta a la lista
frutas.append("durazno")
print("Lista actualizada de frutas:", frutas)
```
* **Explicación:** Las listas se delimitan por corchetes `[]`. El primer elemento se ubica en el índice `0`. Se utiliza el método `.append()` para añadir de forma dinámica elementos nuevos al final del contenedor.
* **Salida en consola:**
  ```text
  Lista de frutas: ['manzana', 'banana', 'cereza']
  Primera fruta: manzana
  Lista actualizada de frutas: ['manzana', 'banana', 'cereza', 'durazno']
  ```

---

### Ejemplo 8: Funciones Básicas (`08_FuncionesBasicas.py`)
Estructuración de código reutilizable.

```python
# Definir una función que saluda
def saludar(nombre):
    print("Hola, " + nombre + "!")

# Llamar a la función
saludar("María")
saludar("Carlos")
```
* **Explicación:** Usamos la palabra clave `def` para declarar una función llamada `saludar` que requiere un parámetro de entrada `nombre`. Al invocarla con diferentes argumentos, ejecuta las sentencias de su bloque interno.
* **Salida en consola:**
  ```text
  Hola, María!
  Hola, Carlos!
  ```

---

### Ejemplo 9: Manejo de Cadenas (`09_ManejodeCadenas.py`)
Herramientas integradas para procesamiento y modificación de textos.

```python
# Definir una cadena de texto
texto = "Hola, Mundo"

# Convertir a mayúsculas
print(texto.upper())

# Convertir a minúsculas
print(texto.lower())

# Reemplazar una palabra
print(texto.replace("Mundo", "Python"))
```
* **Explicación:** Demuestra el uso de métodos incorporados de objetos tipo String. Cabe destacar que estos métodos devuelven una *nueva* cadena modificada, dejando la variable original intacta (inmutabilidad).
* **Salida en consola:**
  ```text
  HOLA, MUNDO
  hola, mundo
  Hola, Python
  ```

---

### Ejemplo 10: Manejo de Archivos Básico (`10_ManejodeArchivosBasicos.py`)
Acciones de entrada y salida persistentes con el disco duro.

```python
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, Mundo\n")
    archivo.write("Bienvenido a Python.")

# Leer desde un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
```
* **Explicación:** La declaración `with` (context manager) se encarga de abrir y cerrar automáticamente la conexión con el archivo `ejemplo.txt`. Usamos el modo `"w"` (write) para sobrescribir y `"r"` (read) para leer el flujo de datos.
* **Salida en consola:**
  ```text
  Contenido del archivo:
  Hola, Mundo
  Bienvenido a Python.
  ```
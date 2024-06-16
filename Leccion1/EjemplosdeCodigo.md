### Ejemplo 1: Hola, Mundo
Este es el ejemplo más básico para imprimir texto en la consola.

```python
# Este es tu primer programa en Python
print("Hola, Mundo")
```

### Ejemplo 2: Operaciones Aritméticas
Introduce a los estudiantes a las operaciones aritméticas básicas en Python.

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

### Ejemplo 3: Uso de Variables
Muestra cómo se pueden usar las variables para almacenar y manipular datos.

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

### Ejemplo 4: Entrada de Usuario
Introduce cómo obtener datos del usuario mediante la función `input`.

```python
# Pedir el nombre del usuario
nombre_usuario = input("¿Cómo te llamas? ")

# Saludar al usuario
print("Hola, " + nombre_usuario + "! Bienvenido a Python.")
```

### Ejemplo 5: Condicionales Básicos
Introduce las estructuras de control como los condicionales.

```python
# Pedir una edad al usuario
edad = int(input("¿Cuántos años tienes? "))

# Usar una estructura condicional
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

### Ejemplo 6: Ciclos Básicos
Introduce los bucles `for` y `while`.

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

### Ejemplo 7: Listas Básicas
Introduce las listas y cómo manipularlas.

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

### Ejemplo 8: Funciones Básicas
Introduce la creación y uso de funciones.

```python
# Definir una función que saluda
def saludar(nombre):
    print("Hola, " + nombre + "!")

# Llamar a la función
saludar("María")
saludar("Carlos")
```

### Ejemplo 9: Manejo de Cadenas
Introduce métodos básicos para manipular cadenas de texto.

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

### Ejemplo 10: Manejo de Archivos Básico
Introduce la lectura y escritura de archivos.

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
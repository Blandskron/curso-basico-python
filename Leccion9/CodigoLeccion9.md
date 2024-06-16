### Ejemplo 1: Importación y Uso Básico de Módulos

```python
# Importación y uso básico de módulos
import math

# Calcular el factorial de un número
numero = 5
factorial = math.factorial(numero)
print(f"El factorial de {numero} es {factorial}")

# Calcular el seno de un ángulo en radianes
angulo = math.radians(45)
seno = math.sin(angulo)
print(f"El seno de 45 grados es aproximadamente {seno:.2f}")
```

En este ejemplo, se importa el módulo `math` y se utilizan algunas de sus funciones matemáticas como `factorial()` y `sin()`, junto con la conversión de grados a radianes usando `radians()`.

### Ejemplo 2: Uso de Funciones Específicas de Módulos

```python
# Uso de funciones específicas de módulos
from random import choice, shuffle

# Lista de colores
colores = ["rojo", "verde", "azul", "amarillo"]

# Elegir un color aleatorio de la lista
color_aleatorio = choice(colores)
print(f"Color aleatorio elegido: {color_aleatorio}")

# Mezclar la lista de colores
shuffle(colores)
print("Lista de colores mezclada:", colores)
```

En este ejemplo, se importan las funciones `choice()` y `shuffle()` del módulo `random`. `choice()` elige un elemento aleatorio de la lista `colores`, mientras que `shuffle()` mezcla la lista `colores` en su lugar.

### Ejemplo 3: Uso de la Librería `os` para Interacción con el Sistema Operativo

```python
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
```

En este ejemplo, se utiliza la librería `os` para obtener el directorio actual de trabajo con `getcwd()` y para listar el contenido del directorio con `listdir()`.

### Ejemplo 4: Uso de la Librería `datetime` para Manejo de Fechas y Horas

```python
# Uso de la librería datetime
import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()
print(f"Fecha y hora actual: {fecha_actual}")

# Formatear la fecha y hora
fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
print(f"Fecha y hora formateada: {fecha_formateada}")
```

En este ejemplo, se importa la librería `datetime` para obtener la fecha y hora actuales con `datetime.now()` y para formatear esa fecha y hora en un formato específico usando `strftime()`.

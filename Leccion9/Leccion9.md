## Lección 9: Módulos y Librerías Estándar

### 1. Importación de Módulos

#### Objetivos
- Aprender cómo importar y utilizar módulos en Python.
- Explorar diferentes formas de importación y el uso de alias.

#### Importación Básica
- Los módulos en Python son archivos que contienen funciones, variables y clases que pueden ser utilizadas en otros programas.
- Se importan utilizando la palabra clave `import`.

```python
# Ejemplo de importación de módulo
import math

# Uso de funciones del módulo math
print(math.sqrt(25))  # Salida: 5.0 (raíz cuadrada de 25)
```

#### Importación con Alias
- Se puede importar un módulo con un alias para facilitar su uso en el código.

```python
# Ejemplo de importación con alias
import datetime as dt

# Uso del módulo datetime con alias
hoy = dt.date.today()
print(hoy)  # Salida: YYYY-MM-DD (fecha actual)
```

#### Importación de Funciones Específicas
- También es posible importar funciones específicas de un módulo en lugar del módulo completo.

```python
# Ejemplo de importación de funciones específicas
from random import randint

# Uso de la función randint() del módulo random
numero = randint(1, 100)
print(f"Número aleatorio: {numero}")
```

### 2. Uso de Librerías Estándar

#### Objetivos
- Explorar algunas de las librerías estándar más comunes en Python.
- Aprender cómo utilizar funcionalidades adicionales disponibles sin necesidad de instalaciones externas.

#### Ejemplos de Librerías Estándar

##### Librería `os`
- Permite interactuar con el sistema operativo, manipular archivos y directorios.

```python
# Ejemplo de uso de la librería os
import os

# Obtener el directorio actual de trabajo
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")
```

##### Librería `datetime`
- Proporciona clases para manipular fechas y horas.

```python
# Ejemplo de uso de la librería datetime
import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")
```

##### Librería `random`
- Ofrece funciones para generar números aleatorios.

```python
# Ejemplo de uso de la librería random
import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio: {numero_aleatorio}")
```

### Ejemplos de Código

#### Ejemplo 1: Importación y Uso Básico de Módulos

```python
# Importación y uso básico de módulos
import math

# Calcular la raíz cuadrada de un número
numero = 16
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
```

#### Ejemplo 2: Uso de Funciones Específicas de Módulos

```python
# Uso de funciones específicas de módulos
from random import choice

# Lista de opciones
opciones = ["rojo", "verde", "azul"]

# Elegir un elemento aleatorio de la lista
eleccion = choice(opciones)
print(f"La elección aleatoria es: {eleccion}")
```

### Resumen y Tareas

- Hoy aprendiste sobre cómo utilizar módulos y librerías estándar en Python.
- Practicaste la importación de módulos, el uso de alias y funciones específicas, así como el aprovechamiento de funcionalidades ofrecidas por librerías estándar como `os`, `datetime` y `random`.
- **Tarea:** Crea un programa que:
  1. Importe la librería `os` y muestre todos los archivos en el directorio actual.
  2. Utilice la librería `datetime` para imprimir la fecha y hora actual.
  3. Importe la función `shuffle` del módulo `random` y mezcle una lista de números del 1 al 10.

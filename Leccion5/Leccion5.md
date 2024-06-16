## Lección 5: Listas y Tuplas

### 1. Listas

#### Objetivos
- Entender qué son las listas y cómo se utilizan en Python.
- Aprender a crear, manipular y acceder a elementos y sublistas.

#### Creación de Listas
- Las listas en Python son colecciones ordenadas y mutables de elementos.
- Se definen usando corchetes `[]`.

```python
# Crear una lista vacía
lista_vacia = []

# Crear una lista con elementos
lista_frutas = ["manzana", "banana", "cereza"]
```

#### Manipulación de Listas
- Las listas pueden contener elementos de cualquier tipo y los elementos pueden ser modificados.

```python
# Agregar elementos a una lista
lista_frutas.append("naranja")
print(lista_frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja']

# Eliminar un elemento de una lista
lista_frutas.remove("banana")
print(lista_frutas)  # Salida: ['manzana', 'cereza', 'naranja']

# Modificar un elemento de una lista
lista_frutas[1] = "fresa"
print(lista_frutas)  # Salida: ['manzana', 'fresa', 'naranja']
```

### 2. Acceso a Elementos y Sublistas

#### Acceso a Elementos
- Los elementos de una lista se pueden acceder usando índices, comenzando desde 0.

```python
# Acceder al primer elemento
print(lista_frutas[0])  # Salida: 'manzana'

# Acceder al último elemento
print(lista_frutas[-1])  # Salida: 'naranja'
```

#### Sublistas
- Se pueden extraer sublistas usando el operador de slicing `:`.

```python
# Extraer una sublista
sublista = lista_frutas[0:2]
print(sublista)  # Salida: ['manzana', 'fresa']
```

### 3. Tuplas

#### Objetivos
- Entender qué son las tuplas y cómo se utilizan en Python.
- Aprender las diferencias entre listas y tuplas.

#### Creación de Tuplas
- Las tuplas en Python son colecciones ordenadas e inmutables de elementos.
- Se definen usando paréntesis `()`.

```python
# Crear una tupla vacía
tupla_vacia = ()

# Crear una tupla con elementos
tupla_frutas = ("manzana", "banana", "cereza")
```

#### Manipulación de Tuplas
- A diferencia de las listas, las tuplas no pueden ser modificadas después de su creación.

```python
# Acceder a elementos de una tupla
print(tupla_frutas[0])  # Salida: 'manzana'

# Intentar modificar una tupla (esto generará un error)
# tupla_frutas[1] = "fresa"  # Error: 'tuple' object does not support item assignment
```

### Diferencias entre Listas y Tuplas

| Característica       | Listas                     | Tuplas                    |
|----------------------|----------------------------|---------------------------|
| Mutabilidad          | Mutables                   | Inmutables                |
| Sintaxis             | Corchetes `[]`             | Paréntesis `()`           |
| Modificable          | Sí                         | No                        |
| Uso                  | Colecciones de elementos   | Colecciones de elementos  |
| Ejemplos de Uso      | Pueden cambiarse frecuentemente | Datos constantes           |

### Ejemplos de Código

#### Ejemplo 1: Creación y Manipulación de Listas

```python
# Crear una lista
numeros = [1, 2, 3, 4, 5]

# Agregar un elemento
numeros.append(6)
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# Eliminar un elemento
numeros.remove(3)
print(numeros)  # Salida: [1, 2, 4, 5, 6]

# Modificar un elemento
numeros[2] = 10
print(numeros)  # Salida: [1, 2, 10, 5, 6]
```

#### Ejemplo 2: Acceso a Elementos y Sublistas

```python
# Crear una lista
animales = ["perro", "gato", "conejo", "tortuga"]

# Acceder al primer y último elemento
print(animales[0])  # Salida: 'perro'
print(animales[-1])  # Salida: 'tortuga'

# Extraer una sublista
sublista_animales = animales[1:3]
print(sublista_animales)  # Salida: ['gato', 'conejo']
```

#### Ejemplo 3: Creación y Acceso a Elementos de Tuplas

```python
# Crear una tupla
colores = ("rojo", "verde", "azul")

# Acceder al primer y último elemento
print(colores[0])  # Salida: 'rojo'
print(colores[-1])  # Salida: 'azul'

# Intentar modificar una tupla generará un error
# colores[1] = "amarillo"  # Error: 'tuple' object does not support item assignment
```

### Resumen y Tareas
- Hoy aprendiste sobre listas y tuplas en Python.
- Practicaste cómo crear, manipular y acceder a elementos de listas y tuplas.
- **Tarea:** Crea un programa que:
  1. Defina una lista de tus frutas favoritas y realice al menos tres manipulaciones (agregar, eliminar, modificar).
  2. Defina una tupla con los nombres de los días de la semana y acceda a los primeros tres días.
  3. Explique las diferencias entre listas y tuplas en un comentario dentro del código.

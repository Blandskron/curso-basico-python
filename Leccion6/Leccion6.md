## Lección 6: Diccionarios y Conjuntos

### 1. Diccionarios

#### Objetivos
- Entender qué son los diccionarios y cómo se utilizan en Python.
- Aprender a crear, manipular y acceder a elementos de diccionarios.
- Conocer los métodos y operaciones básicas con diccionarios.

#### Creación de Diccionarios
- Los diccionarios en Python son colecciones no ordenadas de pares clave-valor.
- Se definen usando llaves `{}` y los elementos se separan por comas.

```python
# Crear un diccionario vacío
diccionario_vacio = {}

# Crear un diccionario con elementos
diccionario_frutas = {"manzana": 3, "banana": 5, "cereza": 2}
```

#### Manipulación de Diccionarios
- Los elementos de un diccionario se acceden usando las claves, que pueden ser de cualquier tipo inmutable (como cadenas, números o tuplas).

```python
# Agregar un elemento a un diccionario
diccionario_frutas["naranja"] = 4
print(diccionario_frutas)  # Salida: {'manzana': 3, 'banana': 5, 'cereza': 2, 'naranja': 4}

# Eliminar un elemento de un diccionario
del diccionario_frutas["banana"]
print(diccionario_frutas)  # Salida: {'manzana': 3, 'cereza': 2, 'naranja': 4}

# Modificar un valor de un diccionario
diccionario_frutas["manzana"] = 6
print(diccionario_frutas)  # Salida: {'manzana': 6, 'cereza': 2, 'naranja': 4}
```

### 2. Métodos y Operaciones con Diccionarios

#### Métodos de Diccionarios
- Python proporciona varios métodos útiles para trabajar con diccionarios, como `keys()`, `values()`, `items()`, etc.

```python
# Obtener todas las claves de un diccionario
claves = diccionario_frutas.keys()
print("Claves:", claves)  # Salida: dict_keys(['manzana', 'cereza', 'naranja'])

# Obtener todos los valores de un diccionario
valores = diccionario_frutas.values()
print("Valores:", valores)  # Salida: dict_values([6, 2, 4])

# Obtener pares clave-valor como tuplas
items = diccionario_frutas.items()
print("Items:", items)  # Salida: dict_items([('manzana', 6), ('cereza', 2), ('naranja', 4)])
```

### 3. Conjuntos

#### Objetivos
- Introducir los conjuntos y su uso en Python.
- Aprender cómo crear conjuntos y realizar operaciones básicas con ellos.

#### Creación de Conjuntos
- Los conjuntos en Python son colecciones desordenadas de elementos únicos.
- Se definen usando llaves `{}` o la función `set()`.

```python
# Crear un conjunto vacío
conjunto_vacio = set()

# Crear un conjunto con elementos
conjunto_colores = {"rojo", "verde", "azul"}
```

#### Operaciones con Conjuntos
- Los conjuntos soportan operaciones como unión, intersección, diferencia y comprobación de pertenencia.

```python
# Agregar elementos a un conjunto
conjunto_colores.add("amarillo")
print(conjunto_colores)  # Salida: {'rojo', 'verde', 'azul', 'amarillo'}

# Eliminar un elemento de un conjunto
conjunto_colores.remove("verde")
print(conjunto_colores)  # Salida: {'rojo', 'azul', 'amarillo'}

# Comprobación de pertenencia
print("rojo" in conjunto_colores)  # Salida: True

# Operaciones entre conjuntos
conjunto_numeros1 = {1, 2, 3, 4, 5}
conjunto_numeros2 = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = conjunto_numeros1 | conjunto_numeros2
print("Unión:", union)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección de conjuntos
interseccion = conjunto_numeros1 & conjunto_numeros2
print("Intersección:", interseccion)  # Salida: {4, 5}

# Diferencia entre conjuntos
diferencia = conjunto_numeros1 - conjunto_numeros2
print("Diferencia:", diferencia)  # Salida: {1, 2, 3}
```

### Ejemplos de Código

#### Ejemplo 1: Creación y Manipulación de Diccionarios

```python
# Crear un diccionario de edad de personas
edades = {"Juan": 30, "María": 25, "Carlos": 35}

# Agregar una nueva persona con su edad
edades["Ana"] = 28
print(edades)  # Salida: {'Juan': 30, 'María': 25, 'Carlos': 35, 'Ana': 28}

# Eliminar la entrada de Carlos
del edades["Carlos"]
print(edades)  # Salida: {'Juan': 30, 'María': 25, 'Ana': 28}

# Mostrar todas las claves del diccionario
print("Claves:", edades.keys())  # Salida: dict_keys(['Juan', 'María', 'Ana'])
```

#### Ejemplo 2: Creación y Operaciones con Conjuntos

```python
# Crear dos conjuntos de números
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Unión de conjuntos
union = set1 | set2
print("Unión:", union)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección de conjuntos
interseccion = set1 & set2
print("Intersección:", interseccion)  # Salida: {4, 5}

# Diferencia entre conjuntos
diferencia = set1 - set2
print("Diferencia:", diferencia)  # Salida: {1, 2, 3}
```

### Resumen y Tareas
- Hoy aprendiste sobre diccionarios y conjuntos en Python.
- Practicaste cómo crear, manipular y realizar operaciones con diccionarios y conjuntos.
- **Tarea:** Crea un programa que:
  1. Defina un diccionario de productos donde las claves sean nombres de productos y los valores sean sus precios.
  2. Defina dos conjuntos: uno con números pares del 1 al 10 y otro con números impares del 1 al 10. Realiza operaciones de unión, intersección y diferencia entre estos conjuntos.

### Ejemplo 1: Creación y Manipulación de Diccionarios

```python
# Crear un diccionario de estudiantes y sus calificaciones
calificaciones = {"Juan": 85, "María": 90, "Carlos": 78}

# Agregar un nuevo estudiante y su calificación
calificaciones["Ana"] = 95
print(calificaciones)  # Salida: {'Juan': 85, 'María': 90, 'Carlos': 78, 'Ana': 95}

# Eliminar la entrada de Carlos
del calificaciones["Carlos"]
print(calificaciones)  # Salida: {'Juan': 85, 'María': 90, 'Ana': 95}

# Obtener todas las claves del diccionario
print("Estudiantes:", calificaciones.keys())  # Salida: dict_keys(['Juan', 'María', 'Ana'])
```

### Ejemplo 2: Métodos y Operaciones con Diccionarios

```python
# Crear un diccionario de palabras y sus traducciones
diccionario = {"casa": "house", "perro": "dog", "sol": "sun"}

# Obtener todas las claves del diccionario
claves = diccionario.keys()
print("Claves:", claves)  # Salida: dict_keys(['casa', 'perro', 'sol'])

# Obtener todos los valores del diccionario
valores = diccionario.values()
print("Valores:", valores)  # Salida: dict_values(['house', 'dog', 'sun'])

# Obtener pares clave-valor como tuplas
items = diccionario.items()
print("Items:", items)  # Salida: dict_items([('casa', 'house'), ('perro', 'dog'), ('sol', 'sun')])
```

### Ejemplo 3: Creación y Operaciones con Conjuntos

```python
# Crear dos conjuntos de números
numeros_pares = {2, 4, 6, 8, 10}
numeros_impares = {1, 3, 5, 7, 9}

# Agregar un número al conjunto de pares
numeros_pares.add(12)
print("Números pares:", numeros_pares)  # Salida: {2, 4, 6, 8, 10, 12}

# Eliminar un número del conjunto de impares
numeros_impares.remove(7)
print("Números impares:", numeros_impares)  # Salida: {1, 3, 5, 9}

# Comprobación de pertenencia en conjuntos
print("¿El número 4 está en números pares?", 4 in numeros_pares)  # Salida: True

# Unión de conjuntos
union = numeros_pares | numeros_impares
print("Unión:", union)  # Salida: {1, 2, 3, 4, 5, 6, 8, 9, 10, 12}

# Intersección de conjuntos
interseccion = numeros_pares & numeros_impares
print("Intersección:", interseccion)  # Salida: set()

# Diferencia entre conjuntos
diferencia = numeros_pares - numeros_impares
print("Diferencia:", diferencia)  # Salida: {2, 4, 6, 8, 10, 12}
```

### Ejemplo 4: Operaciones Avanzadas con Conjuntos

```python
# Crear dos conjuntos de letras
set1 = {"a", "b", "c", "d", "e"}
set2 = {"c", "d", "e", "f", "g"}

# Actualizar un conjunto con elementos de otro conjunto
set1.update(set2)
print("Set1 actualizado:", set1)  # Salida: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# Eliminar un elemento específico de un conjunto
set1.discard("b")
print("Set1 después de descartar 'b':", set1)  # Salida: {'a', 'c', 'd', 'e', 'f', 'g'}

# Vaciar un conjunto
set2.clear()
print("Set2 después de limpiar:", set2)  # Salida: set()
```

### Ejemplo 5: Diccionario de Diccionarios

```python
# Crear un diccionario de diccionarios para almacenar información de estudiantes
estudiantes = {
    "Juan": {"edad": 25, "carrera": "Informática"},
    "María": {"edad": 23, "carrera": "Matemáticas"},
    "Ana": {"edad": 27, "carrera": "Física"}
}

# Acceder a la información de un estudiante específico
print("Información de Juan:", estudiantes["Juan"])  
# Salida: {'edad': 25, 'carrera': 'Informática'}

# Modificar la información de un estudiante
estudiantes["Ana"]["edad"] = 28
print("Información actualizada de Ana:", estudiantes["Ana"])  
# Salida: {'edad': 28, 'carrera': 'Física'}
```

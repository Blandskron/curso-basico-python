### Ejemplo 1: Creación y Manipulación de Listas

```python
# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza", "naranja"]

# Agregar un elemento al final de la lista
frutas.append("kiwi")
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Eliminar un elemento específico de la lista
frutas.remove("banana")
print(frutas)  # Salida: ['manzana', 'cereza', 'naranja', 'kiwi']

# Modificar un elemento en la lista
frutas[0] = "fresa"
print(frutas)  # Salida: ['fresa', 'cereza', 'naranja', 'kiwi']
```

### Ejemplo 2: Acceso a Elementos y Sublistas

```python
# Crear una lista de colores
colores = ["rojo", "verde", "azul", "amarillo", "naranja"]

# Acceder al primer y último elemento de la lista
print(colores[0])     # Salida: 'rojo'
print(colores[-1])    # Salida: 'naranja'

# Extraer una sublista usando slicing
sublista = colores[1:4]
print(sublista)       # Salida: ['verde', 'azul', 'amarillo']
```

### Ejemplo 3: Creación y Acceso a Elementos de Tuplas

```python
# Crear una tupla de coordenadas
coordenadas = (3, 5)

# Acceder a los elementos de la tupla
print("Coordenada X:", coordenadas[0])   # Salida: 3
print("Coordenada Y:", coordenadas[1])   # Salida: 5

# Intentar modificar una tupla (esto generará un error)
# coordenadas[0] = 4  # Error: 'tuple' object does not support item assignment
```

### Ejemplo 4: Diferencias entre Listas y Tuplas

```python
# Listas
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")   # Se puede modificar la lista
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja']

# Tuplas
colores = ("rojo", "verde", "azul")
# colores.append("amarillo")  # Generaría un error, las tuplas son inmutables
print(colores)  # Salida: ('rojo', 'verde', 'azul')
```

### Ejemplo 5: Uso Avanzado de Slicing en Listas

```python
# Crear una lista de números pares del 2 al 10
numeros_pares = [2, 4, 6, 8, 10]

# Acceder a elementos usando slicing avanzado
print(numeros_pares[1:4])     # Salida: [4, 6, 8]
print(numeros_pares[:3])      # Salida: [2, 4, 6]
print(numeros_pares[2:])      # Salida: [6, 8, 10]
print(numeros_pares[::-1])    # Salida: [10, 8, 6, 4, 2] (invertir la lista)
```

### Ejemplo 6: Tuplas Anidadas

```python
# Tuplas anidadas: Tupla de coordenadas
puntos = ((1, 2), (3, 4), (5, 6))

# Acceder a los elementos de la tupla anidada
print("Primer punto:", puntos[0])       # Salida: (1, 2)
print("Coordenada X del segundo punto:", puntos[1][0])  # Salida: 3
print("Coordenada Y del tercer punto:", puntos[2][1])   # Salida: 6
```

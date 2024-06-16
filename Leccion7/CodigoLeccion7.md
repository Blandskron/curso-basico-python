### Ejemplo 1: Operaciones Básicas con Cadenas

```python
# Concatenación de cadenas
saludo = "Hola, "
nombre = "María!"
mensaje = saludo + nombre
print(mensaje)  # Salida: Hola, María!

# Indexación y slicing
frase = "Python es un lenguaje de programación"
primer_caracter = frase[0]
ultima_palabra = frase[-13:]  # Últimos 13 caracteres
print(primer_caracter)     # Salida: P
print(ultima_palabra)   # Salida: programación
```

### Ejemplo 2: Métodos de Cadenas

```python
# Métodos de cadenas
frase = "¡Python es fantástico!"

# Convertir a mayúsculas y minúsculas
print(frase.upper())    # Salida: ¡PYTHON ES FANTÁSTICO!
print(frase.lower())    # Salida: ¡python es fantástico!

# Contar ocurrencias de una subcadena
print(frase.count("a"))    # Salida: 2 (número de veces que 'a' aparece en la frase)

# Encontrar la posición de una subcadena
print(frase.find("fantástico"))    # Salida: 14 (índice de la primera aparición de "fantástico")

# Reemplazar una subcadena
nueva_frase = frase.replace("Python", "Java")
print(nueva_frase)    # Salida: ¡Java es fantástico!
```

### Ejemplo 3: Formateo de Cadenas con f-strings

```python
# Formateo con f-strings
nombre = "Carlos"
edad = 28
mensaje = f"{nombre} tiene {edad} años."
print(mensaje)  # Salida: Carlos tiene 28 años.
```

### Ejemplo 4: Formateo de Cadenas con el Método `format()`

```python
# Formateo con el método format()
nombre = "Ana"
edad = 30
mensaje = "{} tiene {} años.".format(nombre, edad)
print(mensaje)  # Salida: Ana tiene 30 años.
```

### Ejemplo 5: Tarea Sugerida - Contar Ocurrencias y Reemplazar

```python
# Tarea: Contar ocurrencias y reemplazar
frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme..."

# Contar cuántas veces aparece la letra 'a'
conteo_a = frase.count('a')
print(f"La letra 'a' aparece {conteo_a} veces.")

# Reemplazar "Mancha" por "mundo"
nueva_frase = frase.replace("Mancha", "mundo")
print("Frase modificada:", nueva_frase)
```

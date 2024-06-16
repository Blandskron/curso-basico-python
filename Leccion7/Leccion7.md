## Lección 7: Manejo de Cadenas

### 1. Operaciones Básicas con Cadenas

#### Objetivos
- Aprender cómo las cadenas son tratadas como secuencias de caracteres en Python.
- Realizar operaciones básicas como concatenación, indexación y slicing.

#### Concatenación de Cadenas
- La concatenación de cadenas se realiza usando el operador `+`.

```python
# Concatenación de cadenas
saludo = "¡Hola, "
nombre = "Juan!"
mensaje = saludo + nombre
print(mensaje)  # Salida: ¡Hola, Juan!
```

#### Indexación y Slicing
- Las cadenas pueden ser accedidas por índices y segmentadas usando slicing.

```python
# Acceder a caracteres individuales por índice
palabra = "Python"
primer_caracter = palabra[0]  # Primer carácter
ultimo_caracter = palabra[-1]  # Último carácter
print(primer_caracter)  # Salida: 'P'
print(ultimo_caracter)  # Salida: 'n'

# Slicing de cadenas
subcadena = palabra[1:4]  # Desde el índice 1 hasta el 3 (exclusivo)
print(subcadena)  # Salida: 'yth'
```

### 2. Métodos de Cadenas

#### Objetivos
- Explorar métodos integrados de cadenas para manipulación y búsqueda.

#### Métodos Comunes de Cadenas
- Python proporciona una variedad de métodos útiles para operar y manipular cadenas.

```python
# Ejemplo de métodos de cadenas
frase = "Python es un lenguaje de programación"

# Convertir a mayúsculas y minúsculas
print(frase.upper())    # Salida: "PYTHON ES UN LENGUAJE DE PROGRAMACIÓN"
print(frase.lower())    # Salida: "python es un lenguaje de programación"

# Contar ocurrencias de una subcadena
print(frase.count("a"))    # Salida: 4 (número de veces que 'a' aparece en la frase)

# Encontrar la posición de una subcadena
print(frase.find("lenguaje"))    # Salida: 12 (índice de la primera aparición de "lenguaje")

# Reemplazar una subcadena
nueva_frase = frase.replace("Python", "Java")
print(nueva_frase)    # Salida: "Java es un lenguaje de programación"
```

### 3. Formateo de Cadenas

#### Objetivos
- Aprender diferentes métodos para formatear cadenas en Python.

#### Formateo con f-strings (Python 3.6+)
- Las f-strings permiten incrustar expresiones Python dentro de cadenas de manera conveniente.

```python
nombre = "María"
edad = 30

# Usar f-strings para formatear una cadena
mensaje = f"{nombre} tiene {edad} años."
print(mensaje)  # Salida: "María tiene 30 años."
```

#### Método `format()`
- El método `format()` proporciona una forma más flexible de formatear cadenas.

```python
nombre = "Carlos"
edad = 25

# Usar el método format()
mensaje = "{} tiene {} años.".format(nombre, edad)
print(mensaje)  # Salida: "Carlos tiene 25 años."
```

### Ejemplos de Código

#### Ejemplo 1: Operaciones Básicas con Cadenas

```python
# Concatenación de cadenas
saludo = "Hola, "
nombre = "Pedro!"
mensaje = saludo + nombre
print(mensaje)  # Salida: Hola, Pedro!

# Indexación y slicing
frase = "Python es un lenguaje"
primer_letra = frase[0]
ultima_palabra = frase[-9:]
print(primer_letra)     # Salida: P
print(ultima_palabra)   # Salida: lenguaje
```

#### Ejemplo 2: Métodos de Cadenas

```python
# Métodos de cadenas
frase = "Hola Mundo!"

# Convertir a mayúsculas y minúsculas
print(frase.upper())    # Salida: HOLA MUNDO!
print(frase.lower())    # Salida: hola mundo!

# Contar ocurrencias de una subcadena
print(frase.count("o"))    # Salida: 2 (número de veces que 'o' aparece en la frase)

# Encontrar la posición de una subcadena
print(frase.find("Mundo"))    # Salida: 5 (índice de la primera aparición de "Mundo")

# Reemplazar una subcadena
nueva_frase = frase.replace("Mundo", "Amigo")
print(nueva_frase)    # Salida: Hola Amigo!
```

#### Ejemplo 3: Formateo de Cadenas

```python
# Formateo con f-strings
nombre = "Ana"
edad = 28
mensaje = f"{nombre} tiene {edad} años."
print(mensaje)  # Salida: Ana tiene 28 años.

# Formateo con el método format()
nombre = "Juan"
edad = 32
mensaje = "{} tiene {} años.".format(nombre, edad)
print(mensaje)  # Salida: Juan tiene 32 años.
```

### Resumen y Tareas
- Hoy aprendiste sobre cómo manejar cadenas en Python.
- Practicaste operaciones básicas, métodos integrados y técnicas de formateo de cadenas.
- **Tarea:** Crea un programa que:
  1. Solicite al usuario que ingrese su nombre y edad, luego imprima un mensaje formateado utilizando f-strings.
  2. Manipule una cadena para contar cuántas veces aparece una letra específica.
  3. Utilice el método `replace()` para cambiar una palabra en una frase por otra.

### Ejemplo 1: Función sin Parámetros y sin Retorno

```python
def mostrar_mensaje():
    print("Este es un mensaje desde una función.")

# Llamada a la función
mostrar_mensaje()
```

### Ejemplo 2: Función con Parámetros y sin Retorno

```python
def mostrar_nombre(nombre):
    print("Tu nombre es:", nombre)

# Llamada a la función con un argumento
mostrar_nombre("María")
```

### Ejemplo 3: Función con Parámetros y con Retorno

```python
def multiplicar(x, y):
    return x * y

# Llamada a la función y uso del valor de retorno
resultado = multiplicar(4, 5)
print("El resultado de la multiplicación es:", resultado)
```

### Ejemplo 4: Función con Parámetros por Defecto

```python
def saludar(nombre="Amigo"):
    print("Hola,", nombre)

# Llamada a la función sin argumentos (usa el valor por defecto)
saludar()

# Llamada a la función con un argumento
saludar("Ana")
```

### Ejemplo 5: Función de Conversión de Grados Celsius a Fahrenheit

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Pedir al usuario la temperatura en grados Celsius
temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir y mostrar la temperatura en grados Fahrenheit
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print("La temperatura en grados Fahrenheit es:", temp_fahrenheit)
```

### Ejemplo 6: Función para Encontrar el Máximo de Dos Números

```python
def encontrar_maximo(a, b):
    if a > b:
        return a
    else:
        return b

# Pedir al usuario dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Encontrar y mostrar el mayor de los dos números
maximo = encontrar_maximo(numero1, numero2)
print("El número mayor es:", maximo)
```

### Ejemplo 7: Función para Calcular el Factorial de un Número

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pedir al usuario un número
numero = int(input("Introduce un número para calcular su factorial: "))

# Calcular y mostrar el factorial
resultado_factorial = factorial(numero)
print("El factorial de", numero, "es:", resultado_factorial)
```

### Ejercicio 8: Función que Recibe una Lista de Números y Devuelve la Suma de Todos los Elementos

```python
def suma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Calcular y mostrar la suma de los números en la lista
suma = suma_lista(numeros)
print("La suma de los números en la lista es:", suma)
```

### Ejercicio 9: Función que Recibe una Cadena y Devuelve la Cantidad de Vocales en la Cadena

```python
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Cadena de ejemplo
cadena = "Hola, Mundo"

# Calcular y mostrar la cantidad de vocales en la cadena
cantidad_vocales = contar_vocales(cadena)
print("La cantidad de vocales en la cadena es:", cantidad_vocales)
```

### Ejercicio 10: Función que Recibe una Lista de Cadenas y Devuelve la Cadena Más Larga

```python
def cadena_mas_larga(cadenas):
    mas_larga = ""
    for cadena in cadenas:
        if len(cadena) > len(mas_larga):
            mas_larga = cadena
    return mas_larga

# Lista de cadenas
cadenas = ["manzana", "banana", "cereza", "kiwi"]

# Encontrar y mostrar la cadena más larga
larga = cadena_mas_larga(cadenas)
print("La cadena más larga es:", larga)
```

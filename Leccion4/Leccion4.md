## Lección 4: Funciones

### 1. Definición y Llamada a Funciones

#### Objetivos
- Entender qué es una función y por qué es útil.
- Aprender a definir y llamar funciones en Python.

#### ¿Qué es una Función?
- Una función es un bloque de código reutilizable que realiza una tarea específica.
- Ayuda a organizar y estructurar el código, facilitando la legibilidad y el mantenimiento.

#### Definición de Funciones
- Se define una función usando la palabra clave `def` seguida del nombre de la función y paréntesis `()`.
- El cuerpo de la función se indenta.

```python
# Ejemplo de definición de una función
def saludar():
    print("Hola, Mundo")

# Llamada a la función
saludar()
```

### 2. Parámetros y Valores de Retorno

#### Parámetros de Función
- Los parámetros permiten a una función recibir información y usarla dentro de su cuerpo.
- Los parámetros se definen dentro de los paréntesis en la definición de la función.

```python
# Ejemplo de función con parámetros
def saludar(nombre):
    print("Hola,", nombre)

# Llamada a la función con un argumento
saludar("Juan")
```

#### Valores de Retorno
- Las funciones pueden devolver valores usando la palabra clave `return`.
- Esto permite que la función envíe resultados de vuelta al lugar donde fue llamada.

```python
# Ejemplo de función con valor de retorno
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y uso del valor de retorno
suma = sumar(3, 5)
print("La suma es:", suma)
```

### Ejemplos de Funciones

#### Función sin Parámetros y sin Retorno

```python
def mostrar_mensaje():
    print("Este es un mensaje desde una función.")

mostrar_mensaje()
```

#### Función con Parámetros y sin Retorno

```python
def mostrar_nombre(nombre):
    print("Tu nombre es:", nombre)

mostrar_nombre("María")
```

#### Función con Parámetros y con Retorno

```python
def multiplicar(x, y):
    return x * y

resultado = multiplicar(4, 5)
print("El resultado de la multiplicación es:", resultado)
```

#### Función con Parámetros por Defecto

```python
def saludar(nombre="Amigo"):
    print("Hola,", nombre)

saludar()        # Usa el valor por defecto
saludar("Ana")   # Usa el valor proporcionado
```

### Ejercicios Prácticos

#### Ejercicio 1: Función de Conversión de Grados Celsius a Fahrenheit

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Pedir al usuario la temperatura en grados Celsius
temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir y mostrar la temperatura en grados Fahrenheit
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print("La temperatura en grados Fahrenheit es:", temp_fahrenheit)
```

#### Ejercicio 2: Función para Encontrar el Máximo de Dos Números

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

#### Ejercicio 3: Función para Calcular el Factorial de un Número

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

### Resumen y Tareas
- Hoy aprendiste sobre funciones en Python: cómo definirlas, llamarlas, usar parámetros y valores de retorno.
- Practicaste con varios ejemplos de funciones.
- **Tarea:** Crea un programa que:
  1. Defina una función que reciba una lista de números y devuelva la suma de todos los elementos.
  2. Defina una función que reciba una cadena y devuelva la cantidad de vocales en la cadena.
  3. Defina una función que reciba una lista de cadenas y devuelva la cadena más larga.

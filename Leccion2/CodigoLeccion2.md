### Ejemplo 1: Asignación de Variables

```python
# Asignación de variables
numero_entero = 10
numero_flotante = 10.5
cadena_texto = "Hola, Python"
valor_booleano = True

# Imprimir valores de las variables
print("Número entero:", numero_entero)
print("Número flotante:", numero_flotante)
print("Cadena de texto:", cadena_texto)
print("Valor booleano:", valor_booleano)
```

### Ejemplo 2: Operaciones Aritméticas

```python
# Operaciones aritméticas
a = 10
b = 5

suma = a + b
print("Suma:", suma)

resta = a - b
print("Resta:", resta)

multiplicacion = a * b
print("Multiplicación:", multiplicacion)

division = a / b
print("División:", division)

division_entera = a // b
print("División Entera:", division_entera)

modulo = a % b
print("Módulo:", modulo)

exponente = a ** b
print("Exponenciación:", exponente)
```

### Ejemplo 3: Concatenación de Cadenas

```python
# Concatenación de cadenas
saludo = "Hola"
nombre = "Juan"
frase = saludo + ", " + nombre + "!"
print(frase)
```

### Ejemplo 4: Operaciones con Booleanos

```python
# Operaciones lógicas con booleanos
verdadero = True
falso = False

resultado_and = verdadero and falso
print("AND lógico:", resultado_and)

resultado_or = verdadero or falso
print("OR lógico:", resultado_or)

resultado_not = not verdadero
print("NOT lógico:", resultado_not)
```

### Ejemplo 5: Programa Interactivo - Operaciones Aritméticas

```python
# Programa que pide dos números al usuario y realiza operaciones aritméticas

# Pedir al usuario el primer número
numero1 = float(input("Introduce el primer número: "))

# Pedir al usuario el segundo número
numero2 = float(input("Introduce el segundo número: "))

# Realizar operaciones aritméticas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
```

### Ejemplo 6: Programa Interactivo - Mensaje Personalizado

```python
# Programa que pide el nombre y la edad del usuario y muestra un mensaje personalizado

# Pedir al usuario su nombre
nombre = input("Introduce tu nombre: ")

# Pedir al usuario su edad
edad = int(input("Introduce tu edad: "))

# Crear y mostrar el mensaje personalizado
mensaje = "Hola, " + nombre + ". Tienes " + str(edad) + " años."
print(mensaje)
```

### Ejemplo 7: Conversión de Tipos de Datos

```python
# Conversión de tipos de datos
numero_str = "123"
numero_int = int(numero_str)
print("Convertido a entero:", numero_int)

flotante_str = "3.14"
numero_flotante = float(flotante_str)
print("Convertido a flotante:", numero_flotante)

# Convertir número a cadena
numero = 100
numero_cadena = str(numero)
print("Convertido a cadena:", numero_cadena)

# Convertir booleano a entero
verdadero = True
falso = False
print("Convertido a entero (True):", int(verdadero))
print("Convertido a entero (False):", int(falso))
```

## Lección 2: Variables y Tipos de Datos

### 1. Tipos de Datos Básicos

#### Objetivos
- Comprender qué son las variables y cómo se utilizan en Python.
- Conocer los tipos de datos básicos: enteros, flotantes, cadenas y booleanos.
- Realizar operaciones básicas con variables.

#### Variables
- Una variable es un espacio en la memoria donde se almacena un valor.
- En Python, no es necesario declarar el tipo de variable explícitamente; Python lo infiere automáticamente.

#### Asignación de Variables
- Se utiliza el signo igual (`=`) para asignar valores a las variables.

```python
# Asignación de variables
numero_entero = 10
numero_flotante = 10.5
cadena_texto = "Hola, Python"
valor_booleano = True
```

### 2. Tipos de Datos

#### Enteros (int)
- Los enteros son números sin parte decimal.

```python
# Ejemplo de entero
numero_entero = 42
print(numero_entero)
```

#### Flotantes (float)
- Los flotantes son números con parte decimal.

```python
# Ejemplo de flotante
numero_flotante = 3.14
print(numero_flotante)
```

#### Cadenas (str)
- Las cadenas son secuencias de caracteres encerradas entre comillas simples o dobles.

```python
# Ejemplo de cadena
cadena_texto = "Hola, Mundo"
print(cadena_texto)
```

#### Booleanos (bool)
- Los booleanos representan valores de verdad: `True` o `False`.

```python
# Ejemplo de booleano
valor_booleano = True
print(valor_booleano)
```

### 3. Operaciones Básicas con Variables

#### Operaciones Aritméticas
- Puedes realizar operaciones aritméticas básicas con variables enteras y flotantes.

```python
# Suma
a = 10
b = 5
suma = a + b
print("Suma:", suma)

# Resta
resta = a - b
print("Resta:", resta)

# Multiplicación
multiplicacion = a * b
print("Multiplicación:", multiplicacion)

# División
division = a / b
print("División:", division)

# División entera
division_entera = a // b
print("División Entera:", division_entera)

# Módulo
modulo = a % b
print("Módulo:", modulo)

# Exponenciación
exponente = a ** b
print("Exponenciación:", exponente)
```

#### Concatenación de Cadenas
- Las cadenas pueden concatenarse usando el operador `+`.

```python
# Concatenación de cadenas
saludo = "Hola"
nombre = "Juan"
frase = saludo + ", " + nombre + "!"
print(frase)
```

#### Operaciones con Booleanos
- Puedes realizar operaciones lógicas con booleanos utilizando operadores como `and`, `or` y `not`.

```python
# Operaciones lógicas
verdadero = True
falso = False

# AND lógico
resultado_and = verdadero and falso
print("AND lógico:", resultado_and)

# OR lógico
resultado_or = verdadero or falso
print("OR lógico:", resultado_or)

# NOT lógico
resultado_not = not verdadero
print("NOT lógico:", resultado_not)
```

### Resumen y Tareas
- Hoy aprendiste sobre variables y los tipos de datos básicos en Python.
- Practicaste operaciones básicas con estos tipos de datos.
- **Tarea:** Crea un programa que:
  1. Pida al usuario dos números y muestre la suma, resta, multiplicación y división de estos números.
  2. Pida al usuario su nombre y edad, y muestre un mensaje personalizado utilizando estos datos.

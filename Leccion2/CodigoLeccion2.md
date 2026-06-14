# Guía Práctica de Código: Lección 2 (Variables y Tipos de Datos)

Esta guía documenta los archivos y ejemplos de código práctico dedicados al entendimiento y manipulación de variables y tipos de datos básicos en Python.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_AsignaciondeVariables.py` | Asignación básica e inferencia de tipos | `python 01_AsignaciondeVariables.py` |
| `02_OperacionesAritmeticas.py` | Operaciones aritméticas elementales | `python 02_OperacionesAritmeticas.py` |
| `03_ConcatenaciondeCadenas.py` | Unión y formateo de texto | `python 03_ConcatenaciondeCadenas.py` |
| `04_OperacionesconBooleanos.py` | Álgebra booleana y comparadores lógicos | `python 04_OperacionesconBooleanos.py` |
| `05_ProgramaInteractivo_OperacionesAritmeticas.py` | Entrada interactiva y operaciones matemáticas | `python 05_ProgramaInteractivo_OperacionesAritmeticas.py` |
| `06_ProgramaInteractivo_MensajePersonalizado.py` | Captura interactiva de variables múltiples | `python 06_ProgramaInteractivo_MensajePersonalizado.py` |
| `07_ConversiondeTiposdeDatos.py` | Casteo y forzado explícito de tipos | `python 07_ConversiondeTiposdeDatos.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Asignación de Variables (`01_AsignaciondeVariables.py`)
Muestra cómo se almacenan datos simples en variables autodefinidas.

```python
# Asignación de variables
numero_entero = 10
numero_flotante = 10.5
cadena_texto = "Hola, Python"
valor_booleano = True
```
* **Explicación:** Se asignan valores de cuatro tipos distintos a cuatro variables independientes. Python infiere automáticamente sus tipos como `int`, `float`, `str` y `bool`.
* **Salida en consola:** *(Este script no realiza salidas en consola al no contener llamadas a `print()`)*

---

### Ejemplo 2: Operaciones Aritméticas (`02_OperacionesAritmeticas.py`)
Cálculo aritmético usando variables y constantes.

```python
# Definición de operandos
a = 10
b = 5

# Operaciones básicas
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponente = a ** b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División Entera:", division_entera)
print("Módulo:", modulo)
print("Exponenciación:", exponente)
```
* **Explicación:** Declaramos operandos de prueba y aplicamos el catálogo de operadores aritméticos elementales de Python.
* **Salida en consola:**
  ```text
  Suma: 15
  Resta: 5
  Multiplicación: 50
  División: 2.0
  División Entera: 2
  Módulo: 0
  Exponenciación: 100000
  ```

---

### Ejemplo 3: Concatenación de Cadenas (`03_ConcatenaciondeCadenas.py`)
Ensamblado de múltiples cadenas empleando sumas de texto.

```python
# Concatenación de cadenas
saludo = "Hola"
nombre = "Juan"
frase = saludo + ", " + nombre + "!"
print(frase)
```
* **Explicación:** Empleamos el operador `+` para unir físicamente strings literales con variables de tipo cadena.
* **Salida en consola:**
  ```text
  Hola, Juan!
  ```

---

### Ejemplo 4: Operaciones con Booleanos (`04_OperacionesconBooleanos.py`)
Evaluación lógica de condiciones verdaderas o falsas.

```python
verdadero = True
falso = False

# Operadores lógicos
resultado_and = verdadero and falso
resultado_or = verdadero or falso
resultado_not = not verdadero

print("AND lógico:", resultado_and)
print("OR lógico:", resultado_or)
print("NOT lógico:", resultado_not)
```
* **Explicación:** Se operan valores booleanos usando las palabras reservadas de álgebra de proposiciones `and`, `or` y `not`.
* **Salida en consola:**
  ```text
  AND lógico: False
  OR lógico: True
  NOT lógico: False
  ```

---

### Ejemplo 5: Programa Interactivo - Operaciones Aritméticas (`05_ProgramaInteractivo_OperacionesAritmeticas.py`)
Captura interactiva y conversión directa para cálculos inmediatos.

```python
# Capturar datos de entrada
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Cálculos
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
```
* **Explicación:** Envolvemos la función `input()` con `float()` para asegurar que las variables de entrada se almacenen como números con soporte decimal antes de realizar las operaciones aritméticas.
* **Salida en consola:** *(Ejemplo de ejecución con valores 8 y 2)*
  ```text
  Introduce el primer número: 8
  Introduce el segundo número: 2
  Suma: 10.0
  Resta: 6.0
  Multiplicación: 16.0
  División: 4.0
  ```

---

### Ejemplo 6: Programa Interactivo - Mensaje Personalizado (`06_ProgramaInteractivo_MensajePersonalizado.py`)
Despliegue de datos capturados en una sola línea informativa.

```python
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")

print("Hola, " + nombre + "! Tienes " + edad + " años.")
```
* **Explicación:** Capturamos dos entradas separadas e imprimimos una oración descriptiva uniendo los valores. Como no operamos matemáticamente la edad, podemos mantenerla como texto sin necesidad de casteo.
* **Salida en consola:**
  ```text
  ¿Cómo te llamas? Bastian
  ¿Cuántos años tienes? 24
  Hola, Bastian! Tienes 24 años.
  ```

---

### Ejemplo 7: Conversión de Tipos de Datos (`07_ConversiondeTiposdeDatos.py`)
Forzado manual e inspección de clases.

```python
# Conversión de entero a flotante
entero = 5
flotante = float(entero)
print(flotante)  # Imprime: 5.0

# Conversión de flotante a entero (trunca los decimales)
decimal = 5.7
entero_nuevo = int(decimal)
print(entero_nuevo)  # Imprime: 5

# Conversión de número a cadena
numero = 100
cadena = str(numero)
print(type(cadena))  # Imprime: <class 'str'>
```
* **Explicación:** Demostramos el cambio explícito de tipos. Destaca el uso de `type()`, una función integrada de Python que nos indica la clase del objeto evaluado.
* **Salida en consola:**
  ```text
  5.0
  5
  <class 'str'>
  ```

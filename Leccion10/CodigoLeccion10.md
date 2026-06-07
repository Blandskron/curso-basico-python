# Guía Práctica de Código: Lección 10 (Proyectos Integradores)

Esta guía expone las implementaciones completas de los dos proyectos prácticos de cierre del curso detallados en la **Lección 10**.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_CalculadoraBasica.py` | Lógica de menú, funciones modulares y captura interactiva | `python 01_CalculadoraBasica.py` |
| `02_JuegodeAdivinanzadeNumeros.py` | Control de intentos, números aleatorios y bucle centinela | `python 02_JuegodeAdivinanzadeNumeros.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Calculadora Básica (`01_CalculadoraBasica.py`)
Este script implementa un menú que realiza las cuatro operaciones matemáticas básicas.

```python
# Implementación de una calculadora básica en Python

# Función para sumar dos números
def suma(num1, num2):
    return num1 + num2

# Función para restar dos números
def resta(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para dividir dos números
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: división por cero"

# Función principal para operar la calculadora
def calculadora():
    print("Bienvenido a la Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elija una operación (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción inválida")

# Llamar a la función principal de la calculadora
calculadora()
```
* **Explicación:** Se definen las funciones aritméticas básicas. La función `division(num1, num2)` valida si el segundo número es cero para evitar que Python aborte el programa con un error `ZeroDivisionError`.
* **Salida de consola esperada:**
  ```text
  Bienvenido a la Calculadora Básica
  Operaciones disponibles:
  1. Suma
  2. Resta
  3. Multiplicación
  4. División
  Elija una operación (1/2/3/4): 1
  Ingrese el primer número: 12.5
  Ingrese el segundo número: 7.5
  Resultado: 20.0
  ```

---

### Ejemplo 2: Juego de Adivinanza de Números (`02_JuegodeAdivinanzadeNumeros.py`)
Este script genera un número aleatorio entre 1 y 100 y le da 10 intentos al usuario para adivinarlo.

```python
# Implementación de un juego de adivinanza de números en Python
import random

# Función principal del juego
def juego_adivinanza():
    print("Bienvenido al Juego de Adivinanza de Números")
    print("Estoy pensando en un número entre 1 y 100...")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10

    while intentos < max_intentos:
        intentos += 1
        intento = int(input("Intenta adivinar el número: "))

        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

    if intentos == max_intentos:
        print(f"¡Agotaste tus {max_intentos} intentos! El número era {numero_secreto}")

# Llamar a la función principal del juego de adivinanza
juego_adivinanza()
```
* **Explicación:** Se importa `random` para usar `randint()`. El bucle `while` se ejecuta hasta 10 veces. Con cada intento fallido, el programa da una pista condicional (`mayor` o `menor`). Si el usuario acierta, la ejecución del ciclo se rompe inmediatamente usando `break`.
* **Salida de consola esperada:**
  ```text
  Bienvenido al Juego de Adivinanza de Números
  Estoy pensando en un número entre 1 y 100...
  Intenta adivinar el número: 50
  El número es mayor.
  Intenta adivinar el número: 75
  El número es menor.
  Intenta adivinar el número: 63
  ¡Felicidades! Adivinaste el número en 3 intentos.
  ```

### Ejemplo 1: Calculadora Básica

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

### Ejemplo 2: Juego de Adivinanza de Números

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

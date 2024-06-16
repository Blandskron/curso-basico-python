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

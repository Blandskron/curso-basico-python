# Programa que determina si un número es positivo, negativo o cero

# Pedir al usuario un número
numero = float(input("Introduce un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

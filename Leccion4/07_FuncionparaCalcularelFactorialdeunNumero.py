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

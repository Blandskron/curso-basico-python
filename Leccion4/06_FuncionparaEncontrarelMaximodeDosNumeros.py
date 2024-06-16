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

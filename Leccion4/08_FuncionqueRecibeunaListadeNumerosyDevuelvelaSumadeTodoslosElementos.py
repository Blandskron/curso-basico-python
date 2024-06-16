def suma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Calcular y mostrar la suma de los números en la lista
suma = suma_lista(numeros)
print("La suma de los números en la lista es:", suma)

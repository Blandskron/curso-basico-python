# Crear dos conjuntos de números
numeros_pares = {2, 4, 6, 8, 10}
numeros_impares = {1, 3, 5, 7, 9}

# Agregar un número al conjunto de pares
numeros_pares.add(12)
print("Números pares:", numeros_pares)  # Salida: {2, 4, 6, 8, 10, 12}

# Eliminar un número del conjunto de impares
numeros_impares.remove(7)
print("Números impares:", numeros_impares)  # Salida: {1, 3, 5, 9}

# Comprobación de pertenencia en conjuntos
print("¿El número 4 está en números pares?", 4 in numeros_pares)  # Salida: True

# Unión de conjuntos
union = numeros_pares | numeros_impares
print("Unión:", union)  # Salida: {1, 2, 3, 4, 5, 6, 8, 9, 10, 12}

# Intersección de conjuntos
interseccion = numeros_pares & numeros_impares
print("Intersección:", interseccion)  # Salida: set()

# Diferencia entre conjuntos
diferencia = numeros_pares - numeros_impares
print("Diferencia:", diferencia)  # Salida: {2, 4, 6, 8, 10, 12}

# Métodos de cadenas
frase = "¡Python es fantástico!"

# Convertir a mayúsculas y minúsculas
print(frase.upper())    # Salida: ¡PYTHON ES FANTÁSTICO!
print(frase.lower())    # Salida: ¡python es fantástico!

# Contar ocurrencias de una subcadena
print(frase.count("a"))    # Salida: 2 (número de veces que 'a' aparece en la frase)

# Encontrar la posición de una subcadena
print(frase.find("fantástico"))    # Salida: 14 (índice de la primera aparición de "fantástico")

# Reemplazar una subcadena
nueva_frase = frase.replace("Python", "Java")
print(nueva_frase)    # Salida: ¡Java es fantástico!

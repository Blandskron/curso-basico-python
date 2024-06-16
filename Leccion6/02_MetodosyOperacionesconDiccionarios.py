# Crear un diccionario de palabras y sus traducciones
diccionario = {"casa": "house", "perro": "dog", "sol": "sun"}

# Obtener todas las claves del diccionario
claves = diccionario.keys()
print("Claves:", claves)  # Salida: dict_keys(['casa', 'perro', 'sol'])

# Obtener todos los valores del diccionario
valores = diccionario.values()
print("Valores:", valores)  # Salida: dict_values(['house', 'dog', 'sun'])

# Obtener pares clave-valor como tuplas
items = diccionario.items()
print("Items:", items)  # Salida: dict_items([('casa', 'house'), ('perro', 'dog'), ('sol', 'sun')])

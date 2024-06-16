# Uso de funciones específicas de módulos
from random import choice, shuffle

# Lista de colores
colores = ["rojo", "verde", "azul", "amarillo"]

# Elegir un color aleatorio de la lista
color_aleatorio = choice(colores)
print(f"Color aleatorio elegido: {color_aleatorio}")

# Mezclar la lista de colores
shuffle(colores)
print("Lista de colores mezclada:", colores)

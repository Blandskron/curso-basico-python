# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza", "naranja"]

# Agregar un elemento al final de la lista
frutas.append("kiwi")
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Eliminar un elemento específico de la lista
frutas.remove("banana")
print(frutas)  # Salida: ['manzana', 'cereza', 'naranja', 'kiwi']

# Modificar un elemento en la lista
frutas[0] = "fresa"
print(frutas)  # Salida: ['fresa', 'cereza', 'naranja', 'kiwi']

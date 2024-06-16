# Crear dos conjuntos de letras
set1 = {"a", "b", "c", "d", "e"}
set2 = {"c", "d", "e", "f", "g"}

# Actualizar un conjunto con elementos de otro conjunto
set1.update(set2)
print("Set1 actualizado:", set1)  # Salida: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# Eliminar un elemento específico de un conjunto
set1.discard("b")
print("Set1 después de descartar 'b':", set1)  # Salida: {'a', 'c', 'd', 'e', 'f', 'g'}

# Vaciar un conjunto
set2.clear()
print("Set2 después de limpiar:", set2)  # Salida: set()

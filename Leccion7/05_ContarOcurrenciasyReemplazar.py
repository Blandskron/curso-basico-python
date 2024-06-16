# Tarea: Contar ocurrencias y reemplazar
frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme..."

# Contar cuántas veces aparece la letra 'a'
conteo_a = frase.count('a')
print(f"La letra 'a' aparece {conteo_a} veces.")

# Reemplazar "Mancha" por "mundo"
nueva_frase = frase.replace("Mancha", "mundo")
print("Frase modificada:", nueva_frase)

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Cadena de ejemplo
cadena = "Hola, Mundo"

# Calcular y mostrar la cantidad de vocales en la cadena
cantidad_vocales = contar_vocales(cadena)
print("La cantidad de vocales en la cadena es:", cantidad_vocales)

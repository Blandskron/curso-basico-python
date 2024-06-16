def cadena_mas_larga(cadenas):
    mas_larga = ""
    for cadena in cadenas:
        if len(cadena) > len(mas_larga):
            mas_larga = cadena
    return mas_larga

# Lista de cadenas
cadenas = ["manzana", "banana", "cereza", "kiwi"]

# Encontrar y mostrar la cadena más larga
larga = cadena_mas_larga(cadenas)
print("La cadena más larga es:", larga)

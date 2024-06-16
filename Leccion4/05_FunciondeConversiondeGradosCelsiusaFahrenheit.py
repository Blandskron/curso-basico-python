def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Pedir al usuario la temperatura en grados Celsius
temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir y mostrar la temperatura en grados Fahrenheit
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print("La temperatura en grados Fahrenheit es:", temp_fahrenheit)

# Programa que pide números al usuario hasta que introduzca un número negativo

while True:
    numero = float(input("Introduce un número: "))
    if numero < 0:
        print("Número negativo detectado, terminando el programa.")
        break
    print("Número introducido:", numero)

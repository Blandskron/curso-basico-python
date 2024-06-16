# Programa que pide el nombre y la edad del usuario y muestra un mensaje personalizado

# Pedir al usuario su nombre
nombre = input("Introduce tu nombre: ")

# Pedir al usuario su edad
edad = int(input("Introduce tu edad: "))

# Crear y mostrar el mensaje personalizado
mensaje = "Hola, " + nombre + ". Tienes " + str(edad) + " años."
print(mensaje)
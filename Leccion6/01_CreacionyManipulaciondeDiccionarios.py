# Crear un diccionario de estudiantes y sus calificaciones
calificaciones = {"Juan": 85, "María": 90, "Carlos": 78}

# Agregar un nuevo estudiante y su calificación
calificaciones["Ana"] = 95
print(calificaciones)  # Salida: {'Juan': 85, 'María': 90, 'Carlos': 78, 'Ana': 95}

# Eliminar la entrada de Carlos
del calificaciones["Carlos"]
print(calificaciones)  # Salida: {'Juan': 85, 'María': 90, 'Ana': 95}

# Obtener todas las claves del diccionario
print("Estudiantes:", calificaciones.keys())  # Salida: dict_keys(['Juan', 'María', 'Ana'])

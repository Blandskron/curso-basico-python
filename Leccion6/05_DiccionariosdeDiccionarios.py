# Crear un diccionario de diccionarios para almacenar información de estudiantes
estudiantes = {
    "Juan": {"edad": 25, "carrera": "Informática"},
    "María": {"edad": 23, "carrera": "Matemáticas"},
    "Ana": {"edad": 27, "carrera": "Física"}
}

# Acceder a la información de un estudiante específico
print("Información de Juan:", estudiantes["Juan"])  
# Salida: {'edad': 25, 'carrera': 'Informática'}

# Modificar la información de un estudiante
estudiantes["Ana"]["edad"] = 28
print("Información actualizada de Ana:", estudiantes["Ana"])  
# Salida: {'edad': 28, 'carrera': 'Física'}

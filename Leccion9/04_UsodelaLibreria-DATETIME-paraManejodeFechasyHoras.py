# Uso de la librería datetime
import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()
print(f"Fecha y hora actual: {fecha_actual}")

# Formatear la fecha y hora
fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
print(f"Fecha y hora formateada: {fecha_formateada}")

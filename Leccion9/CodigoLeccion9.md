# Guía Práctica de Código: Lección 9 (Módulos y Librería Estándar)

Esta guía detalla los scripts prácticos correspondientes a la **Lección 9**, que muestran cómo estructurar código e importar y utilizar las librerías nativas incorporadas en Python.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_ImportacionyUsoBasicodeModulos.py` | Importación completa de módulos estándar (`math`) | `python 01_ImportacionyUsoBasicodeModulos.py` |
| `02_UsodeFuncionesEspecificasdeModulos.py` | Importación selectiva de funciones con `from` | `python 02_UsodeFuncionesEspecificasdeModulos.py` |
| `03_UsodelaLibrerias-OS-paraImplementacionconelSistemaOperativo.py` | Interacción con el sistema operativo y directorios | `python 03_UsodelaLibrerias-OS-paraImplementacionconelSistemaOperativo.py` |
| `04_UsodelaLibreria-DATETIME-paraManejodeFechasyHoras.py` | Control de fechas, horas y cálculos temporales | `python 04_UsodelaLibreria-DATETIME-paraManejodeFechasyHoras.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Importación y Uso Básico de Módulos (`01_ImportacionyUsoBasicodeModulos.py`)
```python
# Importar el módulo completo math
import math

# Raíz cuadrada
raiz = math.sqrt(25)
print("Raíz cuadrada de 25:", raiz)

# Valor de Pi
print("Valor de Pi:", math.pi)
```
* **Explicación:** Importamos el espacio de nombres completo de `math`. Accedemos a sus funciones y constantes a través de la notación de punto.
* **Salida:**
  ```text
  Raíz cuadrada de 25: 5.0
  Valor de Pi: 3.141592653589793
  ```

---

### Ejemplo 2: Uso de Funciones Específicas de Módulos (`02_UsodeFuncionesEspecificasdeModulos.py`)
```python
# Importar funciones específicas de random
from random import randint, choice

# Generar un número entero aleatorio entre 1 y 10 (ambos inclusive)
numero_azar = randint(1, 10)
print("Número al azar:", numero_azar)

# Selección aleatoria de una lista
opciones = ["rojo", "verde", "azul", "amarillo"]
seleccion = choice(opciones)
print("Color seleccionado al azar:", seleccion)
```
* **Explicación:** Se importan de forma aislada las utilidades `randint` y `choice`. Esto nos permite invocarlas directamente por su nombre, manteniendo el código limpio de prefijos redundantes.

---

### Ejemplo 3: Uso de la Librería `os` (`03_UsodelaLibrerias-OS-paraImplementacionconelSistemaOperativo.py`)
```python
import os

# Obtener directorio de trabajo actual
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)

# Listar los archivos en el directorio actual
archivos = os.listdir(directorio_actual)
print("Archivos en la carpeta:")
for archivo in archivos:
    print("-", archivo)
```
* **Explicación:** Demuestra el uso del módulo `os` para leer directorios físicos del equipo y comprobar rutas.
* **Salida:** *(Dependerá del equipo local del usuario)*
  ```text
  Directorio de trabajo actual: C:\Users\BlandskronNotebook\Documents\updatesGitHubs\CursoBasicoPython\Leccion9
  Archivos en la carpeta:
  - 01_ImportacionyUsoBasicodeModulos.py
  - 02_UsodeFuncionesEspecificasdeModulos.py
  - 03_UsodelaLibrerias-OS-paraImplementacionconelSistemaOperativo.py
  - 04_UsodelaLibreria-DATETIME-paraManejodeFechasyHoras.py
  - CodigoLeccion9.md
  - Leccion9.md
  ```

---

### Ejemplo 4: Uso de la Librería `datetime` (`04_UsodelaLibreria-DATETIME-paraManejodeFechasyHoras.py`)
```python
import datetime

# Obtener fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# Obtener solo la fecha de hoy
hoy = datetime.date.today()
print("Fecha de hoy:", hoy)

# Formatear la fecha en formato legible (Día/Mes/Año)
fecha_formateada = hoy.strftime("%d/%m/%Y")
print("Fecha formateada:", fecha_formateada)
```
* **Explicación:** Se manipulan marcas temporales. Resalta el método `.strftime()`, que nos permite transformar fechas nativas de Python a cadenas legibles personalizables usando directivas (ej. `%d` para día, `%m` para mes, `%Y` para año con 4 dígitos).
* **Salida:** *(Dependerá de la fecha en la que se ejecute el script)*
  ```text
  Fecha y hora actual: 2026-06-07 00:42:43.123456
  Fecha de hoy: 2026-06-07
  Fecha formateada: 07/06/2026
  ```

# Lección 9: Módulos y Librería Estándar (Modulariad)

Esta lección introduce el concepto de modularidad en Python, enseñándote a estructurar tu código en múltiples archivos y a aprovechar las potentes librerías que vienen integradas en el ecosistema estándar de Python.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Comprender** el concepto de módulo y paquete en Python.
2. **Utilizar** las diferentes sintaxis de importación (`import`, `from ... import`, `as`).
3. **Emplear** las librerías matemáticas (`math`) y de azares (`random`) para resolver problemas de cómputo común.
4. **Interactuar** con el sistema operativo utilizando la librería `os` y manipular objetos temporales mediante `datetime`.

---

## 📖 Contenido Conceptual

### 1. ¿Qué es un Módulo?
Un módulo es un archivo que contiene definiciones de funciones, clases y variables escritas en Python (es decir, cualquier archivo `.py`). Permite fragmentar proyectos extensos en componentes independientes y reutilizables.

#### Sintaxis de Importación

* **Importación General:** Importa todo el archivo bajo su espacio de nombres. Requiere usar la notación de punto para acceder a sus funciones.
  ```python
  import math
  print(math.sqrt(16))
  ```
* **Importación Selectiva:** Extrae únicamente los elementos específicos que necesitas, colocándolos directamente en el espacio de nombres local.
  ```python
  from math import sqrt
  print(sqrt(16))  # No requiere anteponer "math."
  ```
* **Alias de Módulos:** Sobrescribe el nombre del módulo con un alias más corto o descriptivo.
  ```python
  import random as rd
  print(rd.randint(1, 10))
  ```

---

### 2. Catálogo de Librerías Estándar Fundamentales

Python incorpora cientos de módulos listos para usar. En este curso exploraremos cuatro pilares básicos:

| Módulo | Utilidad Primaria | Funciones Comunes |
| :--- | :--- | :--- |
| **`math`** | Cálculos numéricos avanzados y constantes trigonométricas. | `sqrt()` (raíz cuadrada), `pow()` (potencia), `pi` (constante $\pi$), `ceil()` (redondeo hacia arriba). |
| **`random`** | Generación de números pseudoaleatorios y selecciones al azar. | `randint(a, b)` (entero aleatorio), `choice(sec)` (elemento al azar), `shuffle(lst)` (mezclar lista). |
| **`os`** | Interacción directa con el sistema de archivos y el sistema operativo. | `getcwd()` (ruta actual), `listdir(path)` (listar directorios), `mkdir()` (crear carpeta), `path.exists()`. |
| **`datetime`**| Manipulación y formateo de fechas y horas del sistema. | `date.today()`, `datetime.now()`, `strftime()` (dar formato a fechas). |

> [!WARNING]
> Evita usar nombres de archivos propios que coincidan con módulos estándar (por ejemplo, no llames a tu script de prácticas `random.py`). Si lo haces, Python intentará importar tu archivo en lugar del oficial, generando errores de importación difíciles de detectar.

---

## 📝 Resumen de la Lección
* Los módulos permiten estructurar y empaquetar código reutilizable.
* Podemos usar `import`, `from ... import` o cambiar el nombre local del módulo con `as`.
* La **Librería Estándar** es una colección de herramientas nativas de Python que no requieren instalaciones adicionales (`math`, `random`, `os`, `datetime`, entre otras).

---

## 🏋️ Desafíos Prácticos
Demuestra tu dominio de las librerías estándar completando estas consignas:

1. **Juego de Dados:** Escribe una función llamada `lanzar_dados()` que simule el lanzamiento de dos dados de 6 caras utilizando `random.randint()`. Retorna la suma de ambos resultados y un mensaje que muestre los valores obtenidos.
2. **Organizador de Archivos:** Escribe un script que utilice la librería `os` para comprobar si existe una carpeta llamada `CopiasDeSeguridad`. Si no existe, créala automáticamente mediante `os.mkdir()`. En caso de que ya exista, lista e imprime todos los archivos contenidos en ella.
3. **Calculadora de Edad:** Diseña un programa que le pida al usuario su fecha de nacimiento (año, mes y día) e imprima exactamente cuántos días de vida tiene transcurridos hasta el día de hoy utilizando el módulo `datetime`.

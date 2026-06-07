# Guía Práctica de Código: Lección 7 (Manejo de Cadenas)

Esta guía recopila y detalla los scripts prácticos correspondientes a la **Lección 7**, enfocados en operaciones lógicas, formateo e inspección de texto.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_OperacionesBasicasconCadenas.py` | Concatenación, repetición y cálculo de longitud | `python 01_OperacionesBasicasconCadenas.py` |
| `02_MetodosdeCadenas.py` | Conversión de mayúsculas, minúsculas y eliminación de espacios | `python 02_MetodosdeCadenas.py` |
| `03_FormateodeCadenascon-F-STRINGS.py` | Uso moderno de interpolación `f-strings` | `python 03_FormateodeCadenascon-F-STRINGS.py` |
| `04_FormateodeCadenasconelMetodo-FORMAT().py` | Uso de marcadores de posición con `.format()` | `python 04_FormateodeCadenasconelMetodo-FORMAT().py` |
| `05_ContarOcurrenciasyReemplazar.py` | Métodos `.count()` y `.replace()` | `python 05_ContarOcurrenciasyReemplazar.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Operaciones Básicas con Cadenas (`01_OperacionesBasicasconCadenas.py`)
```python
cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación
concatenada = cadena1 + " " + cadena2
print("Concatenada:", concatenada)

# Repetición
repetida = cadena1 * 3
print("Repetida:", repetida)

# Longitud
print("Longitud:", len(concatenada))
```
* **Explicación:** Se muestra cómo unir textos con `+`, replicar cadenas usando el operador de producto `*` e inspeccionar el número de caracteres (incluyendo espacios) con la función `len()`.
* **Salida:**
  ```text
  Concatenada: Hola Mundo
  Repetida: HolaHolaHola
  Longitud: 10
  ```

---

### Ejemplo 2: Métodos de Cadenas (`02_MetodosdeCadenas.py`)
```python
texto = "   Hola, Python!   "

# Métodos de transformación
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Sin espacios extras (strip):", texto.strip())
```
* **Salida:**
  ```text
  Mayúsculas:    HOLA, PYTHON!   
  Minúsculas:    hola, python!   
  Sin espacios extras (strip): Hola, Python!
  ```

---

### Ejemplo 3: Formateo de Cadenas con F-Strings (`03_FormateodeCadenascon-F-STRINGS.py`)
```python
nombre = "Bastian"
edad = 24

# Interpolación directa
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
```
* **Salida:**
  ```text
  Hola, mi nombre es Bastian y tengo 24 años.
  ```

---

### Ejemplo 4: Formateo de Cadenas con el Método `format()` (`04_FormateodeCadenasconelMetodo-FORMAT().py`)
```python
nombre = "Bastian"
edad = 24

# Formateo tradicional
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)
```
* **Salida:**
  ```text
  Hola, mi nombre es Bastian y tengo 24 años.
  ```

---

### Ejemplo 5: Contar Ocurrencias y Reemplazar (`05_ContarOcurrenciasyReemplazar.py`)
```python
frase = "Python es genial y aprender Python es divertido."

# Contar apariciones de una palabra
cantidad = frase.count("Python")
print("Veces que aparece 'Python':", cantidad)

# Reemplazar palabra
nueva_frase = frase.replace("Python", "Programación")
print("Frase modificada:", nueva_frase)
```
* **Salida:**
  ```text
  Veces que aparece 'Python': 2
  Frase modificada: Programación es genial y aprender Programación es divertido.
  ```
</div>

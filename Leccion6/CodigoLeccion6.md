# Guía Práctica de Código: Lección 6 (Diccionarios y Conjuntos)

Esta guía recopila y detalla los scripts prácticos correspondientes a la **Lección 6**, enfocados en estructuras de datos asociativas (diccionarios) y de elementos únicos (conjuntos).

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_CreacionyManipulaciondeDiccionarios.py` | Definición de diccionarios, inserción y eliminación | `python 01_CreacionyManipulaciondeDiccionarios.py` |
| `02_MetodosyOperacionesconDiccionarios.py` | Métodos `.get()`, `.keys()`, `.values()` e `.items()` | `python 02_MetodosyOperacionesconDiccionarios.py` |
| `03_CreacionyOperacionesconConjuntos.py` | Creación de conjuntos y eliminación de duplicados | `python 03_CreacionyOperacionesconConjuntos.py` |
| `04_OperacionesAvanzadasconConjuntos.py` | Álgebra de conjuntos (uniones, intersecciones, etc.) | `python 04_OperacionesAvanzadasconConjuntos.py` |
| `05_DiccionariosdeDiccionarios.py` | Estructuras de datos mapeadas anidadas | `python 05_DiccionariosdeDiccionarios.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Creación y Manipulación de Diccionarios (`01_CreacionyManipulaciondeDiccionarios.py`)
```python
# Crear un diccionario de un producto
producto = {
    "nombre": "Laptop",
    "precio": 800,
    "stock": 10
}
print("Producto inicial:", producto)

# Modificar un valor
producto["precio"] = 750

# Agregar un nuevo par clave-valor
producto["marca"] = "BrandX"

# Eliminar una clave
del producto["stock"]

print("Producto modificado:", producto)
```
* **Explicación:** Declaramos una estructura clave-valor. Mostramos cómo reescribir una clave (`precio`), añadir una clave nueva (`marca`), y remover permanentemente una propiedad (`stock`) usando `del`.
* **Salida:**
  ```text
  Producto inicial: {'nombre': 'Laptop', 'precio': 800, 'stock': 10}
  Producto modificado: {'nombre': 'Laptop', 'precio': 750, 'marca': 'BrandX'}
  ```

---

### Ejemplo 2: Métodos y Operaciones con Diccionarios (`02_MetodosyOperacionesconDiccionarios.py`)
```python
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Ingeniería"
}

# Obtener valor de forma segura
print("Correo:", estudiante.get("correo", "No registrado"))

# Obtener claves, valores e ítems
print("Claves:", list(estudiante.keys()))
print("Valores:", list(estudiante.values()))
print("Ítems (Pares):", list(estudiante.items()))
```
* **Explicación:** Se ilustra la robustez de `.get()`. Adicionalmente, extraemos las claves, valores y tuplas asociativas (`items`) para poder convertirlas o recorrerlas con facilidad.
* **Salida:**
  ```text
  Correo: No registrado
  Claves: ['nombre', 'edad', 'carrera']
  Valores: ['Ana', 22, 'Ingeniería']
  Ítems (Pares): [('nombre', 'Ana'), ('edad', 22), ('carrera', 'Ingeniería')]
  ```

---

### Ejemplo 3: Creación y Operaciones con Conjuntos (`03_CreacionyOperacionesconConjuntos.py`)
```python
# Crear un conjunto con duplicados
numeros = {1, 2, 2, 3, 4, 4, 5}
print("Conjunto (valores únicos):", numeros)

# Agregar elementos
numeros.add(6)

# Eliminar elementos
numeros.remove(3)

print("Conjunto modificado:", numeros)
```
* **Explicación:** El intérprete filtra los duplicados de forma interna al inicializar el set. Usamos `.add()` y `.remove()` para gestionar sus valores.
* **Salida:**
  ```text
  Conjunto (valores únicos): {1, 2, 3, 4, 5}
  Conjunto modificado: {1, 2, 4, 5, 6}
  ```

---

### Ejemplo 4: Operaciones Avanzadas con Conjuntos (`04_OperacionesAvanzadasconConjuntos.py`)
```python
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}

# Unión
print("Unión (A | B):", grupo_a | grupo_b)

# Intersección
print("Intersección (A & B):", grupo_a & grupo_b)

# Diferencia (elementos de A que no están en B)
print("Diferencia (A - B):", grupo_a - grupo_b)

# Diferencia simétrica
print("Diferencia Simétrica (A ^ B):", grupo_a ^ grupo_b)
```
* **Salida:**
  ```text
  Unión (A | B): {1, 2, 3, 4, 5, 6}
  Intersección (A & B): {3, 4}
  Diferencia (A - B): {1, 2}
  Diferencia Simétrica (A ^ B): {1, 2, 5, 6}
  ```

---

### Ejemplo 5: Diccionarios de Diccionarios (`05_DiccionariosdeDiccionarios.py`)
```python
# Estructura de base de datos escolar
escuela = {
    "grupo_1": {
        "profesor": "Gómez",
        "alumnos": ["Juan", "María"]
    },
    "grupo_2": {
        "profesor": "Pérez",
        "alumnos": ["Carlos", "Ana"]
    }
}

# Acceso anidado
print("Profesor del Grupo 1:", escuela["grupo_1"]["profesor"])
print("Alumnos del Grupo 2:", escuela["grupo_2"]["alumnos"])
```
* **Explicación:** Demuestra el modelado de datos jerárquico. Se encadenan llaves de acceso para profundizar en el diccionario anidado.
* **Salida:**
  ```text
  Profesor del Grupo 1: Gómez
  Alumnos del Grupo 2: ['Carlos', 'Ana']
  ```

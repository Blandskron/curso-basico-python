# Guía Práctica de Código: Lección 5 (Listas y Tuplas)

Esta guía documenta los scripts prácticos correspondientes a la **Lección 5**, enfocados en la manipulación de arreglos dinámicos (listas) y estructuras de solo lectura (tuplas).

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_CreacionyManipulaciondeListas.py` | Métodos mutables básicos de listas | `python 01_CreacionyManipulaciondeListas.py` |
| `02_AccesoaElementosySublitas.py` | Indexación simple y extracción de sublistas | `python 02_AccesoaElementosySublitas.py` |
| `03_CreacionyAccesoaElementosdeTuplas.py` | Declaración y acceso a tuplas | `python 03_CreacionyAccesoaElementosdeTuplas.py` |
| `04_DiferenciasentreListasyTuplas.py` | Evidencia de mutabilidad vs inmutabilidad | `python 04_DiferenciasentreListasyTuplas.py` |
| `05_UsoAvanzadodeSlicingenListas.py` | Segmentación avanzada de secuencias | `python 05_UsoAvanzadodeSlicingenListas.py` |
| `06_TuplasAnidadas.py` | Estructuras complejas multidimensionales | `python 06_TuplasAnidadas.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Creación y Manipulación de Listas (`01_CreacionyManipulaciondeListas.py`)
```python
# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas)

# Acceder a elementos de la lista
print("Primera fruta:", frutas[0])

# Agregar una nueva fruta a la lista
frutas.append("durazno")
print("Lista actualizada de frutas:", frutas)
```
* **Explicación:** Se inicializa una lista con tres strings. Mediante `.append()`, se añade de forma mutable `"durazno"` al final de la misma.
* **Salida:**
  ```text
  Lista de frutas: ['manzana', 'banana', 'cereza']
  Primera fruta: manzana
  Lista actualizada de frutas: ['manzana', 'banana', 'cereza', 'durazno']
  ```

---

### Ejemplo 2: Acceso a Elementos y Sublistas (`02_AccesoaElementosySublitas.py`)
```python
numeros = [10, 20, 30, 40, 50]

# Acceso directo
print("Elemento en índice 2:", numeros[2])

# Sublista (Slicing) del índice 1 al 4 (excluyente)
print("Sublista [1:4]:", numeros[1:4])
```
* **Salida:**
  ```text
  Elemento en índice 2: 30
  Sublista [1:4]: [20, 30, 40]
  ```

---

### Ejemplo 3: Creación y Acceso a Elementos de Tuplas (`03_CreacionyAccesoaElementosdeTuplas.py`)
```python
# Declaración de una tupla de coordenadas
coordenadas = (10.0, 20.0)

print("Coordenadas completas:", coordenadas)
print("Latitud (X):", coordenadas[0])
print("Longitud (Y):", coordenadas[1])
```
* **Salida:**
  ```text
  Coordenadas completas: (10.0, 20.0)
  Latitud (X): 10.0
  Longitud (Y): 20.0
  ```

---

### Ejemplo 4: Diferencias entre Listas y Tuplas (`04_DiferenciasentreListasyTuplas.py`)
```python
# Lista (Mutable)
mi_lista = [1, 2, 3]
mi_lista[0] = 10
print("Lista modificada:", mi_lista)

# Tupla (Inmutable)
mi_tupla = (1, 2, 3)
try:
    mi_tupla[0] = 10
except TypeError as e:
    print("Error al intentar modificar tupla:", e)
```
* **Explicación:** Este ejemplo demuestra de forma práctica la inmutabilidad de las tuplas. Si intentamos alterar un valor de la tupla, Python levanta un error de tipo `TypeError`. Usamos un bloque `try-except` para evitar que el script falle abruptamente.
* **Salida:**
  ```text
  Lista modified: [10, 2, 3]
  Error al intentar modificar tupla: 'tuple' object does not support item assignment
  ```

---

### Ejemplo 5: Uso Avanzado de Slicing en Listas (`05_UsoAvanzadodeSlicingenListas.py`)
```python
valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing con paso
print("Impares (desde índice 1 en pasos de 2):", valores[1::2])

# Invertir lista
print("Valores invertidos:", valores[::-1])
```
* **Salida:**
  ```text
  Impares (desde índice 1 en pasos de 2): [1, 3, 5, 7, 9]
  Valores invertidos: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  ```

---

### Ejemplo 6: Tuplas Anidadas (`06_TuplasAnidadas.py`)
```python
# Matriz o tupla que contiene otras tuplas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Fila 1 completa:", matriz[0])
print("Elemento central (Fila 2, Columna 2):", matriz[1][1])
```
* **Explicación:** Se accede a la estructura anidada indicando los índices consecutivos: el primer corchete indica la fila y el segundo la columna.
* **Salida:**
  ```text
  Fila 1 completa: (1, 2, 3)
  Elemento central (Fila 2, Columna 2): 5
  ```

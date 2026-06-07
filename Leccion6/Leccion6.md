# Lección 6: Diccionarios y Conjuntos (Colecciones No Secuenciales)

Esta lección cubre las colecciones no indexadas secuencialmente: los Diccionarios (basados en mapeo de clave-valor) y los Conjuntos (basados en unicidad de elementos).

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Crear y manipular** diccionarios (`dict`) para almacenar y recuperar información mediante claves personalizadas.
2. **Utilizar** los métodos más comunes de diccionarios (como `.keys()`, `.values()`, `.items()`, y `.get()`).
3. **Declarar** conjuntos (`set`) y utilizarlos para eliminar valores duplicados.
4. **Realizar** operaciones algebraicas de conjuntos (Unión, Intersección, Diferencia y Diferencia Simétrica).

---

## 📖 Contenido Conceptual

### 1. Diccionarios (`dict`)
Un diccionario es una colección desordenada (a partir de Python 3.7 preservan el orden de inserción de forma interna), modificable y mapeada. En lugar de acceder a los elementos mediante índices numéricos, los diccionarios utilizan un sistema de **Clave-Valor** (`key-value`).

Se definen utilizando llaves `{}` con la estructura `clave: valor`:

```python
usuario = {
    "nombre": "Bastian",
    "edad": 24,
    "es_instructor": True
}
```

#### Reglas de los Diccionarios
* **Claves Únicas:** No puede haber claves duplicadas en un mismo diccionario. Si asignas un valor a una clave existente, el valor anterior se sobrescribe.
* **Claves Inmutables:** Las claves deben ser de un tipo de datos inmutable (generalmente cadenas de texto, números enteros o tuplas).

> [!TIP]
> **Evitar errores de Clave Inexistente:** Si intentas acceder a una clave que no existe mediante `usuario["correo"]`, Python lanzará un error `KeyError`. Para evitarlo de manera limpia, utiliza el método `usuario.get("correo", "Valor por defecto")`, el cual devuelve `None` (o el valor alternativo indicado) en lugar de fallar.

---

### 2. Conjuntos (`set`)
Un conjunto es una colección **desordenada**, **no indexada** y que **no admite elementos duplicados**. Son muy útiles para filtrar duplicados de listas de forma masiva y realizar operaciones matemáticas de conjuntos.

Se definen utilizando llaves `{}` (sin la notación de dos puntos de clave-valor) o mediante el constructor `set()`:

```python
frutas_unicas = {"manzana", "platano", "manzana"}
print(frutas_unicas)  # Salida: {'manzana', 'platano'}
```

---

### 3. Operaciones de Álgebra de Conjuntos
Python cuenta con operadores lógicos específicos para realizar operaciones sobre conjuntos:

| Operación Matemática | Operador en Python | Método Equivalente | Descripción |
| :--- | :---: | :--- | :--- |
| **Unión** | `A \| B` | `A.union(B)` | Elementos en A, en B o en ambos. |
| **Intersección** | `A & B` | `A.intersection(B)` | Elementos presentes en ambos conjuntos. |
| **Diferencia** | `A - B` | `A.difference(B)` | Elementos en A que no pertenecen a B. |
| **Diferencia Simétrica** | `A ^ B` | `A.symmetric_difference(B)` | Elementos en A o en B, pero no en ambos. |

---

## 📝 Resumen de la Lección
* Los diccionarios (`dict`) asocian claves inmutables con valores de cualquier clase.
* Para recuperar valores de forma segura sin generar excepciones se usa el método `.get()`.
* Los conjuntos (`set`) almacenan elementos únicos no ordenados.
* Python soporta de forma nativa las operaciones matemáticas de conjuntos como unión (`|`), intersección (`&`) y diferencia (`-`).

---

## 🏋️ Desafíos Prácticos
Pon a prueba lo aprendido resolviendo las siguientes problemáticas:

1. **Gestor de Contactos:** Crea un diccionario que represente un contacto de teléfono (nombre, celular, correo). Agrega una nueva clave para la dirección de residencia, actualiza el correo electrónico y elimina la clave del celular. Muestra el estado del diccionario en cada paso.
2. **Control de Inventario Escolar:** Dadas las listas de alumnos inscritos en el curso de matemáticas `mate = ["Juan", "Ana", "Pedro", "Luis"]` y en el curso de física `fisica = ["Ana", "Pedro", "Carlos", "Sofia"]`:
   * Convierte ambas listas a conjuntos.
   * Encuentra los alumnos inscritos en **ambos** cursos (Intersección).
   * Encuentra los alumnos inscritos únicamente en matemáticas pero **no** en física (Diferencia).
   * Genera la lista única de todos los alumnos inscritos al menos en un curso (Unión).
3. **Limpieza de Duplicados:** Escribe un script que tome una lista con elementos repetidos: `[1, 2, 2, 3, 4, 4, 4, 5, 1, 6]` y devuelva una nueva lista con los elementos únicos ordenados de menor a mayor.

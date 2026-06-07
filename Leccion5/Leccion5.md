# Lección 5: Listas y Tuplas (Colecciones de Datos)

Esta lección introduce el concepto de estructuras de datos secuenciales, enfocándose en las similitudes, diferencias y casos de uso de las Listas y las Tuplas.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Crear y manipular** listas dinámicas (mutables) y tuplas (inmutables).
2. **Acceder** a elementos individuales utilizando indexación positiva y negativa.
3. **Extraer** porciones de colecciones mediante rebanado o corte (Slicing).
4. **Distinguir** cuándo es óptimo usar una lista frente a una tupla basándote en la mutabilidad y el rendimiento.

---

## 📖 Contenido Conceptual

### 1. Listas (Mutables)
Una lista es una colección ordenada y modificable de elementos. En Python, se definen delimitando los elementos con corchetes `[]` y separándolos por comas. Pueden almacenar múltiples tipos de datos simultáneamente.

```python
mi_lista = [10, "Python", True, 3.14]
```

#### Características Clave
* **Ordenadas:** El orden de inserción se mantiene de manera estricta.
* **Mutables:** Es posible modificar, añadir, reordenar o eliminar sus elementos una vez creada.

---

### 2. Tuplas (Inmutables)
Una tupla es una colección ordenada e **inmodificable**. Se definen encerrando sus valores entre paréntesis `()`.

```python
mi_tupla = (10, "Python", True, 3.14)
```

#### Características Clave
* **Inmutables:** Una vez definida una tupla, no se puede alterar su contenido (no se pueden añadir, eliminar o reescribir elementos).
* **Eficiencia:** Al ser de tamaño fijo, consumen menos memoria en el sistema y se procesan más rápido que las listas.

#### Comparativa Rápida

| Propiedad | Listas (`list`) | Tuplas (`tuple`) |
| :--- | :---: | :---: |
| **Sintaxis** | Corchetes `[]` | Paréntesis `()` |
| **Mutable** | Sí | No |
| **Uso común** | Colección homogénea que cambia con el tiempo | Datos fijos, registros (ej. coordenadas `(x, y)`) |
| **Rendimiento** | Más lento en memoria | Más rápido en memoria |

---

### 3. Sistemas de Indexación y Rebanado (Slicing)

#### Indexación Positiva y Negativa
Python asigna un índice de posición a cada elemento de la colección, permitiendo acceder desde el inicio (comenzando en `0`) o desde el final (utilizando números negativos comenzando en `-1`).

| Elemento | `'P'` | `'y'` | `'t'` | `'h'` | `'o'` | `'n'` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Índice Positivo** | 0 | 1 | 2 | 3 | 4 | 5 |
| **Índice Negativo** | -6 | -5 | -4 | -3 | -2 | -1 |

#### Rebanado o Slicing
El rebanado nos permite extraer subconjuntos de datos a partir de una secuencia utilizando la nomenclatura `coleccion[inicio:fin:paso]`.

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraer del índice 2 al 5 (excluyente)
print(numeros[2:5])  # Salida: [2, 3, 4]

# Extraer con saltos de paso 2
print(numeros[::2])  # Salida: [0, 2, 4, 6, 8]

# Invertir una lista completa
print(numeros[::-1])  # Salida: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

> [!TIP]
> Si omites `inicio`, Python asumirá el comienzo (índice 0). Si omites `fin`, asumirá el final del contenedor.

---

## 📝 Resumen de la Lección
* Las listas (`list`) se definen con corchetes `[]` y son dinámicas/mutables.
* Las tuplas (`tuple`) se definen con paréntesis `()` y son estáticas/inmutables.
* Los índices positivos van de `0` a `longitud - 1`, mientras que los negativos van de `-1` a `-longitud`.
* El Slicing `[start:stop:step]` es una técnica muy potente para segmentar y manipular subcolecciones.

---

## 🏋️ Desafíos Prácticos
Completa los siguientes ejercicios aplicando las técnicas de esta sesión:

1. **Manipulador de Tareas:** Crea una lista de tareas pendientes. Agrega 2 tareas nuevas al final usando `.append()`, inserta otra en la primera posición utilizando `.insert(0, tarea)` y elimina la última usando `.pop()`. Muestra la lista resultante.
2. **Empaquetado de Datos:** Define una tupla que represente los datos de un libro: `(titulo, autor, anio_publicacion)`. Intenta cambiar el año de publicación. Registra el error obtenido y explica por qué sucede.
3. **Extracción de Rangos:** Dada la lista `valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`, obtén y muestra:
   * Los primeros 3 elementos.
   * Los últimos 2 elementos usando índices negativos.
   * La sublista invertida que contenga desde el elemento `70` al `30`.

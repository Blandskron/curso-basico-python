# Lección 2: Variables y Tipos de Datos

Esta lección cubre las bases de cómo almacenar información en memoria y manipular diferentes clases de valores como números, textos y estados de verdad.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Definir** qué es una variable y comprender el concepto de tipado dinámico en Python.
2. **Reconocer y emplear** los cuatro tipos de datos primordiales: Enteros (`int`), Flotantes (`float`), Cadenas de texto (`str`) y Booleanos (`bool`).
3. **Efectuar** operaciones matemáticas elementales y lógicas con variables.
4. **Realizar** conversiones de tipo de datos (casting) de forma explícita.

---

## 📖 Contenido Conceptual

### 1. Variables y Tipado Dinámico
Una variable es un identificador o nombre que apunta a una ubicación de almacenamiento en la memoria física de la computadora. En Python, la asignación se realiza mediante el operador `=`.

```python
edad = 25
```

> [!NOTE]
> **Tipado Dinámico:** A diferencia de lenguajes como C++ o Java, en Python no necesitas indicar explícitamente si tu variable guardará un número o un texto. El intérprete deduce el tipo de forma automática basándose en el valor asignado y permite que una misma variable cambie de tipo en cualquier momento.

#### Reglas de Nomenclatura para Variables
* Deben iniciar con una letra o guion bajo (`_`).
* No pueden iniciar con números.
* Solo contienen caracteres alfanuméricos y guiones bajos (`a-z`, `A-Z`, `0-9`, `_`).
* Son sensibles a mayúsculas y minúsculas (Case-Sensitive): `total` y `Total` son variables distintas.
* No pueden utilizarse palabras reservadas del lenguaje (como `if`, `while`, `import`, etc.).

---

### 2. Tipos de Datos Primitivos

| Nombre Técnico | Tipo en Python | Descripción | Ejemplo |
| :--- | :---: | :--- | :--- |
| **Entero** | `int` | Números enteros positivos o negativos, sin decimales. | `contador = 100` |
| **Flotante** | `float` | Números con parte fraccionaria o decimal. | `precio = 19.99` |
| **Cadena de Texto** | `str` | Colección ordenada de caracteres delimitados por comillas simples (`'`) o dobles (`"`). | `curso = "Curso de Python"` |
| **Booleano** | `bool` | Valores lógicos de verdad, únicamente pueden ser verdadero o falso. | `activo = True` |

---

### 3. Operaciones Básicas y Aritméticas

Python soporta todos los operadores matemáticos estándar:

* **Suma (`+`)**
* **Resta (`-`)**
* **Multiplicación (`*`)**
* **División (`/`):** Produce siempre un número flotante (`float`), incluso si la división es exacta.
* **División Entera (`//`):** Trunca la parte decimal, devolviendo únicamente la parte entera del cociente.
* **Módulo (`%`):** Devuelve el residuo de una división entera.
* **Exponenciación (`**`):** Eleva un número a la potencia de otro.

> [!WARNING]
> La división por cero (ej. `x / 0` o `x // 0`) genera un error de tiempo de ejecución de tipo `ZeroDivisionError`. Debes asegurarte de validar los denominadores antes de realizar estas operaciones.

---

### 4. Conversión de Tipos de Datos (Casting)
En ocasiones es indispensable forzar la transformación de un dato a otro tipo (por ejemplo, convertir una cadena de texto ingresada por teclado a número entero para poder operarla matemáticamente).

Para ello se utilizan funciones constructoras integradas:
* `int(valor)`: Convierte el valor a entero.
* `float(valor)`: Convierte el valor a flotante.
* `str(valor)`: Convierte el valor a representación de texto.
* `bool(valor)`: Evalúa el valor bajo lógica booleana (cualquier número distinto de cero y cualquier cadena no vacía se evalúan como `True`).

---

## 📝 Resumen de la Lección
* Las variables sirven para etiquetar y hacer referencia a datos en memoria.
* Python deduce automáticamente el tipo de dato de una variable (tipado dinámico).
* Los tipos básicos son `int`, `float`, `str` y `bool`.
* Se pueden realizar operaciones matemáticas y lógicas directamente sobre variables del mismo tipo.
* El "Casting" permite convertir variables entre diferentes tipos de datos manualmente.

---

## 🏋️ Desafíos Prácticos
Desarrolla tus habilidades resolviendo estos ejercicios en tu entorno local:

1. **Calculadora Tributaria:** Define una variable `ingreso_mensual` con un valor flotante y calcula el impuesto a pagar correspondiente al 19%. Muestra el resultado de forma legible.
2. **Casting Seguro:** Intenta forzar la conversión de la cadena `"123.45"` a un entero utilizando `int()`. ¿Qué sucede? Investiga cuál es la forma correcta de realizar esta conversión en dos pasos.
3. **Tabla Lógica:** Crea un script que declare dos variables booleanas `p = True` y `q = False`. Imprime en consola la salida de la expresión `(p or q) and not (p and q)`. Explica qué operación lógica representa.

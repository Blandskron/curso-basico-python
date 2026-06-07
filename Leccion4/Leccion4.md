# Lección 4: Funciones en Python

Esta lección enseña la importancia de modularizar y organizar el código en bloques lógicos reutilizables mediante la declaración y el uso de funciones.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Declarar** e invocar funciones personalizadas utilizando la palabra clave `def`.
2. **Gestionar** el paso de parámetros, incluyendo argumentos obligatorios, posicionales y parámetros por defecto.
3. **Controlar** el retorno de valores simples y múltiples utilizando la palabra clave `return`.
4. **Comprender** el ámbito de las variables (ámbito local vs. ámbito global).
5. **Aplicar** buenas prácticas de documentación de funciones utilizando Docstrings.

---

## 📖 Contenido Conceptual

### 1. ¿Qué es una Función?
Una función es un bloque de código organizado y reutilizable que se diseña para realizar una única tarea específica. Las funciones ayudan a evitar la repetición de código (filosofía DRY: *Don't Repeat Yourself*) y facilitan las tareas de depuración y prueba.

#### Anatomía de una Función en Python

```python
def nombre_de_la_funcion(parametro1, parametro2):
    """
    Docstring: Descripción breve de lo que hace la función.
    """
    # Cuerpo de la función (Bloque indentado)
    resultado = parametro1 + parametro2
    return resultado
```

* **`def`:** Palabra clave que inicia la declaración.
* **Nombre de la función:** Identificador de la función (se recomienda usar minúsculas y guiones bajos: snake_case).
* **Parámetros:** Variables entre paréntesis que reciben los argumentos al invocar la función (opcional).
* **Cuerpo de la función:** Bloque indentado que contiene la lógica.
* **`return`:** Devuelve un valor al punto donde se llamó la función e interrumpe de inmediato su ejecución (opcional, si se omite, la función devuelve `None`).

---

### 2. Parámetros por Defecto
Python permite asignar valores predeterminados a los parámetros en la firma de la función. Si al invocar la función se omite dicho argumento, se usará el valor por defecto configurado.

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")
```

> [!WARNING]
> Todos los parámetros que tengan valores por defecto deben colocarse **al final** de la lista de parámetros en la firma de la función. De lo contrario, Python lanzará un error de sintaxis (`SyntaxError: non-default argument follows default argument`).

---

### 3. Ámbito de las Variables (Scope)
El lugar del código donde declaras una variable determina su ciclo de vida y visibilidad:

* **Ámbito Local:** Variables definidas dentro de una función. Solo existen y pueden ser accedidas mientras la función se está ejecutando.
* **Ámbito Global:** Variables definidas en el cuerpo principal del script. Son accesibles desde cualquier lugar del archivo, incluso dentro de las funciones.

> [!TIP]
> Intenta evitar el uso de variables globales dentro de tus funciones. Es una mejor práctica pasar la información necesaria explícitamente a través de parámetros y retornar los resultados requeridos.

---

### 4. Introducción a Type Hints (Anotaciones de Tipo)
Aunque Python es un lenguaje de tipado dinámico, la documentación profesional actual promueve el uso de anotaciones de tipo para mejorar la legibilidad y ayudar a las herramientas de desarrollo a detectar errores:

```python
def duplicar_numero(numero: float) -> float:
    return numero * 2
```
* `: float` indica que el parámetro esperado es un número flotante.
* `-> float` indica que la función retornará un valor flotante.

---

## 📝 Resumen de la Lección
* Las funciones se definen con `def` y estructuran el código para evitar repeticiones.
* Los parámetros permiten ingresar información externa a la función, y `return` envía de vuelta un resultado procesado.
* Los parámetros por defecto se declaran al final de la firma.
* Las variables declaradas dentro de una función son locales a la misma.
* Se aconseja documentar las funciones usando Docstrings explicativos.

---

## 🏋️ Desafíos Prácticos
Prueba a resolver los siguientes retos prácticos escribiendo funciones en tu computadora:

1. **Calculadora de IMC:** Escribe una función llamada `calcular_imc(peso: float, altura: float) -> float` que retorne el índice de masa corporal ($IMC = \frac{peso}{altura^2}$).
2. **Contador de Palabras:** Diseña una función que reciba una cadena de texto y devuelva el número total de palabras contenidas en ella.
3. **Conversor de Moneda:** Escribe una función que convierta una cantidad en dólares a euros. Permite un parámetro opcional `tasa_cambio` que tenga un valor por defecto de `0.92`.

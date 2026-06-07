# Lección 7: Manejo de Cadenas de Texto (Strings)

Esta lección cubre las técnicas esenciales para el procesamiento, manipulación y formateo de cadenas de caracteres en Python.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Comprender** la inmutabilidad de los strings en Python.
2. **Utilizar** los métodos integrados de texto para limpiar, buscar, segmentar y reemplazar información.
3. **Dominar** las técnicas modernas de interpolación y formateo de cadenas utilizando `f-strings` y `.format()`.
4. **Manipular** secuencias de escape y strings multilínea de forma correcta.

---

## 📖 Contenido Conceptual

### 1. Propiedades Fundamentales de los Strings
* **Indexación:** Las cadenas son secuencias de caracteres indexadas. Cada letra posee un índice numérico de acceso (positivo y negativo), similar a las listas.
* **Inmutabilidad:** Las cadenas no pueden ser modificadas una vez creadas. Cualquier operación de cambio (como pasar a mayúsculas) devuelve un objeto string nuevo en memoria, dejando la variable original intacta.

```python
texto = "python"
# Esto lanzará un TypeError:
# texto[0] = "P"
```

---

### 2. Catálogo de Métodos Esenciales de Cadenas

Python provee una extensa gama de herramientas internas para tratar texto:

| Método | Ejemplo | Descripción |
| :--- | :--- | :--- |
| **`.upper()`** | `"hola".upper()` $\rightarrow$ `"HOLA"` | Convierte todos los caracteres a mayúsculas. |
| **`.lower()`** | `"HOLA".lower()` $\rightarrow$ `"hola"` | Convierte todos los caracteres a minúsculas. |
| **`.title()`** | `"hola mundo".title()` $\rightarrow$ `"Hola Mundo"` | Capitaliza la primera letra de cada palabra. |
| **`.strip()`** | `"  hola  ".strip()` $\rightarrow$ `"hola"` | Remueve los espacios en blanco iniciales y finales. |
| **`.replace(ant, nue)`**| `"hola".replace("o", "a")` $\rightarrow$ `"hala"` | Reemplaza las coincidencias del texto indicado. |
| **`.split(del)`** | `"a,b,c".split(",")` $\rightarrow$ `["a", "b", "c"]` | Segmenta el texto en una lista usando un delimitador. |
| **`.join(lista)`** | `"-".join(["a", "b"])` $\rightarrow$ `"a-b"` | Une una lista de textos mediante una cadena conector. |
| **`.count(sub)`** | `"hola".count("o")` $\rightarrow$ `1` | Cuenta cuántas veces se repite una subcadena. |
| **`.find(sub)`** | `"hola".find("l")` $\rightarrow$ `2` | Devuelve el primer índice donde se halla la subcadena. |

---

### 3. Formateo y Interpolación de Cadenas

Existen varias formas de estructurar y formatear strings en Python:

#### f-Strings (Interpolación de Cadenas Literal)
Es el estándar moderno y preferido de la industria debido a su legibilidad y eficiencia. Se declara anteponiendo una `f` al inicio de las comillas e insertando variables o expresiones entre llaves `{}`:

```python
nombre = "Juan"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años. El próximo año tendré {edad + 1}.")
```

#### El Método `.format()`
Sintaxis tradicional ampliamente utilizada. Emplea marcadores de posición `{}` dentro de la cadena y asocia las variables en orden como argumentos al final:

```python
nombre = "Juan"
print("Hola, {}!".format(nombre))
```

---

## 📝 Resumen de la Lección
* Los strings son inmutables; las operaciones generan nuevas cadenas.
* Poseen métodos potentes para transformar, buscar e inspeccionar contenidos (`upper`, `lower`, `replace`, `find`, etc.).
* Para segmentar y unir textos se emplean los métodos complementarios `.split()` y `.join()`.
* Las `f-strings` ofrecen el método de formateo más eficiente y legible.

---

## 🏋️ Desafíos Prácticos
Consolida tu aprendizaje resolviendo estos problemas:

1. **Formateador de Reportes:** Escribe un script que solicite el nombre de un artículo (`articulo`), su precio unitario (`precio`) y la cantidad comprada (`cantidad`). Imprime una línea formateada usando f-strings que diga:
   `Reporte: 5 unidades de LAPTOP compradas a $750.00 c/u. Total: $3750.00`
   *(Asegura que el nombre del artículo se imprima en mayúsculas y los precios muestren dos decimales)*.
2. **Limpiador de Entrada:** Dado un texto con espaciados irregulares y comas: `"   carlos, ana,  pedro, sofía   "`, escribe el código necesario para limpiar los espacios y transformarlo en una lista limpia de nombres independientes: `['carlos', 'ana', 'pedro', 'sofía']`.
3. **Buscador de Extensiones:** Crea una función que tome el nombre de un archivo (por ejemplo, `"documento.pdf"` o `"imagen.png"`) y extraiga únicamente la extensión del mismo. Pista: utiliza `.split()` o indexación con `.find()`.

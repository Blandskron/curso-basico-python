# Guía Práctica de Código: Lección 4 (Funciones)

Esta guía recopila y explica los scripts prácticos correspondientes a la **Lección 4**, abarcando desde funciones elementales hasta implementaciones algorítmicas específicas.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_FuncionsinParametrodysinRetorno.py` | Función básica sin datos de entrada/salida | `python 01_FuncionsinParametrodysinRetorno.py` |
| `02_FuncionconParametrosysinRetorno.py` | Parámetros obligatorios sin retorno | `python 02_FuncionconParametrosysinRetorno.py` |
| `03_FuncionconParametrosyconRetorno.py` | Uso de parámetros y cláusula `return` | `python 03_FuncionconParametrosyconRetorno.py` |
| `04_FuncionconParametrosporDefecto.py` | Declaración de argumentos predeterminados | `python 04_FuncionconParametrosporDefecto.py` |
| `05_FunciondeConversiondeGradosCelsiusaFahrenheit.py` | Conversor de escalas térmicas | `python 05_FunciondeConversiondeGradosCelsiusaFahrenheit.py` |
| `06_FuncionparaEncontrarelMaximodeDosNumeros.py` | Condicionales dentro de funciones | `python 06_FuncionparaEncontrarelMaximodeDosNumeros.py` |
| `07_FuncionparaCalcularelFactorialdeunNumero.py` | Bucle iterativo de cálculo factorial | `python 07_FuncionparaCalcularelFactorialdeunNumero.py` |
| `08_FuncionqueRecibeunaListadeNumerosyDevuelvelaSumadeTodoslosElementos.py` | Acumulador de listas mediante ciclos | `python 08_FuncionqueRecibeunaListadeNumerosyDevuelvelaSumadeTodoslosElementos.py` |
| `09_FuncionqueRecibeunaCadenayDevuelvelaCantidaddeVocalesenlaCadena.py` | Conteo de caracteres condicional | `python 09_FuncionqueRecibeunaCadenayDevuelvelaCantidaddeVocalesenlaCadena.py` |
| `10_FuncionqueRecibeunaListadeCadenasyDevuelvelaCadenaMasLarga.py` | Comparador iterativo de longitud de texto | `python 10_FuncionqueRecibeunaListadeCadenasyDevuelvelaCadenaMasLarga.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Función sin Parámetro y sin Retorno (`01_FuncionsinParametrodysinRetorno.py`)
```python
def saludar():
    print("Hola, Mundo")

saludar()
```
* **Explicación:** Una función simple que ejecuta un `print` cuando es llamada. No requiere argumentos ni devuelve ningún valor.
* **Salida:** `Hola, Mundo`

---

### Ejemplo 2: Función con Parámetros y sin Retorno (`02_FuncionconParametrosysinRetorno.py`)
```python
def saludar_usuario(nombre):
    print("Hola, " + nombre + "!")

saludar_usuario("Juan")
```
* **Explicación:** Recibe la variable `nombre` e imprime un saludo concatenado.
* **Salida:** `Hola, Juan!`

---

### Ejemplo 3: Función con Parámetros y con Retorno (`03_FuncionconParametrosyconRetorno.py`)
```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
```
* **Explicación:** La función realiza la suma y devuelve el resultado al llamador mediante `return`.
* **Salida:** `8`

---

### Ejemplo 4: Función con Parámetros por Defecto (`04_FuncionconParametrosporDefecto.py`)
```python
def saludar(nombre, saludo="Hola"):
    print(saludo + ", " + nombre + "!")

saludar("Juan")
saludar("Juan", "Buenos días")
```
* **Explicación:** Si omitimos el segundo argumento, la función utiliza `"Hola"`.
* **Salida:**
  ```text
  Hola, Juan!
  Buenos días, Juan!
  ```

---

### Ejemplo 5: Conversión de Grados Celsius a Fahrenheit (`05_FunciondeConversiondeGradosCelsiusaFahrenheit.py`)
```python
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(100))
```
* **Salida:**
  ```text
  32.0
  212.0
  ```

---

### Ejemplo 6: Encontrar el Máximo de Dos Números (`06_FuncionparaEncontrarelMaximodeDosNumeros.py`)
```python
def encontrar_maximo(a, b):
    if a > b:
        return a
    else:
        return b

print(encontrar_maximo(10, 20))
```
* **Salida:** `20`

---

### Ejemplo 7: Calcular el Factorial de un Número (`07_FuncionparaCalcularelFactorialdeunNumero.py`)
```python
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))
```
* **Explicación:** Calcula $5! = 5 \times 4 \times 3 \times 2 \times 1$.
* **Salida:** `120`

---

### Ejemplo 8: Suma de Todos los Elementos de una Lista (`08_FuncionqueRecibeunaListadeNumerosyDevuelvelaSumadeTodoslosElementos.py`)
```python
def sumar_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

print(sumar_lista([1, 2, 3, 4, 5]))
```
* **Salida:** `15`

---

### Ejemplo 9: Cantidad de Vocales en una Cadena (`09_FuncionqueRecibeunaCadenayDevuelvelaCantidaddeVocalesenlaCadena.py`)
```python
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

print(contar_vocales("Hola, Mundo"))
```
* **Explicación:** Recorre el texto comprobando si cada letra pertenece al conjunto de vocales definidas.
* **Salida:** `4` (o, a, u, o)

---

### Ejemplo 10: Encontrar la Cadena Más Larga (`10_FuncionqueRecibeunaListadeCadenasyDevuelvelaCadenaMasLarga.py`)
```python
def cadena_mas_larga(cadenas):
    mas_larga = ""
    for cadena in cadenas:
        if len(cadena) > len(mas_larga):
            mas_larga = cadena
    return mas_larga

print(cadena_mas_larga(["hola", "mundo", "programacion", "python"]))
```
* **Explicación:** Compara iterativamente el tamaño (`len()`) de cada cadena contra el valor más largo guardado.
* **Salida:** `programacion`

# Guía Práctica de Código: Lección 3 (Estructuras de Control)

Esta guía documenta los scripts de ejemplos de condicionales y ciclos bucle desarrollados en la **Lección 3**.

---

## 📋 Índice de Ejemplos y Archivos

| Archivo Ejecutable | Concepto que Ilustra | Comando de Ejecución |
| :--- | :--- | :--- |
| `01_Condicional-IF.py` | Condicional simple `if` | `python 01_Condicional-IF.py` |
| `02_Condicional-IF-ELSE.py` | Bifurcación doble `if-else` | `python 02_Condicional-IF-ELSE.py` |
| `03_Condicional-IF-ELIF-ELSE.py` | Múltiples condiciones `if-elif-else` | `python 03_Condicional-IF-ELIF-ELSE.py` |
| `04_Ciclo-FOR-conunaLista.py` | Recorrido iterativo de listas | `python 04_Ciclo-FOR-conunaLista.py` |
| `05_Ciclo-FOR-con-RANGE.py` | Generación de secuencias con `range` | `python 05_Ciclo-FOR-con-RANGE.py` |
| `06_Ciclo-WHILE.py` | Bucle basado en condiciones variables | `python 06_Ciclo-WHILE.py` |
| `07_Usode-BREAK-enun-CICLO.py` | Salida forzada de un bucle | `python 07_Usode-BREAK-enun-CICLO.py` |
| `08_Usode-Continue-enun-CICLO.py` | Omisión de iteraciones específicas | `python 08_Usode-Continue-enun-CICLO.py` |
| `09_ProgramaInterectivo-Condicionales.py` | Entrada de usuario clasificada por condicionales | `python 09_ProgramaInterectivo-Condicionales.py` |
| `10_ProgramaInteractivo-CICLO-FOR.py` | Conteo automático con ciclo `for` | `python 10_ProgramaInteractivo-CICLO-FOR.py` |
| `11_ProgramaInteractivo-Ciclo-WHILE.py` | Centinela de salida interactiva | `python 11_ProgramaInteractivo-Ciclo-WHILE.py` |

---

## 🔍 Explicación Detallada de los Ejemplos

### Ejemplo 1: Condicional `if` (`01_Condicional-IF.py`)
```python
# Ejemplo de uso de if
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")  # Se ejecuta si la evaluación es True
```
* **Salida:** `Eres mayor de edad.`

---

### Ejemplo 2: Condicional `if-else` (`02_Condicional-IF-ELSE.py`)
```python
# Ejemplo de uso de if-else
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")  # Se ejecuta si la evaluación es False
```
* **Salida:** `Eres menor de edad.`

---

### Ejemplo 3: Condicional `if-elif-else` (`03_Condicional-IF-ELIF-ELSE.py`)
```python
# Ejemplo de uso de if-elif-else
edad = 20

if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")  # Se ejecuta si todas las anteriores son False
```
* **Salida:** `Eres un adulto.`

---

### Ejemplo 4: Ciclo `for` con una Lista (`04_Ciclo-FOR-conunaLista.py`)
```python
# Iteración básica sobre un arreglo
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```
* **Explicación:** En cada iteración, la variable temporal `fruta` asume el valor del siguiente elemento de la lista.
* **Salida:**
  ```text
  manzana
  banana
  cereza
  ```

---

### Ejemplo 5: Ciclo `for` con `range` (`05_Ciclo-FOR-con-RANGE.py`)
```python
# Rango del 0 al 4
for i in range(5):
    print(i)
```
* **Explicación:** Por defecto, `range(N)` genera una secuencia que inicia en `0` y termina en `N-1`.
* **Salida:**
  ```text
  0
  1
  2
  3
  4
  ```

---

### Ejemplo 6: Ciclo `while` (`06_Ciclo-WHILE.py`)
```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1  # Modificamos el contador para evitar un bucle infinito
```
* **Salida:**
  ```text
  0
  1
  2
  3
  4
  ```

---

### Ejemplo 7: Uso de `break` en un Ciclo (`07_Usode-BREAK-enun-CICLO.py`)
```python
for i in range(10):
    if i == 5:
        break  # Se sale del ciclo al cumplirse la condición
    print(i)
```
* **Salida:**
  ```text
  0
  1
  2
  3
  4
  ```

---

### Ejemplo 8: Uso de `continue` en un Ciclo (`08_Usode-Continue-enun-CICLO.py`)
```python
for i in range(10):
    if i % 2 == 0:
        continue  # Omite los números pares y salta al siguiente ciclo
    print(i)
```
* **Salida:**
  ```text
  1
  3
  5
  7
  9
  ```

---

### Ejemplo 9: Programa Interactivo - Condicionales (`09_ProgramaInterectivo-Condicionales.py`)
```python
# Programa que determina si un número es positivo, negativo o cero
numero = float(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
```

---

### Ejemplo 10: Programa Interactivo - Ciclo `for` (`10_ProgramaInteractivo-CICLO-FOR.py`)
```python
# Imprimir rango exacto del 1 al 10
for i in range(1, 11):
    print(i)
```

---

### Ejemplo 11: Programa Interactivo - Ciclo `while` (`11_ProgramaInteractivo-Ciclo-WHILE.py`)
```python
# Bucle centinela interactivo
while True:
    numero = float(input("Introduce un número: "))
    if numero < 0:
        print("Número negativo detectado, terminando el programa.")
        break
    print("Número introducido:", numero)
```
* **Explicación:** Se define un bucle indefinido `while True`. Solo se rompe (`break`) cuando el usuario introduce un número menor a cero.

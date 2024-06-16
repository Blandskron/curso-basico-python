### Ejemplo 1: Condicional `if`

```python
# Ejemplo de uso de if
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")  # Esto se ejecutará porque la condición es verdadera
```

### Ejemplo 2: Condicional `if-else`

```python
# Ejemplo de uso de if-else
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")  # Esto se ejecutará porque la condición es falsa
```

### Ejemplo 3: Condicional `if-elif-else`

```python
# Ejemplo de uso de if-elif-else
edad = 20

if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")  # Esto se ejecutará porque las condiciones anteriores son falsas
```

### Ejemplo 4: Ciclo `for` con una Lista

```python
# Ejemplo de uso de for con una lista
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

### Ejemplo 5: Ciclo `for` con `range`

```python
# Ejemplo de uso de for con range
for i in range(5):
    print(i)
```

### Ejemplo 6: Ciclo `while`

```python
# Ejemplo de uso de while
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

### Ejemplo 7: Uso de `break` en un Ciclo

```python
# Ejemplo de uso de break
for i in range(10):
    if i == 5:
        break  # Sale del ciclo cuando i es igual a 5
    print(i)
```

### Ejemplo 8: Uso de `continue` en un Ciclo

```python
# Ejemplo de uso de continue
for i in range(10):
    if i % 2 == 0:
        continue  # Salta a la siguiente iteración del ciclo si i es par
    print(i)
```

### Ejemplo 9: Programa Interactivo - Condicionales

```python
# Programa que determina si un número es positivo, negativo o cero

# Pedir al usuario un número
numero = float(input("Introduce un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
```

### Ejemplo 10: Programa Interactivo - Ciclo `for`

```python
# Programa que imprime los números del 1 al 10

for i in range(1, 11):
    print(i)
```

### Ejemplo 11: Programa Interactivo - Ciclo `while`

```python
# Programa que pide números al usuario hasta que introduzca un número negativo

while True:
    numero = float(input("Introduce un número: "))
    if numero < 0:
        print("Número negativo detectado, terminando el programa.")
        break
    print("Número introducido:", numero)
```

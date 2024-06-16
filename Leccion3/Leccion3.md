## Lección 3: Estructuras de Control

### 1. Condicionales: if, elif, else

#### Objetivos
- Entender cómo usar estructuras condicionales para tomar decisiones en el código.
- Aprender a utilizar `if`, `elif` y `else` para manejar múltiples condiciones.

#### Uso de Condicionales

##### Estructura `if`
- La estructura `if` se usa para ejecutar un bloque de código si una condición es verdadera.

```python
# Ejemplo de uso de if
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
```

##### Estructura `if-else`
- La estructura `if-else` se usa para ejecutar un bloque de código si una condición es verdadera y otro bloque si es falsa.

```python
# Ejemplo de uso de if-else
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

##### Estructura `if-elif-else`
- La estructura `if-elif-else` se usa para manejar múltiples condiciones.

```python
# Ejemplo de uso de if-elif-else
edad = 20

if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")
```

### 2. Ciclos: for, while

#### Objetivos
- Entender cómo usar ciclos para repetir bloques de código.
- Aprender a utilizar los ciclos `for` y `while` para iterar sobre secuencias y ejecutar bloques de código repetidamente.

#### Uso del Ciclo `for`
- El ciclo `for` se usa para iterar sobre una secuencia (como una lista, tupla, cadena o rango).

```python
# Ejemplo de uso de for con una lista
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

- Uso de `range` en un ciclo `for`.

```python
# Ejemplo de uso de for con range
for i in range(5):
    print(i)
```

#### Uso del Ciclo `while`
- El ciclo `while` se usa para repetir un bloque de código mientras una condición sea verdadera.

```python
# Ejemplo de uso de while
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

#### Control de Ciclos
- Uso de `break` para salir de un ciclo.
- Uso de `continue` para saltar a la siguiente iteración del ciclo.

```python
# Ejemplo de uso de break
for i in range(10):
    if i == 5:
        break
    print(i)

# Ejemplo de uso de continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### Resumen y Tareas
- Hoy aprendiste sobre estructuras condicionales y ciclos en Python.
- Practicaste cómo usar `if`, `elif`, `else` para tomar decisiones en el código.
- Practicaste cómo usar los ciclos `for` y `while` para repetir bloques de código.
- **Tarea:** Crea un programa que:
  1. Pida al usuario un número y determine si es positivo, negativo o cero.
  2. Use un ciclo `for` para imprimir los números del 1 al 10.
  3. Use un ciclo `while` para pedir al usuario un número y continuar pidiéndolo hasta que el usuario introduzca un número negativo.

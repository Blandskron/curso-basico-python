# Lección 8: Entrada y Salida (Consola y Archivos)

Esta lección cubre las técnicas para interactuar con el usuario a través de la terminal y persistir información en el disco duro mediante la lectura y escritura de archivos físicos.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Capturar** datos por consola y formatear salidas de texto.
2. **Utilizar** la declaración `with` (Context Manager) para abrir y cerrar archivos de manera segura.
3. **Comprender** y emplear los distintos modos de apertura de archivos (`r`, `w`, `a`).
4. **Implementar** control de excepciones (`try-except`) para prevenir errores críticos de lectura/escritura (como archivos inexistentes).

---

## 📖 Contenido Conceptual

### 1. Entrada y Salida por Consola
* **Entrada (`input`):** Captura la información escrita por teclado en forma de texto (`str`).
* **Salida (`print`):** Despliega información en pantalla. Permite configurar argumentos opcionales como `sep` (delimitador entre elementos) y `end` (carácter final al imprimir, por defecto un salto de línea `\n`).

---

### 2. Persistencia en Archivos de Texto
Para trabajar con archivos en disco, se utiliza la función integrada `open(ruta, modo)`.

#### Modos de Apertura de Archivos

| Modo | Nombre | Descripción |
| :---: | :--- | :--- |
| **`r`** | Read (Lectura) | Abre un archivo para lectura. Lanza error si el archivo no existe. (Modo por defecto). |
| **`w`** | Write (Escritura) | Abre el archivo para escritura. Sobrescribe el contenido existente o crea un archivo nuevo si no existe. |
| **`a`** | Append (Anexar) | Abre el archivo para añadir información al final de este sin borrar el contenido anterior. Crea el archivo si no existe. |

---

### 3. El Gestor de Contexto: Declaración `with`
En el desarrollo profesional de software, siempre se prefiere abrir archivos utilizando la estructura `with open(...) as alias:`.

```python
with open("datos.txt", "w") as archivo:
    archivo.write("Línea de datos")
```

> [!IMPORTANT]
> **Por qué usar `with`:** Si abres un archivo manualmente con `archivo = open(...)` y ocurre un error a mitad de ejecución, el archivo se quedará abierto en el sistema de archivos (bloqueado, consumiendo recursos y pudiendo corromperse). La declaración `with` garantiza el cierre automático y seguro del archivo en cuanto finaliza su bloque indentado, ocurra o no una excepción.

---

### 4. Gestión de Errores de Archivos (`try-except`)
Las operaciones de lectura y escritura de archivos son propensas a fallar por factores ajenos al código (archivo borrado por el usuario, falta de permisos en la carpeta, disco lleno, etc.).

Para evitar que tu programa deje de funcionar abruptamente, se capturan las excepciones mediante bloques `try-except`:

```python
try:
    with open("archivo_secreto.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo especificado no existe en la ruta.")
except PermissionError:
    print("Error: No tienes permisos para leer este archivo.")
```

---

## 📝 Resumen de la Lección
* `input()` captura strings y `print()` expone resultados configurando espaciados y finales de línea.
* La persistencia de datos en Python se realiza con `open()`.
* Los modos esenciales de archivo son `r` (lectura), `w` (sobrescritura) y `a` (anexar).
* La instrucción `with` automatiza la liberación de recursos (cierre de archivos) de forma segura.
* El manejo de excepciones con `try-except` evita fallas de sistema al abrir archivos.

---

## 🏋️ Desafíos Prácticos
Lleva a cabo estos ejercicios de persistencia en tu computadora:

1. **Bitácora Diaria:** Crea un script que pida al usuario una frase o nota personal. Guarda el texto capturado en un archivo llamado `bitacora.txt`. Si el archivo ya tiene contenido, la nueva nota debe agregarse al final en una línea nueva (usa el modo `a`).
2. **Lector con Estadísticas:** Escribe un programa que lea un archivo de texto llamado `poema.txt`. Si no existe, captura el error de forma segura mostrando un mensaje amigable. Si existe, lee su contenido, muéstralo en pantalla e imprime cuántas líneas y cuántas palabras en total contiene el archivo.
3. **Copia de Seguridad:** Diseña una función `respaldar_archivo(origen: str, destino: str)` que lea el contenido de un archivo origen y escriba una copia idéntica en el archivo destino.

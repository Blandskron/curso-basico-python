## Lección 1: Introducción a Python

### 1. Instalación y Configuración del Entorno

#### Objetivos
- Entender qué es Python y por qué es útil aprenderlo.
- Instalar Python en tu sistema operativo.
- Configurar el entorno de desarrollo para escribir y ejecutar programas en Python.

#### ¿Qué es Python?
- Python es un lenguaje de programación interpretado, de alto nivel y de propósito general.
- Es conocido por su sintaxis clara y legible, lo que lo hace ideal para principiantes.
- Usos comunes: desarrollo web, automatización, análisis de datos, inteligencia artificial, y más.

#### Instalación de Python
1. **Windows:**
   - Visita la página oficial de Python: [python.org](https://www.python.org/).
   - Descarga el instalador para Windows.
   - Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH".
   - Sigue las instrucciones en pantalla para completar la instalación.
   
2. **macOS:**
   - Python viene preinstalado en macOS, pero es recomendable instalar la versión más reciente.
   - Puedes usar Homebrew para instalar Python:
     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     brew install python
     ```
   
3. **Linux:**
   - La mayoría de las distribuciones de Linux vienen con Python preinstalado.
   - Para instalar la versión más reciente, usa tu gestor de paquetes:
     ```sh
     sudo apt update
     sudo apt install python3
     ```

#### Verificación de la Instalación
- Abre la terminal o el símbolo del sistema.
- Escribe `python --version` o `python3 --version` para verificar la instalación.
- Deberías ver algo como `Python 3.x.x`.

#### Instalación de un Editor de Código
- Se recomienda usar Visual Studio Code (VS Code):
  - Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/).
  - Instálalo siguiendo las instrucciones para tu sistema operativo.
  - Instala la extensión de Python para VS Code desde el marketplace de extensiones.

### 2. Primer Programa en Python: "Hola, Mundo"

#### Objetivos
- Escribir y ejecutar tu primer programa en Python.
- Familiarizarte con la sintaxis básica de Python.

#### Escribir tu Primer Programa
1. Abre Visual Studio Code.
2. Crea una nueva carpeta para tus proyectos de Python.
3. Dentro de esta carpeta, crea un nuevo archivo llamado `hola_mundo.py`.
4. Abre `hola_mundo.py` y escribe el siguiente código:
   ```python
   print("Hola, Mundo")
   ```

#### Ejecutar tu Programa
1. Guarda el archivo.
2. Abre la terminal integrada en VS Code (puedes abrirla desde el menú: `View` > `Terminal`).
3. Navega hasta la carpeta donde guardaste `hola_mundo.py` usando el comando `cd`:
   ```sh
   cd ruta/a/tu/carpeta
   ```
4. Ejecuta el programa escribiendo:
   ```sh
   python hola_mundo.py
   ```
   - En algunas configuraciones puede ser necesario usar `python3` en lugar de `python`.
5. Deberías ver la salida:
   ```
   Hola, Mundo
   ```

### Resumen y Tareas
- Hoy aprendiste qué es Python, cómo instalarlo y configurarlo en tu sistema.
- Escribiste y ejecutaste tu primer programa en Python.
- **Tarea:** Investiga otros editores de código como PyCharm, Atom o Jupyter Notebook y escribe una breve comparación.

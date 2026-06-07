# Lección 1: Introducción a Python y Configuración del Entorno

Esta lección inicial tiene como propósito introducirte al ecosistema de Python, guiarte en el proceso de instalación y configuración de tu entorno de trabajo, y enseñarte a escribir y ejecutar tu primer script de programación.

---

## 🎯 Objetivos de Aprendizaje
Al finalizar esta lección, serás capaz de:
1. **Comprender** la naturaleza de Python, sus características de alto nivel y sus campos de aplicación más habituales.
2. **Configurar** con éxito el intérprete de Python 3 en tu sistema operativo (Windows, macOS o Linux).
3. **Instalar** y preparar un editor de código profesional (Visual Studio Code) junto con la extensión de soporte para Python.
4. **Desarrollar, guardar y ejecutar** tu primer script ejecutable en Python (`print("Hola, Mundo")`) utilizando la interfaz de línea de comandos.

---

## 📖 Contenido Conceptual

### 1. ¿Qué es Python y por qué aprenderlo?
Python es un lenguaje de programación interpretado, de alto nivel, de tipado dinámico y multiparadigma. Es ampliamente valorado en la industria del software debido a las siguientes fortalezas:

* **Sintaxis Legible:** Su filosofía de diseño enfatiza la legibilidad del código (uso estricto de sangrías/indentación), lo que reduce el costo de mantenimiento y facilita el aprendizaje.
* **Propósito General:** Se utiliza en desarrollo web, análisis de datos, aprendizaje automático (Machine Learning), automatización de tareas de sistema (scripting) y desarrollo científico.
* **Baterías Incluidas:** Posee una robusta biblioteca estándar que proporciona herramientas listas para usar para resolver problemas comunes sin depender de paquetes externos.

> [!NOTE]
> Un lenguaje **interpretado** significa que el código fuente se ejecuta instrucción por instrucción mediante un programa llamado intérprete, sin necesidad de compilarlo previamente a lenguaje máquina binario.

---

### 2. Instalación de Python 3

#### En Windows
1. Descarga el instalador ejecutable de 64 bits para Windows desde la sección de descargas de [python.org](https://www.python.org/).
2. Ejecuta el instalador descargado.
3. > [!IMPORTANT]
   > Asegúrate de activar la casilla **"Add Python to PATH"** en la parte inferior del asistente de instalación. Esto te permitirá llamar al comando `python` desde cualquier ventana del terminal.
4. Selecciona **Install Now** y completa la instalación.

#### En macOS
macOS suele incluir una versión heredada de Python. Para instalar la última versión estable, se recomienda usar el gestor de paquetes **Homebrew**:
1. Abre tu terminal.
2. Si no tienes instalado Homebrew, ejecútalo:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Ejecuta la instalación de Python:
   ```bash
   brew install python
   ```

#### En Linux (Distribuciones basadas en Debian/Ubuntu)
Generalmente viene preinstalado. Si necesitas asegurarte de tener la versión más reciente:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-dev
```

#### Verificación de la Instalación
Una vez completados los pasos anteriores, abre una nueva consola (Símbolo del Sistema en Windows, Terminal en macOS/Linux) y escribe el siguiente comando:
```bash
python --version
# O en sistemas macOS/Linux:
python3 --version
```
Deberías ver una salida indicando la versión instalada, por ejemplo: `Python 3.11.x`.

---

### 3. Editor de Código: Visual Studio Code
Para escribir programas de manera ágil y organizada, utilizaremos **Visual Studio Code (VS Code)**, un editor ligero y potente.

1. Descarga el instalador desde [code.visualstudio.com](https://code.visualstudio.com/).
2. Instala el software siguiendo los pasos por defecto correspondientes a tu plataforma.
3. Instala la extensión oficial de **Python**:
   * Abre VS Code.
   * Haz clic en el ícono de extensiones en la barra lateral izquierda (o presiona `Ctrl+Shift+X`).
   * Escribe `Python` en la barra de búsqueda y selecciona la extensión publicada por **Microsoft**.
   * Haz clic en **Install**.

---

### 4. Tu Primer Script: "Hola, Mundo"
El programa tradicional para aprender cualquier lenguaje de programación consiste en mostrar un texto en pantalla.

#### Estructura de la función `print()`
La función integrada `print()` recibe como argumento un dato (por ejemplo, una cadena de texto rodeada de comillas) y lo envía a la salida estándar (la consola de texto).

```python
# Este código muestra un saludo en la consola
print("Hola, Mundo")
```

> [!TIP]
> En Python, los comentarios comienzan con el símbolo `#`. El intérprete ignora estas líneas, sirviendo exclusivamente para documentar y explicar el comportamiento del código a otros programadores.

---

## 📝 Resumen de la Lección
* Comprendimos las ventajas de Python: legibilidad, potencia y versatilidad.
* Instalamos el intérprete de Python, asegurando su vinculación en las variables del sistema (PATH).
* Configuramos Visual Studio Code como nuestro entorno de desarrollo primario.
* Escribimos e interpretamos la línea de código `print("Hola, Mundo")`.

---

## 🏋️ Desafíos Prácticos
Pon en práctica lo aprendido en esta lección completando los siguientes retos:

1. **Modificar el Saludo:** Edita tu script `hola_mundo.py` para que imprima tu nombre en la consola (por ejemplo: `Hola, Bastian`).
2. **Múltiples Impresiones:** Escribe un programa que imprima tres mensajes diferentes, cada uno en una línea separada, describiendo tres razones por las que decidiste aprender a programar.
3. **Investigación de Entornos:** Investiga qué es un Entorno de Desarrollo Integrado (IDE) y en qué se diferencia de un editor de texto plano como el Bloc de Notas (Notepad). Escribe tus conclusiones en un párrafo.

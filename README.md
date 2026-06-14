# Curso de Python Basico

Modulo inicial de la ruta profesional gratuita de Python. Esta etapa esta pensada para estudiantes sin experiencia previa o con conocimientos muy iniciales que necesitan construir una base solida antes de pasar a programacion intermedia.

## Objetivo del modulo

Al finalizar este modulo seras capaz de:

- instalar y ejecutar Python desde consola;
- escribir scripts pequenos de forma autonoma;
- usar variables, tipos de datos, condicionales, ciclos y funciones;
- trabajar con listas, tuplas, diccionarios, conjuntos, cadenas y archivos;
- resolver problemas simples mediante proyectos de consola.

## Requisitos

- Python 3.10 o superior recomendado.
- Visual Studio Code u otro editor de codigo.
- Terminal o simbolo del sistema.

Este modulo no requiere paquetes externos. El archivo `requirements.txt` se incluye solo para dejarlo explicito.

## Estructura del curso

| Leccion | Tema | Teoria | Codigo |
|---|---|---|---|
| 1 | Introduccion, entorno y primeros scripts | [Leccion1.md](./Leccion1/Leccion1.md) | [CodigoLeccion1.md](./Leccion1/CodigoLeccion1.md) |
| 2 | Variables, tipos de datos y operadores | [Leccion2.md](./Leccion2/Leccion2.md) | [CodigoLeccion2.md](./Leccion2/CodigoLeccion2.md) |
| 3 | Condicionales y ciclos | [Leccion3.md](./Leccion3/Leccion3.md) | [CodigoLeccion3.md](./Leccion3/CodigoLeccion3.md) |
| 4 | Funciones, parametros y retorno | [Leccion4.md](./Leccion4/Leccion4.md) | [CodigoLeccion4.md](./Leccion4/CodigoLeccion4.md) |
| 5 | Listas y tuplas | [Leccion5.md](./Leccion5/Leccion5.md) | [CodigoLeccion5.md](./Leccion5/CodigoLeccion5.md) |
| 6 | Diccionarios y conjuntos | [Leccion6.md](./Leccion6/Leccion6.md) | [CodigoLeccion6.md](./Leccion6/CodigoLeccion6.md) |
| 7 | Cadenas y formateo de texto | [Leccion7.md](./Leccion7/Leccion7.md) | [CodigoLeccion7.md](./Leccion7/CodigoLeccion7.md) |
| 8 | Entrada, salida y archivos | [Leccion8.md](./Leccion8/Leccion8.md) | [CodigoLeccion8.md](./Leccion8/CodigoLeccion8.md) |
| 9 | Modulos y librerias estandar | [Leccion9.md](./Leccion9/Leccion9.md) | [CodigoLeccion9.md](./Leccion9/CodigoLeccion9.md) |
| 10 | Proyectos integradores basicos | [Leccion10.md](./Leccion10/Leccion10.md) | [CodigoLeccion10.md](./Leccion10/CodigoLeccion10.md) |

## Como ejecutar ejemplos

Desde la carpeta del modulo:

```bash
python Leccion1/01_HolaMundo.py
python Leccion3/01_Condicional-IF.py
python Leccion10/01_CalculadoraBasica.py
```

En macOS/Linux puede que debas usar `python3` en lugar de `python`.

## Proyecto de cierre

La Leccion 10 integra lo aprendido mediante:

- una calculadora de consola;
- un juego de adivinanza numerica.

Para practicar profesionalmente, intenta agregar validacion de errores, historial de operaciones y niveles de dificultad.

## Criterio de aprobacion

Antes de pasar al modulo intermedio, deberias poder:

- explicar que hace cada linea de un script simple;
- leer errores comunes de consola;
- crear funciones propias;
- usar colecciones para guardar y transformar datos;
- leer y escribir archivos pequenos.

## Validacion

```bash
python -m compileall .
```

Si el comando termina sin errores, todos los archivos Python tienen sintaxis valida.

## Licencia

MIT. Consulta [LICENSE](./LICENSE).

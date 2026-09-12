# 11 — Tu entorno local: VS Code, Python y Git

**Sesión 12 · Bloque 1 de 2 · Duración estimada: 75 minutos**

Hasta ahora todo el diplomado corrió en **Google Colab**, que es cómodo porque no hay que instalar
nada. Pero Colab tiene tres límites que ya empezamos a topar: la sesión se borra al cerrarla, no
puedes correr una aplicación web de verdad, y no puedes trabajar con un proyecto de varios archivos
con comodidad.

En esta sesión montamos un **entorno local** en tu computadora. No vamos a construir agentes hoy:
el objetivo es que al terminar tengas todo instalado y verificado, para que las sesiones
posteriores de agentes con **Agno** empiecen en el contenido y no en la instalación.

> **Al final corres un script que verifica todo.** Si te marca todo en verde, quedaste listo.

> **Si algo aquí se te complica, no te quedas sin la sesión.** El segundo bloque (tu página
> personal en GitHub Pages) se hace por completo desde el navegador y no necesita nada de lo que
> instalamos aquí.

## Qué vamos a instalar y para qué

| Herramienta | Para qué |
|---|---|
| **Python 3.12 o superior** | Agno lo exige. La versión que trae tu sistema suele ser más vieja. |
| **VS Code** | El editor donde vas a escribir el proyecto y usar la terminal integrada. |
| **Git** | Para versionar tu trabajo y publicarlo en GitHub desde tu computadora. |
| **Un entorno virtual** | Para que los paquetes de este proyecto no se mezclen con los de otros. |

---

## Paso 1 — Instalar Python 3.12 o superior

**Primero revisa qué tienes.** Abre una terminal (en Windows, *PowerShell*; en Mac, *Terminal*):

```bash
python3 --version      # Mac y Linux
python --version       # Windows
```

Si dice 3.12 o más, salta al paso 2.

### En Windows

1. Ve a [python.org/downloads](https://www.python.org/downloads/) y descarga el instalador.
2. En la primera pantalla del instalador, **marca la casilla "Add python.exe to PATH"**. Es el
   error más común de esta sesión: sin esa casilla, la terminal no encuentra Python.
3. *Install Now*. Cierra y vuelve a abrir la terminal para que tome el cambio.

### En Mac

Descarga el instalador de [python.org/downloads](https://www.python.org/downloads/) y ábrelo.
Si usas Homebrew, también funciona `brew install python@3.12`.

> **No borres la versión vieja de Python.** El sistema puede estar usándola. Conviven sin problema.

---

## Paso 2 — Instalar VS Code

Descárgalo de [code.visualstudio.com](https://code.visualstudio.com/) e instálalo con las opciones
por omisión.

En Windows, durante la instalación conviene marcar **"Add to PATH"** y **"Abrir con Code"** en el
menú contextual.

### Extensiones

Abre VS Code, haz clic en el ícono de **Extensiones** en la barra izquierda (o `Ctrl+Shift+X`, en
Mac `Cmd+Shift+X`) e instala:

| Extensión | Autor | Para qué |
|---|---|---|
| **Python** | Microsoft | Autocompletado, errores en vivo, selección de intérprete. |
| **Jupyter** | Microsoft | Abrir y correr notebooks `.ipynb` dentro de VS Code. |
| **Ruff** | Astral | Marca errores de estilo y de sintaxis mientras escribes. |

---

## Paso 3 — Instalar Git

Si ya lo instalaste antes en el diplomado, sáltate esto. Si no, sigue el manual que está en
`00 Notas/Manual_Git_Mac_Windows_2026.pdf` de este mismo repositorio, o descárgalo de
[git-scm.com](https://git-scm.com/downloads).

Verifica con:

```bash
git --version
```

---

## Paso 4 — Crear la carpeta del proyecto y su entorno virtual

Un **entorno virtual** es una carpeta con su propia copia de Python y sus propios paquetes. Sirve
para que instalar algo aquí no rompa otro proyecto. Es la práctica estándar y vale la pena
adoptarla desde ahora.

Abre la terminal y crea la carpeta:

```bash
mkdir agentes-diplomado
cd agentes-diplomado
```

**Crea el entorno virtual:**

```bash
# Mac / Linux
python3.12 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

Sabes que funcionó porque el nombre `(.venv)` aparece al inicio de la línea de la terminal.

> **Si PowerShell se niega** con un mensaje sobre "ejecución de scripts deshabilitada", corre una
> sola vez:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
> y responde que sí. Es un permiso de Windows, no un problema de Python.

**Abre la carpeta en VS Code:**

```bash
code .
```

Y dile a VS Code cuál intérprete usar: `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) → escribe
**"Python: Select Interpreter"** → elige el que dice `.venv`. Este paso se olvida seguido, y sin él
VS Code te marcará como no instalados paquetes que sí instalaste.

---

## Paso 5 — Instalar los paquetes

Copia el archivo `requirements.txt` de esta carpeta a tu proyecto y corre:

```bash
pip install -r requirements.txt
```

Tarda unos minutos la primera vez.

---

## Paso 6 — Guardar tu llave de Groq (sin publicarla nunca)

Hasta ahora escribíamos la llave con `getpass` cada vez. En un proyecto local se guarda en un
archivo `.env` y se lee desde el código.

**Crea un archivo `.env`** en la carpeta del proyecto con una sola línea:

```
GROQ_API_KEY=gsk_tu_llave_aqui
```

**Crea un archivo `.gitignore`** en la misma carpeta con:

```
.env
.venv/
__pycache__/
*.pyc
```

> **Esto no es un trámite.** Una llave subida a un repositorio público se detecta en minutos con
> herramientas automáticas y se usa para gastar tu cuota. Por eso `.env` va en `.gitignore`
> **antes** del primer `commit`. Si alguna vez te pasa, no basta con borrar el archivo: hay que
> revocar la llave y generar una nueva.

Así se lee después desde Python:

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()                          # lee el archivo .env
cliente = Groq(api_key=os.environ["GROQ_API_KEY"])
```

---

## Paso 7 — Verificar

Copia `verificar_entorno.py` a tu carpeta de proyecto y córrelo:

```bash
python verificar_entorno.py
```

Revisa siete cosas: la versión de Python, que el entorno virtual esté activo, los paquetes, que
exista el `.env` con una llave con el formato correcto, que `.env` esté en `.gitignore`, y que Git
esté instalado.

**Si todo sale en verde, terminaste este bloque.** Si algo sale en rojo, el mensaje te dice qué
paso repetir.

---

## Qué sigue: Agno

En las sesiones posteriores vamos a usar **[Agno](https://docs.agno.com)**, un marco de trabajo en
Python para construir agentes. Ya lo tienes instalado.

La idea será la misma que vimos en `08 Building-a-Chat` con LangChain —un modelo que decide cuándo
usar herramientas— pero con tres cosas que hoy no podíamos hacer y que ahora sí, gracias a tener
entorno local: agentes que **recuerdan** entre ejecuciones, agentes que **trabajan en equipo**, y
agentes con acceso a **tus propios archivos**.

Por hoy basta con que el entorno esté listo y verificado.

## Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| `python no se reconoce como comando` (Windows) | No marcaste "Add python.exe to PATH". Vuelve a correr el instalador y elige *Modify*. |
| `pip install` instala pero VS Code marca el paquete como faltante | No seleccionaste el intérprete del `.venv`. Repite el final del paso 4. |
| PowerShell no deja activar el entorno | Corre el comando `Set-ExecutionPolicy` del paso 4. |
| `python3.12: command not found` en Mac | Prueba solo `python3 -m venv .venv` y verifica con `python3 --version` que sea 3.12+. |
| El verificador dice que falta `agno` aunque lo instalaste | Lo instalaste fuera del entorno virtual. Actívalo y repite el paso 5. |

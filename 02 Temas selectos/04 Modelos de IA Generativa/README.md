# 04 Modelos de IA Generativa

**Sesiones del módulo:** Sesiones 11 y 12 (sesiones adicionales, posteriores al cierre de la
Sesión 10).
**Duración:** entre 2.5 y 3 horas cada una.
**Prerrequisito:** `03 Aplicaciones NLP (word embeddings)`, en particular
`06_Using_Embeddings_in_RAG_Inference.ipynb`, que deja el sistema RAG armado hasta el paso de
recuperación.
**Notas relacionadas:** `main.tex`, capítulo 2, sección *"Introducción a los LLMs y aplicaciones
basadas en LLMs"* (arquitectura Transformer, modelos base vs. ajustados por instrucción, prompt
engineering, agentes y uso de herramientas).

## Por qué estas dos sesiones son distintas

Las diez sesiones anteriores terminan en un notebook. Estas dos terminan en **algo que existe en
internet y que puedes enseñarle a alguien más**: una aplicación desplegada y una página personal.
El cambio de formato es deliberado — pasar de "corrí el ejemplo" a "publiqué algo que funciona" es
el paso que convierte un curso en un proyecto propio.

Cada sesión cierra con una URL tuya.

## Objetivo de la unidad

Pasar de *usar* un modelo de lenguaje a *diseñar y desplegar* un sistema que lo incorpore:
cerrar el ciclo de RAG con generación, controlar el comportamiento del modelo con el prompt de
sistema, publicar el resultado como aplicación web, y dejar montado un entorno local de desarrollo
para las sesiones de agentes que siguen.

---

## Sesión 11 — Del notebook a la aplicación

**Producto final: tu asistente RAG corriendo en una URL pública.**

| Tiempo | Bloque | Material |
|---|---|---|
| 0:00 – 0:15 | Repaso: dónde quedó el RAG y qué falta | `06_Using_Embeddings_in_RAG_Inference.ipynb` |
| 0:15 – 1:40 | Generación con Groq, prompt de sistema medido, elección del recuperador | `08 RAG-Completo/08_RAG_Completo.ipynb` |
| 1:40 – 1:55 | **Receso** | |
| 1:55 – 2:50 | Construir y desplegar la app en Streamlit Community Cloud | `09 App-RAG-Streamlit/README.md` |
| 2:50 – 3:00 | Cierre y comparación de las apps del grupo | |

**El experimento central** de la sesión es el de la sección 6 del notebook: con el mismo contexto
recuperado y tres prompts de sistema distintos, se ve al mismo modelo inventar cifras y luego
negarse a inventarlas. El prompt de sistema deja de ser "afinar el tono" y se vuelve visiblemente
la parte del programa donde se implementa la política de honestidad del sistema.

---

## Sesión 12 — Tu entorno local y tu presencia pública

**Producto final: tu página personal publicada, enlazando la app de la sesión anterior.**

| Tiempo | Bloque | Material |
|---|---|---|
| 0:00 – 1:15 | VS Code, Python 3.12, entorno virtual, Git y manejo seguro de llaves | `10 Entorno-Local-VSCode/README.md` |
| 1:15 – 1:30 | **Receso** | |
| 1:30 – 2:40 | Página personal con GitHub Pages, editada en VS Code y publicada con Git | `11 Pagina-Personal-GitHub-Pages/README.md` |
| 2:40 – 3:00 | Cierre: qué sigue con Agno | |

El primer bloque no construye agentes: prepara el entorno para las sesiones posteriores en las que
se usará **Agno**, de modo que aquellas empiecen en el contenido y no en la instalación. El
segundo bloque usa ese entorno recién montado para algo real, que es la mejor forma de verificar
que quedó bien.

---

## Contenido de la carpeta

| Carpeta | Qué es | Sesión |
|---|---|---|
| `06 Intro-to-IA` | Enlace a la presentación de apoyo (Canva). Material de exposición, no ejecutable. | 11 (apertura) |
| `07 Building-a-Chat/Agente_Basico.ipynb` | Agente conversacional con LangChain + Llama 3.3 (Groq): modelo, roles y memoria como lista de mensajes. | Referencia |
| `07 Building-a-Chat/Agente_Intermedio.ipynb` | El mismo agente con dos herramientas (búsqueda web y calculadora segura sin `eval()`). El modelo decide cuándo usarlas. | Referencia |
| `08 RAG-Completo/08_RAG_Completo.ipynb` | Cierra el ciclo de RAG: generación con Groq, el prompt de sistema medido con un experimento, y la elección del recuperador con datos. | 11 |
| `09 App-RAG-Streamlit/` | La aplicación desplegable: `streamlit_app.py`, `rag_core.py`, `corpus_diplomado.py` y la guía de despliegue. | 11 |
| `10 Entorno-Local-VSCode/` | Guía de instalación (Mac y Windows) y `verificar_entorno.py`, que revisa siete condiciones y dice qué falta. | 12 |
| `11 Pagina-Personal-GitHub-Pages/` | Guía de publicación y una plantilla HTML de una sola página, responsiva y sin dependencias. | 12 |

Los notebooks `07 Building-a-Chat` son material previo y siguen vigentes; se usan como referencia
del patrón de agente con herramientas, que es hacia donde apuntan las sesiones posteriores con
Agno.

---

## Preparación previa (importante)

### Llaves de Groq: cada quien la suya

Cada estudiante crea su **cuenta gratuita** en [console.groq.com](https://console.groq.com/keys).
No conviene compartir una sola llave del grupo: el límite gratuito por minuto se satura con veinte
personas trabajando a la vez, y además la app desplegada necesita que cada quien use la suya.

La aplicación **pide la llave al visitante en la barra lateral** y no la guarda en ningún lado. Por
eso el estudiante puede compartir la URL de su app sin que nadie consuma su cuota.

**Pídeles que creen la cuenta y generen la llave antes de la sesión 11.** Es el trámite que más
tiempo consume si se hace en clase.

### Cuenta de GitHub

Necesaria en las dos sesiones (para desplegar en Streamlit y para publicar la página). Si alguien
no la tiene, conviene crearla antes. La instalación de Git está documentada en
`00 Notas/Manual_Git_Mac_Windows_2026.pdf`.

### Dónde corre cada cosa

| Material | Dónde |
|---|---|
| Notebook `08_RAG_Completo.ipynb` | Google Colab (instala solo lo que falte) |
| App de Streamlit | Se despliega en Streamlit Community Cloud desde el repositorio del estudiante |
| Sesión 12 completa | **En su computadora**, no en Colab: ése es justamente el objetivo |

---

## Nota de arquitectura: por qué la app no usa embeddings

Streamlit Community Cloud da **1 GB de RAM** en su plan gratuito. Medimos el consumo de las
opciones: TF-IDF ~150 MB, `all-MiniLM-L6-v2` 597 MB, y el modelo multilingüe
`paraphrase-multilingual-MiniLM-L12-v2` 1,372 MB — que **no cabe**, y es el único que funcionaría
con un corpus en español.

Al medir la calidad de recuperación con 18 preguntas de respuesta conocida resultó, además, que
TF-IDF **no pierde** contra los embeddings en este corpus (8/8 contra 7/8 en preguntas normales,
empate 6/10 en parafraseadas). La sección 7 del notebook desarrolla ese hallazgo y explica por qué
ocurre con un corpus chico y bien escrito, y en qué condiciones se invertiría.

Es una de las lecciones que más se aprovechan de estas sesiones: **el lugar donde se va a
desplegar es parte del diseño**, y la técnica más nueva no es automáticamente la mejor para el
problema que se tiene enfrente.

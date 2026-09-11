# 04 Modelos de IA Generativa

**Sesiones del módulo:** bloque de cierre de la Sesión 10, más las Sesiones 11 y 12 (adicionales).
**Duración:** ~50 minutos el notebook 07; entre 2.5 y 3 horas cada sesión adicional.
**Prerrequisito:** `03 Aplicaciones NLP (word embeddings)`, en particular
`06_Using_Embeddings_in_RAG_Inference.ipynb`, que deja el sistema RAG armado hasta el paso de
recuperación.
**Notas relacionadas:** `main.tex`, capítulo 2, sección *"Introducción a los LLMs y aplicaciones
basadas en LLMs"* (arquitectura Transformer, modelos base vs. ajustados por instrucción, prompt
engineering, agentes y uso de herramientas).

## Cómo está organizada la carpeta

El material va de adentro hacia afuera: primero **cómo funciona** un modelo de lenguaje, luego
**cómo se usa** por una API, y por último **cómo se despliega** algo que otras personas puedan
abrir.

```
07 De-Texto-a-Respuesta   ¿qué pasa dentro del modelo?   (notebook, se abre la caja negra)
08 Building-a-Chat        el modelo por API + memoria + herramientas   (referencia)
09 RAG-Completo           el ciclo de RAG cerrado: recuperar y generar
10 App-RAG-Streamlit      lo mismo, pero desplegado en una URL pública
11 Entorno-Local-VSCode   salir de Colab: Python, VS Code, Git y llaves
12 Pagina-Personal        tu página en GitHub Pages, enlazando lo anterior
```

## Por qué las dos sesiones adicionales son distintas

Las diez sesiones anteriores terminan en un notebook. Las Sesiones 11 y 12 terminan en **algo que
existe en internet y que puedes enseñarle a alguien más**: una aplicación desplegada y una página
personal. El cambio de formato es deliberado — pasar de "corrí el ejemplo" a "publiqué algo que
funciona" es el paso que convierte un curso en un proyecto propio.

Cada sesión cierra con una URL tuya.

## Objetivo de la unidad

Pasar de *usar* un modelo de lenguaje a *entenderlo y desplegarlo*: ver qué ocurre entre el texto
que entra y el texto que sale, cerrar el ciclo de RAG con generación, controlar el comportamiento
del modelo con el prompt de sistema, publicar el resultado como aplicación web, y dejar montado un
entorno local de desarrollo para las sesiones de agentes que siguen.

---

## Bloque de cierre de la Sesión 10 — Abrir la caja negra

**Producto: entender qué hace el modelo que vas a llamar por API en las dos sesiones siguientes.**

| Tiempo | Bloque | Material |
|---|---|---|
| 0:00 – 0:50 | Texto → tokens → vectores → Transformer → logits → token → texto | `07 De-Texto-a-Respuesta/07_De_Texto_a_Respuesta.ipynb` |

Es el puente entre los *embeddings* de la Sesión 10 y las llamadas a la API de las Sesiones 11 y
12: descarga un GPT-2 pequeño en español (~500 MB) y lo desarma pieza por pieza, sin necesidad de
llave de API. Ahí se ve, medido y no contado, que la salida del modelo no es una frase sino una
distribución de probabilidad sobre 50,257 tokens; qué hace exactamente `temperature`; y por qué un
texto en español cuesta ~67 % más tokens que el mismo texto en inglés.

**Si la Sesión 10 se queda corta de tiempo**, este notebook funciona igual de bien como apertura
de la Sesión 11 (en cuyo caso el repaso de RAG se recorta a 10 minutos y el bloque del notebook 09
empieza más tarde).

---

## Sesión 11 — Del notebook a la aplicación

**Producto final: tu asistente RAG corriendo en una URL pública.**

| Tiempo | Bloque | Material |
|---|---|---|
| 0:00 – 0:15 | Repaso: dónde quedó el RAG y qué falta | `06_Using_Embeddings_in_RAG_Inference.ipynb` |
| 0:15 – 1:40 | Generación con Groq, prompt de sistema medido, elección del recuperador | `09 RAG-Completo/09_RAG_Completo.ipynb` |
| 1:40 – 1:55 | **Receso** | |
| 1:55 – 2:50 | Construir y desplegar la app en Streamlit Community Cloud | `10 App-RAG-Streamlit/README.md` |
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
| 0:00 – 1:15 | VS Code, Python 3.12, entorno virtual, Git y manejo seguro de llaves | `11 Entorno-Local-VSCode/README.md` |
| 1:15 – 1:30 | **Receso** | |
| 1:30 – 2:40 | Página personal con GitHub Pages, editada en VS Code y publicada con Git | `12 Pagina-Personal-GitHub-Pages/README.md` |
| 2:40 – 3:00 | Cierre: qué sigue con Agno | |

El primer bloque no construye agentes: prepara el entorno para las sesiones posteriores en las que
se usará **Agno**, de modo que aquellas empiecen en el contenido y no en la instalación. El
segundo bloque usa ese entorno recién montado para algo real, que es la mejor forma de verificar
que quedó bien.

---

## Contenido de la carpeta

| Carpeta | Qué es | Sesión |
|---|---|---|
| `07 De-Texto-a-Respuesta/07_De_Texto_a_Respuesta.ipynb` | Abre la caja negra: tokenización, la tabla de embeddings dentro del modelo, las capas de atención causal, los logits, la temperatura y el bucle autorregresivo escrito a mano. Todo local, sin llave de API. | 10 (cierre) |
| `08 Building-a-Chat/Agente_Basico.ipynb` | Agente conversacional con LangChain + `openai/gpt-oss-120b` (Groq): modelo, roles y memoria como lista de mensajes. | Referencia |
| `08 Building-a-Chat/Agente_Intermedio.ipynb` | El mismo agente con dos herramientas (búsqueda web y calculadora segura sin `eval()`). El modelo decide cuándo usarlas. | Referencia |
| `09 RAG-Completo/09_RAG_Completo.ipynb` | Cierra el ciclo de RAG: generación con Groq, el prompt de sistema medido con un experimento, y la elección del recuperador con datos. | 11 |
| `10 App-RAG-Streamlit/` | La aplicación desplegable: `streamlit_app.py`, `rag_core.py`, `corpus_diplomado.py` y la guía de despliegue. | 11 |
| `11 Entorno-Local-VSCode/` | Guía de instalación (Mac y Windows) y `verificar_entorno.py`, que revisa siete condiciones y dice qué falta. | 12 |
| `12 Pagina-Personal-GitHub-Pages/` | Guía de publicación y una plantilla HTML de una sola página, responsiva y sin dependencias. | 12 |

Los notebooks de `08 Building-a-Chat` son material previo y siguen vigentes; se usan como
referencia del patrón de agente con herramientas, que es hacia donde apuntan las sesiones
posteriores con Agno.

> **Sobre la numeración.** Los números continúan la secuencia de todo `02 Temas selectos`
> (01 árboles, 02–03 redes neuronales, 04–06 *embeddings*), de modo que el número de la carpeta y
> el del notebook que contiene siempre coinciden.

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

> **Los nombres de modelo caducan.** Groq retiró `llama-3.3-70b-versatile` de la capa gratuita el
> **16 de agosto de 2026**; el material está actualizado a `openai/gpt-oss-120b` (y
> `openai/gpt-oss-20b` como opción rápida). Cuando vuelva a pasar, el síntoma es un
> `404 ... model_not_found`: el notebook 09 trae una celda que le pregunta a la llave qué modelos
> puede usar hoy, y `rag_core.modelos_disponibles()` hace lo mismo desde la app. Conviene
> **verificarlo el día anterior a la clase**.

El notebook 07 es la excepción: **no necesita llave ni cuenta**, porque el modelo corre localmente.

### Descarga del modelo del notebook 07

Son ~500 MB desde Hugging Face (`datificate/gpt2-small-spanish`), una sola vez. Conviene arrancar
la sección 0 del notebook apenas empiece el bloque, para que baje mientras se explica el mapa.
Si ese repositorio no responde, el notebook cae automáticamente a `gpt2` y avisa que los números
del texto ya no van a coincidir. En Colab la descarga se repite en cada sesión, porque la caché no
se conserva.

### Cuenta de GitHub

Necesaria en las dos sesiones adicionales (para desplegar en Streamlit y para publicar la página).
Si alguien no la tiene, conviene crearla antes. La instalación de Git está documentada en
`00 Notas/Manual_Git_Mac_Windows_2026.pdf`.

### Dónde corre cada cosa

| Material | Dónde |
|---|---|
| Notebook `07_De_Texto_a_Respuesta.ipynb` | Google Colab o local (instala solo lo que falte; sin GPU) |
| Notebook `09_RAG_Completo.ipynb` | Google Colab (instala solo lo que falte) |
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
empate 6/10 en parafraseadas). La sección 7 del notebook 09 desarrolla ese hallazgo y explica por
qué ocurre con un corpus chico y bien escrito, y en qué condiciones se invertiría.

Es una de las lecciones que más se aprovechan de estas sesiones: **el lugar donde se va a
desplegar es parte del diseño**, y la técnica más nueva no es automáticamente la mejor para el
problema que se tiene enfrente.

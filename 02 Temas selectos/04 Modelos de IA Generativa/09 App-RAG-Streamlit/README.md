# 09 — App RAG desplegable (Streamlit)

Aplicación web que responde preguntas sobre el Módulo V usando **solo** las notas del curso.
Es la versión "producto" de lo que construimos en el notebook `08_RAG_Completo.ipynb`.

**Al terminar esta parte tendrás una URL pública, tuya, que puedes compartir con quien quieras.**

## Qué hay en esta carpeta

| Archivo | Qué es |
|---|---|
| `streamlit_app.py` | La interfaz. Solo se ocupa de lo visual: barra lateral, chat, expansores. |
| `rag_core.py` | La lógica de RAG (indexar, recuperar, armar el prompt, generar). Sin nada de Streamlit, para poder probarla sola. |
| `corpus_diplomado.py` | La base de conocimiento: 29 fragmentos de las notas del módulo. **Este es el archivo que vas a cambiar para hacer tuya la app.** |
| `requirements.txt` | Las dependencias que instalará Streamlit Cloud. |

## Por qué esta app no usa embeddings

En el notebook comparamos los dos recuperadores sobre este mismo corpus con 18 preguntas de
respuesta conocida, y TF-IDF **no perdió**: 8/8 contra 7/8 en preguntas normales y un empate 6/10
en preguntas parafraseadas. Con un corpus chico y bien escrito, coincidir literalmente es una
señal muy fuerte. Y la decisión quedó cerrada por el despliegue:

| Recuperador | RAM medida | ¿Cabe en Streamlit Community Cloud (1 GB)? |
|---|---|---|
| TF-IDF (`scikit-learn`) | ~150 MB | Sí, con holgura |
| `all-MiniLM-L6-v2` (solo inglés) | 597 MB | Apenas, y el corpus tendría que estar en inglés |
| `paraphrase-multilingual-MiniLM-L12-v2` | 1,372 MB | **No** |

El plan gratuito de Streamlit da **1 GB de RAM**. Un modelo multilingüe no cabe, y el corpus está
en español. Por eso la app usa TF-IDF: es una decisión de ingeniería tomada con números, no una
simplificación. Donde TF-IDF sí se queda corto es en preguntas muy parafraseadas, y eso lo
compensamos con dos defensas: recuperar varios fragmentos (`k`, porque el acierto en el top-3 sube
a 8/10) y un prompt de sistema que obliga al modelo a admitir cuando el contexto no le alcanza.

## Probarla en tu computadora (opcional)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Desplegarla en Streamlit Community Cloud

Necesitas una cuenta de GitHub y una llave de Groq. Las dos son gratuitas.

### 1. Consigue tu llave de Groq

Entra a [console.groq.com/keys](https://console.groq.com/keys), crea una cuenta y genera una llave.
Empieza con `gsk_...`. **Cópiala en ese momento: no se vuelve a mostrar.**

> La app **nunca** guarda tu llave. Cada visitante escribe la suya en la barra lateral, así que
> puedes compartir la URL sin que nadie gaste tu cuota.

### 2. Crea tu propio repositorio

En GitHub, **New repository** → nómbralo `asistente-modulo-v` → **Public** → *Create*.

Sube los cuatro archivos de esta carpeta **a la raíz** del repositorio nuevo (no dentro de
subcarpetas: Streamlit Cloud busca `requirements.txt` en la raíz). Puedes arrastrarlos con
*Add file → Upload files*, o desde la terminal:

```bash
git clone https://github.com/TU_USUARIO/asistente-modulo-v.git
cd asistente-modulo-v
# copia aquí streamlit_app.py, rag_core.py, corpus_diplomado.py y requirements.txt
git add .
git commit -m "Primera versión del asistente"
git push
```

### 3. Despliega

1. Entra a [share.streamlit.io](https://share.streamlit.io) e inicia sesión **con GitHub**.
2. *Create app* → *Deploy a public app from GitHub*.
3. Llena los campos:
   - **Repository:** `TU_USUARIO/asistente-modulo-v`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
4. *Deploy*. El primer arranque tarda **2 a 4 minutos** mientras instala las dependencias.

Tu app queda en `https://TU_USUARIO-asistente-modulo-v-....streamlit.app`.

### 4. Pruébala

Pega tu llave en la barra lateral y haz estas cuatro pruebas, en este orden:

1. **Una pregunta del temario** — *¿Cuál es la diferencia entre Ridge y Lasso?*
   Abre el expansor "Fragmentos recuperados" y verifica que la respuesta cite lo que ahí dice.
2. **Una pregunta fuera del temario** — *¿Cuál es la mejor receta de tacos al pastor?*
   Debe contestar que no tiene esa información, **sin llamar al modelo**.
3. **Apaga el interruptor "Usar RAG"** y repite la pregunta 1. Compara: sin contexto el modelo
   responde de memoria, sin citar y con riesgo de inventar detalles.
4. **Sube la temperatura a 1.0** y repite la misma pregunta tres veces. Observa cuánto cambia.

## Cómo hacerla tuya

Lo único que tienes que tocar es `corpus_diplomado.py`. Sustituye los fragmentos por contenido de
tu área —un reglamento, tus apuntes, la documentación de tu trabajo, un informe— respetando el
formato:

```python
{"sesion": 1, "titulo": "Un título corto y descriptivo",
 "texto": "Un párrafo autocontenido de entre 40 y 80 palabras."}
```

Tres reglas que sí importan:

- **Un fragmento, una idea.** Si un fragmento habla de cinco cosas, su vector queda en medio de
  todas y no se parece a ninguna pregunta en particular.
- **Ni muy largo ni muy corto.** Muy largo diluye; muy corto parte la respuesta en dos fragmentos
  y el modelo solo recibe la mitad.
- **El título pesa doble** en el índice (ver `rag_core.py`), así que conviene que contenga las
  palabras con las que alguien buscaría ese contenido.

Cambia también el título y los ejemplos de `streamlit_app.py` para que hablen de tu tema. Cada
`git push` vuelve a desplegar la app automáticamente.

## Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| `Error 401 - Invalid API Key` | La llave está mal copiada o fue revocada. Genera una nueva en console.groq.com/keys. |
| `Error 429 - Rate limit` | Se agotó la cuota gratuita del minuto. Espera un momento o cambia al modelo `llama-3.1-8b-instant`. |
| La app dice "no encontré nada" con preguntas que sí son del temario | El umbral está muy alto. Bájalo en la barra lateral. |
| `ModuleNotFoundError` al desplegar | `requirements.txt` no está en la raíz del repositorio. |
| La app "duerme" y tarda en abrir | Normal: en el plan gratuito las apps se suspenden tras 12 horas sin visitas. El primer acceso la despierta. |

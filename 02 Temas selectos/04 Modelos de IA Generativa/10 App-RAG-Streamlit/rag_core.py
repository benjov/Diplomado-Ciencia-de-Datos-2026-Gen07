"""Lógica del sistema RAG, sin nada de interfaz.

Separamos el núcleo de la interfaz a propósito: así este archivo se puede probar
solo, y `streamlit_app.py` se queda únicamente con lo visual. Es el mismo código
que construimos paso a paso en el notebook `09_RAG_Completo.ipynb`.

Los tres pasos de RAG viven aquí:
  1. indexar()          -> convierte el corpus en una matriz consultable
  2. recuperar()        -> encuentra los fragmentos más cercanos a la pregunta
  3. construir_mensajes() + responder() -> arma el prompt y llama al modelo
"""

from __future__ import annotations

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Palabras vacías del español. Sin ellas, preguntas como "¿para qué sirve...?"
# se parecen a cualquier documento solo por las palabras de relleno.
STOPWORDS_ES = [
    "a", "al", "algo", "ante", "antes", "como", "con", "contra", "cual", "cuales", "cuando",
    "cuanto", "de", "del", "desde", "donde", "dos", "el", "ella", "ellas", "ellos", "en",
    "entre", "era", "es", "esa", "ese", "eso", "esta", "estas", "este", "esto", "estos", "ha",
    "hace", "hacer", "hasta", "hay", "la", "las", "le", "les", "lo", "los", "mas", "más", "me",
    "mi", "mis", "mucho", "muy", "ni", "no", "nos", "o", "otra", "otro", "para", "pero", "por",
    "porque", "que", "qué", "quien", "se", "si", "sin", "sobre", "son", "su", "sus", "tan",
    "te", "tiene", "todo", "todos", "tu", "un", "una", "uno", "unos", "y", "ya", "yo",
    "sirve", "cómo", "cuál", "cuáles", "quiero", "tengo",
]

# Groq retiró "llama-3.3-70b-versatile" de la capa gratuita el 2026-08-16.
# Si esto vuelve a pasar, `modelos_disponibles()` dice qué ofrece hoy tu llave.
MODELO_POR_DEFECTO = "openai/gpt-oss-120b"
MODELO_RAPIDO = "openai/gpt-oss-20b"

PROMPT_SISTEMA = """Eres el asistente del Módulo V del Diplomado de Ciencia de Datos de la FES Acatlán, UNAM.

Reglas que debes respetar siempre:
1. Responde ÚNICAMENTE con la información de los fragmentos de CONTEXTO que recibes.
2. Cita entre corchetes el número del fragmento que respalda cada afirmación, así: [1].
3. Si el contexto no contiene la respuesta, dilo con claridad y no la completes con
   conocimiento propio. Es preferible admitir que no sabes a inventar.
4. Responde en español, en un tono claro y didáctico, en un máximo de seis oraciones.
5. No inventes números, fechas ni nombres que no estén en el contexto."""


def indexar(corpus, stopwords=STOPWORDS_ES):
    """Paso 1 de RAG: convierte el corpus en una matriz TF-IDF consultable.

    El título se repite dos veces a propósito: pesa más que el cuerpo, lo que
    mejora bastante la recuperación (lo medimos en el notebook).
    """
    documentos = [f"{d['titulo']}. {d['titulo']}. {d['texto']}" for d in corpus]
    vectorizador = TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        ngram_range=(1, 2),
        sublinear_tf=True,
        stop_words=stopwords,
    )
    matriz = vectorizador.fit_transform(documentos)
    return vectorizador, matriz


def recuperar(pregunta, corpus, vectorizador, matriz, k=3, umbral=0.05):
    """Paso 2 de RAG: devuelve los k fragmentos más parecidos por encima del umbral.

    Devuelve una lista de diccionarios con el documento y su puntaje. Si ninguno
    supera el umbral, devuelve la lista vacía: esa es la señal de que la pregunta
    cae fuera de la base de conocimiento.
    """
    vector_pregunta = vectorizador.transform([pregunta])
    puntajes = (matriz @ vector_pregunta.T).toarray().ravel()

    mejores = np.argsort(-puntajes)[:k]
    return [
        {**corpus[i], "puntaje": float(puntajes[i])}
        for i in mejores
        if puntajes[i] >= umbral
    ]


def formatear_contexto(fragmentos):
    """Convierte los fragmentos recuperados en el bloque de texto que ve el modelo."""
    return "\n\n".join(
        f"[{n}] (Sesión {f['sesion']} — {f['titulo']}) {f['texto']}"
        for n, f in enumerate(fragmentos, start=1)
    )


def construir_mensajes(pregunta, fragmentos, historial=None, prompt_sistema=PROMPT_SISTEMA):
    """Paso 3a de RAG: arma la lista de mensajes que se le manda al modelo.

    `historial` es una lista de dicts {"role": ..., "content": ...} con los turnos
    previos, para que el asistente entienda preguntas de seguimiento.
    """
    mensajes = [{"role": "system", "content": prompt_sistema}]
    mensajes.extend(historial or [])

    contenido = (
        f"CONTEXTO:\n{formatear_contexto(fragmentos)}\n\n"
        f"PREGUNTA: {pregunta}"
    )
    mensajes.append({"role": "user", "content": contenido})
    return mensajes


def modelos_disponibles(cliente):
    """Pregunta a la API qué modelos puede usar esta llave, hoy.

    Los proveedores retiran modelos cada pocos meses (a este curso le pasó con
    `llama-3.3-70b-versatile` el 2026-08-16). Cuando una llamada falle con un 404,
    esta función dice con qué reemplazarlo sin tener que buscar en la documentación.
    """
    return sorted(m.id for m in cliente.models.list().data)


def responder(cliente, mensajes, modelo=MODELO_POR_DEFECTO, temperatura=0.2, max_tokens=700):
    """Paso 3b de RAG: llama al modelo de lenguaje y devuelve el texto de la respuesta."""
    try:
        respuesta = cliente.chat.completions.create(
            model=modelo,
            messages=mensajes,
            temperature=temperatura,
            max_tokens=max_tokens,
        )
    except Exception as error:
        if "model_not_found" in str(error) or "does not exist" in str(error):
            raise RuntimeError(
                f"El proveedor ya no ofrece el modelo '{modelo}'. "
                f"Modelos disponibles hoy para tu llave: "
                f"{', '.join(modelos_disponibles(cliente))}"
            ) from None
        raise
    return respuesta.choices[0].message.content


MENSAJE_SIN_CONTEXTO = (
    "No encontré nada sobre eso en las notas del Módulo V, así que prefiero no responder "
    "para no inventar. Prueba con una pregunta sobre los temas del diplomado: regresión, "
    "agrupamiento, modelos de texto, embeddings o agentes."
)


def preguntar(pregunta, corpus, vectorizador, matriz, cliente=None,
              k=3, umbral=0.05, historial=None, **kwargs):
    """Pipeline completo: recuperar -> armar prompt -> generar.

    Si no se recupera nada por encima del umbral, ni siquiera se llama al modelo:
    se responde con un mensaje fijo. Eso ahorra una llamada y, sobre todo, evita
    que el modelo alucine sobre un contexto que no viene al caso.
    """
    fragmentos = recuperar(pregunta, corpus, vectorizador, matriz, k=k, umbral=umbral)

    if not fragmentos:
        return {"respuesta": MENSAJE_SIN_CONTEXTO, "fragmentos": [], "se_llamo_al_modelo": False}

    mensajes = construir_mensajes(pregunta, fragmentos, historial=historial)

    if cliente is None:      # modo de prueba: devuelve el prompt sin llamar al modelo
        return {"respuesta": None, "fragmentos": fragmentos,
                "mensajes": mensajes, "se_llamo_al_modelo": False}

    texto = responder(cliente, mensajes, **kwargs)
    return {"respuesta": texto, "fragmentos": fragmentos, "se_llamo_al_modelo": True}

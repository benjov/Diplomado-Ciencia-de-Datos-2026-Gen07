"""Asistente del Módulo V — aplicación RAG desplegable en Streamlit Community Cloud.

Toda la lógica vive en `rag_core.py`; este archivo es solo la interfaz.
Para correrla localmente:  streamlit run streamlit_app.py
"""

import streamlit as st
from groq import Groq

from corpus_diplomado import CORPUS
from rag_core import (
    MENSAJE_SIN_CONTEXTO,
    PROMPT_SISTEMA,
    construir_mensajes,
    indexar,
    recuperar,
    responder,
)

st.set_page_config(page_title="Asistente del Módulo V", page_icon="🎓", layout="centered")


# --------------------------------------------------------------------------
# Índice: se construye una sola vez y se reutiliza entre recargas
# --------------------------------------------------------------------------
@st.cache_resource
def cargar_indice():
    return indexar(CORPUS)


vectorizador, matriz = cargar_indice()


# --------------------------------------------------------------------------
# Barra lateral: configuración
# --------------------------------------------------------------------------
with st.sidebar:
    st.header("Configuración")

    api_key = st.text_input(
        "Tu llave de Groq",
        type="password",
        help="Se obtiene gratis en console.groq.com. No se guarda en ningún lado: "
             "vive solo en tu sesión del navegador.",
    )
    st.caption("[Crear una llave gratuita](https://console.groq.com/keys)")

    st.divider()

    modelo = st.selectbox(
        "Modelo",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
        help="El de 70B responde mejor; el de 8B responde más rápido.",
    )
    k = st.slider("Fragmentos a recuperar (k)", 1, 6, 3,
                  help="Cuántos documentos del corpus se le entregan al modelo.")
    temperatura = st.slider("Temperatura", 0.0, 1.0, 0.2, 0.1,
                            help="0 = respuestas estables. Valores altos = más variadas.")
    umbral = st.slider("Umbral de similitud", 0.0, 0.3, 0.05, 0.01,
                       help="Por debajo de este puntaje se considera que la pregunta "
                            "cae fuera de la base de conocimiento.")

    st.divider()

    usar_rag = st.toggle(
        "Usar RAG", value=True,
        help="Apágalo para preguntarle al modelo sin darle el contexto del curso. "
             "Sirve para comparar las dos respuestas.",
    )

    if st.button("Borrar conversación"):
        st.session_state.historial = []
        st.rerun()

    st.divider()
    st.caption(f"Base de conocimiento: {len(CORPUS)} fragmentos de las notas del Módulo V.")


# --------------------------------------------------------------------------
# Encabezado
# --------------------------------------------------------------------------
st.title("🎓 Asistente del Módulo V")
st.caption(
    "Diplomado de Ciencia de Datos · FES Acatlán, UNAM — "
    "responde preguntas sobre el módulo usando **solo** las notas del curso."
)

if not api_key:
    st.info(
        "Para empezar, pega tu llave de Groq en la barra lateral. "
        "Es gratuita y se obtiene en console.groq.com/keys.",
        icon="🔑",
    )

with st.expander("¿Qué puedo preguntarle?"):
    st.markdown(
        "- ¿Cuál es la diferencia entre Ridge y Lasso?\n"
        "- ¿Cómo decido cuántos grupos usar en un agrupamiento?\n"
        "- ¿Qué hago si mi variable dependiente es una calificación del 1 al 5?\n"
        "- ¿Para qué sirve el prompt de sistema?\n"
        "- ¿Cuánto vale cada tarea en la calificación del módulo?\n\n"
        "Y para ver qué pasa cuando la pregunta se sale del temario, prueba con algo "
        "como *¿cuál es la mejor receta de tacos al pastor?*"
    )


# --------------------------------------------------------------------------
# Conversación
# --------------------------------------------------------------------------
if "historial" not in st.session_state:
    st.session_state.historial = []

for turno in st.session_state.historial:
    with st.chat_message(turno["role"]):
        st.markdown(turno["content"])
        if turno.get("fragmentos"):
            with st.expander(f"Fragmentos recuperados ({len(turno['fragmentos'])})"):
                for n, f in enumerate(turno["fragmentos"], start=1):
                    st.markdown(
                        f"**[{n}] Sesión {f['sesion']} — {f['titulo']}** "
                        f"· similitud {f['puntaje']:.3f}\n\n{f['texto']}"
                    )

pregunta = st.chat_input("Escribe tu pregunta sobre el módulo...")

if pregunta:
    st.session_state.historial.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.chat_message("assistant"):
        if not api_key:
            texto, fragmentos = "Falta tu llave de Groq: pégala en la barra lateral.", []
            st.warning(texto)

        else:
            # Solo mandamos al modelo los turnos previos de texto, no los fragmentos.
            historial_previo = [
                {"role": t["role"], "content": t["content"]}
                for t in st.session_state.historial[:-1]
            ][-6:]

            if not usar_rag:
                fragmentos = []
                mensajes = (
                    [{"role": "system", "content":
                      "Eres un asistente del Diplomado de Ciencia de Datos. Responde en español."}]
                    + historial_previo
                    + [{"role": "user", "content": pregunta}]
                )
            else:
                fragmentos = recuperar(pregunta, CORPUS, vectorizador, matriz,
                                       k=k, umbral=umbral)
                mensajes = construir_mensajes(
                    pregunta, fragmentos, historial=historial_previo,
                    prompt_sistema=PROMPT_SISTEMA,
                )

            if usar_rag and not fragmentos:
                # Ni siquiera llamamos al modelo: nos ahorramos la llamada y el riesgo.
                texto = MENSAJE_SIN_CONTEXTO
                st.markdown(texto)
            else:
                try:
                    with st.spinner("Consultando al modelo..."):
                        texto = responder(Groq(api_key=api_key), mensajes,
                                          modelo=modelo, temperatura=temperatura)
                    st.markdown(texto)
                except Exception as error:
                    texto = f"No se pudo consultar al modelo: {error}"
                    st.error(texto)
                    fragmentos = []

            if fragmentos:
                with st.expander(f"Fragmentos recuperados ({len(fragmentos)})"):
                    for n, f in enumerate(fragmentos, start=1):
                        st.markdown(
                            f"**[{n}] Sesión {f['sesion']} — {f['titulo']}** "
                            f"· similitud {f['puntaje']:.3f}\n\n{f['texto']}"
                        )

    st.session_state.historial.append(
        {"role": "assistant", "content": texto, "fragmentos": fragmentos}
    )

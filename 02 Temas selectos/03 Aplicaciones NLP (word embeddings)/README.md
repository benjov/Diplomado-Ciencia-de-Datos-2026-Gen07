# 03 Aplicaciones NLP (word embeddings)

**Sesión del módulo:** Sesión 10 (sábado) — Embeddings + IA generativa/agentes (primera mitad,
cierre de módulo).
**Prerrequisito:** Sesión 9 (redes neuronales) y, de la Sesión 8, Naive Bayes/regresión
logística de texto (`04 Análisis de texto`).
**Notas relacionadas:** `main.tex`, capítulo 2, sección "Aplicaciones de modelos de lenguaje
natural con bases vectoriales (word embeddings)" (embeddings estáticos/contextuales, distancias
y similitud entre vectores, token vs. oración, introducción a RAG).

## Objetivo de la unidad

Entender qué es un embedding, cómo medir similitud entre vectores, la diferencia entre
embeddings de token (BERT) y de oración (dual encoder/SBERT), y cómo se usan para recuperar
información relevante (RAG) antes de pasarla a un LLM.

## Contenido

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `04 Intro_to_Embeddings` | Introducción práctica a embeddings de imágenes (MNIST) y de oraciones, y comparación de cuatro métricas de distancia (euclidiana, Manhattan, producto punto, coseno). Usa modelos abiertos vía `sentence-transformers`, no la API de OpenAI. | Sí ("Tu turno") |
| `05 Embeddings/05 Token_vs_Sentence_Embeddings.ipynb` | Compara embeddings de token (BERT) contra embeddings de oración (dual encoder/SBERT), evaluados contra juicios humanos de similitud. | No |
| `05 Embeddings/06_Using_Embeddings_in_RAG_Inference.ipynb` | Introduce RAG (Retrieval-Augmented Generation): recuperación por similitud pura y con dual encoder, como paso previo a la generación. Es el puente hacia `04 Modelos de IA Generativa`. | No |

## Nota pedagógica

Este material asume que el estudiante ya vio redes neuronales (Sesión 9); si se imparte antes,
conviene una introducción breve a "qué es un embedding" (ver también `02 Modelos de agrupamiento
/06_PCA/02_PCA_Texto.ipynb`, que usa embeddings de texto sin explicarlos, varias sesiones antes).

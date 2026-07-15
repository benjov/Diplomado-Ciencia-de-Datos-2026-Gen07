# 04 Modelos de IA Generativa

**Sesión del módulo:** Sesión 10 (sábado) — Embeddings + IA generativa/agentes (segunda mitad,
cierre de módulo).
**Prerrequisito:** `03 Aplicaciones NLP (word embeddings)` (misma sesión).
**Notas relacionadas:** `main.tex`, capítulo 2, sección "Introducción a los LLMs y aplicaciones
basadas en LLMs" (LLMs base vs. instruction-tuned, prompt engineering, agentes y uso de
herramientas — patrón ReAct).

## Objetivo de la unidad

Pasar de "usar un LLM para generar texto" a "diseñar un sistema que combine un LLM con
herramientas externas", entendiendo el patrón de razonamiento detrás de un agente y los riesgos
prácticos de darle herramientas a un modelo (dependencia externa, latencia, variabilidad,
seguridad).

## Contenido

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `06 Intro-to-IA` | Solo contiene un enlace a una presentación (Canva) — es apoyo para exposición en vivo, no un notebook ejecutable. | N/A |
| `07 Building-a-Chat/Agente_Basico.ipynb` | Agente conversacional simple con LangChain + Llama 3.3 70B (vía Groq): modelo + memoria de conversación, sin herramientas todavía. | Sí (preguntas de reflexión por sección) |
| `07 Building-a-Chat/Agente_Intermedio.ipynb` | Mismo agente, ahora con dos herramientas (búsqueda web y calculadora segura sin `eval()`): el modelo decide cuándo usar cada una. Es el **ejemplo insignia** del módulo (destacado en el `README.md` raíz del repo). | Sí (preguntas de reflexión + ejercicio de comparación) |

## Orden recomendado

Ver `Agente_Basico.ipynb` antes que `Agente_Intermedio.ipynb`: el segundo se apoya explícitamente
en las limitaciones del primero ("¿Qué mejora respecto al agente básico?") para introducir el
concepto de herramienta.

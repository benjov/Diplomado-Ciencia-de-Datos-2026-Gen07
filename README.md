# Diplomado en Ciencia de Datos — Módulo V (Generación 07, 2026)

**Introducción a la Ciencia de Datos: herramientas para el aprendizaje automatizado en las ciencias sociales y humanidades**

FES Acatlán, UNAM · Profesor: Benjamín Oliva Vázquez · Contacto: benjov@ciencias.unam.mx

---

## Qué es este repositorio

Este repositorio contiene el material de código del Módulo V del Diplomado en Ciencia de Datos
de la FES Acatlán (UNAM): notebooks de Python (`.ipynb`) y R Markdown (`.Rmd`) que se ejecutan en
clase y en las tareas del módulo. El Módulo V cubre dos bloques:

1. **Aplicaciones de ML con R y Python** — regresión lineal, agrupamiento (clustering), modelos
   categóricos (logit/probit) y análisis de texto.
2. **Temas selectos** — árboles de decisión y bosques aleatorios, redes neuronales, embeddings y
   modelos de lenguaje (LLMs), incluyendo agentes con herramientas.

El desarrollo teórico correspondiente (definiciones, derivaciones, citas) vive en las notas de
clase (documento en LaTeX, fuera de este repositorio); aquí está la parte ejecutable.

## Estructura del repositorio

```
00 Notas/                          — Materiales de referencia
01 Aplicaciones de ML con R y Python/
    01 Modelos de regresión lineal/          (incluye 00_Causalidad_DAGs, Sesión 1)
    02 Modelos de agrupamiento/
    03 Modelos de categoricos/
    04 Análisis de texto/
02 Temas selectos/
    01 Modelos de árboles y bosques aleatorios/
    02 Modelos de redes neuronales/
    03 Aplicaciones NLP (word embeddings)/
    04 Modelos de IA Generativa/
Tarea 01/                          — Regresión + Agrupamiento
Tarea 02/                          — Análisis de texto
Reporte Final/                     — Ensayo individual de cierre
```

Cada una de las 8 subcarpetas temáticas tiene su propio `README.md` con el objetivo de
aprendizaje, prerrequisitos y una tabla del contenido (qué hace cada notebook/Rmd y si incluye
ejercicios de reflexión).

## Calendario de sesiones

El módulo se imparte en 10 sesiones (viernes 3.5h + sábado 4.5h, dos por semana):

| # | Tema | Material de este repo |
|---|---|---|
| 1 | Esperanza condicional, causalidad, DAGs | `01 Modelos de regresión lineal/00_Causalidad_DAGs` |
| 2 | Regresión lineal (MCO, bondad de ajuste) | `01 Modelos de regresión lineal` |
| 3 | Clustering I (PCA, K-means) | `02 Modelos de agrupamiento` (PCA, Customer, Countries) |
| 4 | Clustering II (series de tiempo, app) | `02 Modelos de agrupamiento` (Defunciones, series de tiempo, Shiny App) |
| 5 | Modelos categóricos (Logit) | `03 Modelos de categoricos` (Logit Delitos) |
| 6 | Logit ordinal + app | `03 Modelos de categoricos` (Logit Ordenado, App) |
| 7 | Análisis de texto I (regex, PDFs, n-gramas) | `04 Análisis de texto` (regex, PDF, n-gramas) |
| 8 | Análisis de texto II (Naive Bayes, logit de texto) | `04 Análisis de texto` (Naive Bayes, regresión logística) |
| 9 | Árboles/bosques + redes neuronales | `02 Temas selectos/01` y `02` |
| 10 | Embeddings + IA generativa/agentes | `02 Temas selectos/03` y `04` (cierre de módulo) |

## Entregables

| Entregable | Contenido | Entrega |
|---|---|---|
| Tarea 01 | Regresión lineal + Agrupamiento | Miércoles 26 de agosto |
| Tarea 02 | Análisis de texto | Miércoles 9 de septiembre |
| Reporte Final | Ensayo individual de reflexión | Viernes 18 de septiembre |

Instrucciones y rúbricas completas en el `README.md` de cada carpeta de tarea.

## Sobre el bloque de IA Generativa

`02 Temas selectos/04 Modelos de IA Generativa` incluye dos notebooks progresivos: un agente
conversacional simple (`Agente_Basico.ipynb`) y un agente con herramientas —búsqueda web y
calculadora segura, sin `eval()`— que decide cuándo usarlas (`Agente_Intermedio.ipynb`). Ambos
usan LangChain con Llama 3.3 70B vía Groq (sin costo para el estudiante). El objetivo no es que
domines la ingeniería del framework, sino que entiendas cómo se diseña un sistema que combina un
modelo de lenguaje con herramientas externas, y qué implicaciones prácticas y éticas tiene esa
decisión (dependencia de servicios externos, latencia, variabilidad de resultados).

## Generaciones anteriores

Este módulo se ha impartido en generaciones previas del Diplomado (Gen 01–06, 2023–2026); esos
repositorios están disponibles en [github.com/benjov](https://github.com/benjov).

## Contacto

- benjov@ciencias.unam.mx
- [github.com/benjov](https://github.com/benjov)
- [Grabaciones de clase](https://www.youtube.com/@benjamin_oliva_educ)

# 04 Análisis de texto

**Sesiones del módulo:** Sesión 7 (viernes) — Análisis de texto I (regex, PDFs, n-gramas);
Sesión 8 (sábado) — Análisis de texto II (Naive Bayes, logit de texto).
**Prerrequisito:** Sesión 6 (Logit ordinal). No requiere clustering ni PCA.
**Notas relacionadas:** `main.tex`, capítulo 2, sección "Aplicación de modelos de análisis de
texto" (expresiones regulares, N-gramas, Naive Bayes, regresión logística aplicada a texto).

## Objetivo de la unidad

Extraer y limpiar texto con expresiones regulares, modelarlo con n-gramas, y clasificarlo con
dos algoritmos de línea base (Naive Bayes y regresión logística).

## Contenido — Sesión 7 (regex, PDFs, n-gramas)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `11_Expresiones_Regulares` | Introducción a expresiones regulares en Python para procesamiento de texto. **Nota:** la celda 13 deja guardado un `AttributeError` (`match.group()` sobre `None`) sin explicar que es intencional — aclarar en clase que ilustra que una búsqueda fallida regresa `None`. | Sí (varios) |
| `12_Leer_Datos_PDF` | Extracción de datos tabulares desde PDF (precios máximos vigentes, publicaciones oficiales). Es más script que notebook narrativo (3 celdas markdown vs. 16 de código). | No |
| `13_N_Grams` | Modelos de lenguaje con n-gramas, desde la intuición hasta un modelo funcional. | Sí (varios) |

## Contenido — Sesión 8 (Naive Bayes, logit de texto)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `14_Naive_Bayes/14_Naive_Bayes_Classifier.ipynb` | Naive Bayes aplicado a datos tabulares (`adult.csv`), como introducción al algoritmo antes de aplicarlo a texto. | No |
| `14_Naive_Bayes/14_Naive_Bayes_Classifier_Text.ipynb` | Naive Bayes aplicado a clasificación de texto (`noticias.csv`). | No |
| `15_Logistic_Regression` | Regresión logística para análisis de sentimiento sobre tweets (Twitter Sentiment Analysis). | Sí (varios) |

## Nota de navegación

Ambos notebooks de `14_Naive_Bayes` comparten el prefijo `14_`; el sufijo (`Classifier` vs.
`Classifier_Text`) es lo que distingue el ejemplo tabular del de texto — revisarlos en ese orden.
`main.tex`, subsección "Clasificación de texto con Naive Bayes", cita la carpeta
`14_Naive_Bayes` en general, no un archivo específico.

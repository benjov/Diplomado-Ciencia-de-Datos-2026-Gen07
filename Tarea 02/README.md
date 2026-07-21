# Proyecto final: Análisis de texto sobre violencia contra las mujeres

## Objetivo

Aplicar técnicas de análisis de texto y aprendizaje automático trabajadas en el curso, para explorar, procesar y modelar un conjunto de noticias sobre violencia contra las mujeres.

---

## Fuente de datos

Descarga el conjunto de datos desde:

**https://zenodo.org/records/6958808**

Utiliza el archivo `ViolenceAgainstWomen.json`.

> **Nota:** usa como referencia el código **“Lector de datos.ipynb”** para leer los datos contenidos en `ViolenceAgainstWomen.json`.

---

## Modalidad

La actividad debe realizarse en equipos.

## Instrucciones generales

1. Descarga y carga el dataset.

2. Desarrolla un análisis reproducible en **R, Python o ambos**.

3. Usa únicamente herramientas y enfoques de análisis de texto.

4. Documenta todas tus decisiones metodológicas.

5. Entrega:
   - código,
   - visualizaciones,
   - y reporte final en **PDF** o **notebook**.

## Actividades requeridas

### 1. Carga y exploración de datos

- Descargar y leer el archivo.

- Mostrar ejemplos de títulos y cuerpos de noticia.

- Identificar:

  - textos vacíos,

  - duplicados,

  - problemas de codificación,

  - campos incompletos.

- Reportar estadísticas básicas del corpus:

  - número de documentos,

  - longitud promedio de los textos,

  - número de palabras,

  - frecuencia de términos.

### 2. Limpieza y preprocesamiento

Usa procedimientos afines a los trabajados en clase, por ejemplo:

- normalización a minúsculas;

- limpieza de caracteres especiales;

- eliminación de signos de puntuación, números o patrones irrelevantes;

- uso de expresiones regulares cuando sea pertinente;

- tokenización;

- eliminación de stopwords, si la justificas.

Debes explicar por qué cada paso mejora el análisis.

### 3. Análisis de texto

Debes realizar **al menos dos** de las siguientes actividades:

#### A. Exploración con n-gramas

- Construye unigramas, bigramas o trigramas.

- Identifica patrones léxicos frecuentes.

- Interpreta qué expresiones aparecen de forma recurrente en las noticias.

- Presenta al menos una visualización de frecuencias (por ejemplo, barras horizontales ordenadas por frecuencia; evita nubes de palabras como única evidencia, ya que no permiten comparar magnitudes con precisión).

#### B. Clasificación con Naive Bayes

- Define una variable objetivo.

- Crea o adapta etiquetas para clasificar noticias.

- Entrena un modelo Naive Bayes.

- Evalúa su desempeño con métricas apropiadas.

#### C. Clasificación con regresión logística

- Plantea un problema de clasificación binaria o multiclase.

- Entrena un modelo de regresión logística.

- Reporta métricas de evaluación.

- Compara, si lo deseas, su desempeño con Naive Bayes.

#### D. Extracción o depuración de texto con expresiones regulares

- Identifica patrones textuales relevantes.

- Limpia encabezados, símbolos, fechas, etiquetas u otros elementos del texto.

- Muestra ejemplos antes y después de la limpieza.

- Explica cómo esa depuración mejora el análisis posterior.

### Estándares de visualización

Todas las visualizaciones del reporte (no solo las de la sección de n-gramas) deben cumplir con:

- título y ejes con etiquetas claras (unidades cuando aplique);

- el tipo de gráfico adecuado para lo que se muestra (por ejemplo, barras para comparar frecuencias entre categorías, no pastel con muchas categorías);

- si hay comparación entre grupos o modelos, un único gráfico que permita esa comparación directamente (en vez de gráficos separados difíciles de comparar entre sí).

## Restricciones metodológicas

### Se permite trabajar con:

- expresiones regulares,

- limpieza de texto,

- n-gramas,

- Naive Bayes,

- regresión logística.

### No se pide trabajar con:

- BERT,

- transformers,

- embeddings profundos,

- LLMs,

- visualización semántica avanzada.

## Estructura del reporte

### 1. Introducción

- Contexto del problema.

- Relevancia del análisis de noticias sobre violencia contra las mujeres.

- Objetivo del proyecto.

### 2. Descripción de los datos

- Origen del dataset.

- Estructura general.

- Problemas detectados en la exploración inicial.

### 3. Metodología

- Procesos de limpieza y preprocesamiento.

- Técnicas seleccionadas del curso.

- Justificación de cada elección.

### 4. Resultados

- Tablas y gráficos.

- Desempeño de modelos, si aplica.

- Hallazgos principales del análisis textual.

### 5. Discusión

- Interpretación crítica de los resultados.

- Limitaciones del análisis.

- Posibles sesgos de los datos o del modelo.

### 6. Conclusiones

- Principales aportaciones del trabajo.

- Posibles extensiones futuras dentro del marco del curso.

## Entregables

Cada equipo o estudiante deberá entregar:

- **código fuente** completo;

- **reporte** en PDF o notebook;

- visualizaciones incluidas en el reporte;

- una breve nota de ejecución, si el código requiere pasos específicos.

## Rúbrica de evaluación

| Criterio | Descripción | Puntos |
|---|---|---:|
| Uso adecuado de materiales del curso | El proyecto se apega claramente a las actividades de la clase. | 15 |
| Carga y exploración de datos | Lee correctamente el dataset, describe su estructura y detecta problemas básicos. | 10 |
| Limpieza y preprocesamiento | Aplica técnicas de limpieza coherentes con el corpus y bien justificadas. | 15 |
| Aplicación de técnicas del módulo | Implementa correctamente al menos dos actividades del bloque: expresiones regulares, n-gramas, Naive Bayes o regresión logística. | 25 |
| Evaluación e interpretación | Presenta resultados claros y los interpreta de forma pertinente. | 10 |
| Visualizaciones y tablas | Incluye gráficos y tablas relevantes, con el tipo de visualización adecuado, ejes/leyendas claras, y que efectivamente comunican el hallazgo (no solo decoración). | 15 |
| Calidad del código | Código ordenado, reproducible y entendible. | 5 |
| Calidad del reporte | Buena redacción, estructura clara y coherencia general. | 5 |

**Total: 100 puntos**

---

## Fecha de entrega

**9 de septiembre de 2026**

## Envío

Enviar **código y reporte** a: **benjov@ciencias.unam.mx**

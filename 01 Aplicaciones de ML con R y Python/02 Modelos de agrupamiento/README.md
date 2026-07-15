# 02 Modelos de agrupamiento

**Sesiones del módulo:** Sesión 3 (viernes) — Clustering I (PCA, K-means); Sesión 4 (sábado) —
Clustering II (series de tiempo, app).
**Prerrequisito:** Sesión 2 (regresión lineal).
**Notas relacionadas:** `main.tex`, capítulo de aprendizaje no supervisado (PCA, análisis
factorial, jerárquico, K-means, distancias de Minkowski, series de tiempo).

## Objetivo de la unidad

Reducir dimensionalidad con PCA y encontrar grupos homogéneos en los datos con distintos
algoritmos de clustering (K-means, jerárquico), incluyendo el caso especial de series de tiempo.

## Contenido — Sesión 3 (PCA, K-means)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `06_PCA/01_PCA.ipynb` | Introducción práctica a Análisis de Componentes Principales. | No |
| `06_PCA/02_PCA_Texto.ipynb` | Aplica PCA sobre embeddings de texto precalculados. Usa el concepto de "embedding" antes de que se formalice (eso es hasta la Sesión 10, `03 Aplicaciones NLP`) — ya tiene una nota de contexto al inicio del notebook aclarándolo. | Sí |
| `07_UnsupervisedClustering/01 Clustering Customer` | K-means aplicado a segmentación de clientes. | Sí (varios) |
| `07_UnsupervisedClustering/02 Clustering Countries` | Clustering jerárquico + PCA aplicado a datos de países. | Sí (varios) |
| `07_UnsupervisedClustering/03 Defunciones` | K-means (y otros algoritmos) aplicado a datos de defunciones por COVID-19. | Sí (varios) |

## Contenido — Sesión 4 (series de tiempo, app)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `08_Unsupervised_Clustering_Time_Series/01_Stocks` | Introducción a clustering de series de tiempo (acciones bursátiles). | Sí |
| `08_Unsupervised_Clustering_Time_Series/02 Nodos PML` | Clustering de series de tiempo de precios eléctricos (K-means euclidiano, DTW y soft-DTW; verificado de punta a punta, corre en ~2 minutos). Usa los datos generados en `01 Modelos de regresión lineal/04_Generando_Datos_PML`. | Sí |
| `05 Shiny App/App-Base`, `05 Shiny App/App-Final` | Apps interactivas en R Shiny para explorar visualmente los resultados de clustering. | N/A (son apps, no notebooks) |

## Estado de verificación

`Clustering_Time_Series_PML.ipynb` se ejecutó de punta a punta (con `tslearn` instalado) y
corre sin errores en las 41 celdas, en poco más de 2 minutos en total. Tuvo dos bugs de
ejecución, ambos corregidos (ver `CLAUDE.md`): soft-DTW sobre datos horarios completos no
terminaba, y luego se encontró que DTW normal tenía el mismo problema — ambas métricas ahora
corren sobre el promedio diario de cada nodo (T=62 en vez de T=1488).

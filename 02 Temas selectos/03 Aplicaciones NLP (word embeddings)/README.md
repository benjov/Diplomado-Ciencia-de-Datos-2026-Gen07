# 03 Aplicaciones NLP (word embeddings)

**Sesión del módulo:** Sesión 10 — Embeddings e introducción a RAG.
**Duración:** 3.5 horas (210 minutos), incluido un receso.
**Prerrequisitos:** Sesión 3 (PCA), Sesión 4 (K-means y *silhouette*), Sesión 8 (bolsa de palabras
y clasificación de texto) y Sesión 9 (redes neuronales).
**Notas relacionadas:** `main.tex`, capítulo 2, sección *"Aplicaciones de modelos de lenguaje
natural con bases vectoriales (word embeddings)"*.

## Objetivo de la unidad

Que el estudiante pueda representar texto como vectores, medir similitud entre ellos con criterio,
evaluar la calidad de un modelo de embeddings contra un estándar externo, y construir un sistema
de recuperación de información (el primer paso de RAG) reconociendo sus modos de falla.

Esta unidad es el puente entre todo lo que se vio en el módulo y el bloque de IA generativa: los
embeddings toman las herramientas de las sesiones anteriores (PCA, K-means, similitud coseno,
redes neuronales) y las aplican a texto, y RAG conecta ese resultado con los LLM.

## Contenido

Los tres notebooks son secuenciales: cada uno usa resultados del anterior.

| # | Notebook | Duración | Qué hace |
|---|---|---|---|
| 1 | `04 Intro_to_Embeddings/04_Intro_to_Embeddings.ipynb` | 70 min | Qué es un embedding (visto primero dentro de la red neuronal de la Sesión 9), bolsa de palabras vs. vectores densos, las cuatro métricas de distancia implementadas y comparadas, PCA y K-means sobre texto, y la limitación del idioma. |
| 2 | `05 Embeddings/05 Token_vs_Sentence_Embeddings.ipynb` | 60 min | Tokenización en subpalabras, demostración de que los embeddings de BERT son contextuales, *mean pooling* con máscara de atención, y evaluación cuantitativa BERT vs. SBERT contra juicios humanos (STS-Benchmark). |
| 3 | `05 Embeddings/06_Using_Embeddings_in_RAG_Inference.ipynb` | 50 min | Índice vectorial y búsqueda top-$k$ sobre un corpus del propio curso, recuperación asimétrica con dual encoder (DPR), el modo de falla de la recuperación fuera de corpus y su mitigación con umbral, y armado del *prompt* de RAG. |

Los tres cierran con una sección **"Para pensar"** con preguntas ancladas al resultado concreto que
produjo el notebook. El notebook 1 incluye además un ejercicio guiado ("Tu turno") para hacerse en
clase.

## Plan de la sesión (210 minutos)

| Tiempo | Bloque | Contenido |
|---|---|---|
| 0:00 – 0:20 | Encuadre | Repaso del hilo del módulo: de la bolsa de palabras (Sesión 8) al significado como vector. Lectura de las notas: sección de embeddings y subsección de distancias. |
| 0:20 – 1:30 | Notebook 04 | Secciones 1 a 5. El "Tu turno" (sección 6) se deja como trabajo en casa si el tiempo aprieta. |
| 1:30 – 1:45 | **Receso** | Buen momento para que quienes no lo hayan hecho corran la descarga de `bert-base-uncased`. |
| 1:45 – 2:45 | Notebook 05 | Completo. El clímax es la comparación BERT vs. SBERT contra el estándar humano. |
| 2:45 – 3:35 | Notebook 06 | Completo. Si la red no aguanta la descarga de DPR, se corre con `EJECUTAR_DPR = False` y se discute la salida ya conocida. |
| 3:35 – 3:50 | Cierre | Enlace explícito con `04 Modelos de IA Generativa`: el *prompt* que armamos al final del notebook 06 es exactamente la entrada del siguiente bloque. |

**Si hay que recortar:** el notebook 06 es el que menos se puede sacrificar (es el puente al
siguiente bloque). Lo recortable, en este orden, es la sección 6 del notebook 04 ("Tu turno", que
funciona bien como tarea), la sección 6 del notebook 05 (el experimento con `[CLS]`) y la sección
3.1 del notebook 06 (DPR).

## Uso en Google Colab

**Los tres notebooks funcionan en Colab sin modificarlos.** La primera celda de código de cada uno
detecta lo que falta y lo instala sola (en Colab, típicamente `sentence-transformers`, que no viene
preinstalado; `transformers`, `torch`, `scikit-learn`, `seaborn`, `scipy` y `pandas` sí vienen).

Consideraciones prácticas:

| Punto | Qué esperar en Colab |
|---|---|
| Instalación | La celda de dependencias tarda ~1 minuto la primera vez. No hace falta reiniciar el entorno de ejecución. |
| Descarga de modelos | Se bajan de Hugging Face en cada sesión nueva de Colab, porque la caché **no** se conserva al cerrar. Son ~510 MB (o ~1.4 GB si se corre DPR). En la red de Colab tarda poco, pero hay que contarlo cada vez. |
| GPU | No hace falta. Todo corre en CPU en tiempos razonables; el notebook 05 es el más pesado (~10 s de cómputo con BERT). |
| Datos del notebook 05 | Si abres el notebook **suelto**, sin el resto de la carpeta, no encontrará `stsbenchmark_muestra.csv` y bajará automáticamente el conjunto completo con `datasets` (probado). No se rompe nada. |
| Notebook 06, sección DPR | Los ~846 MB se bajan rápido en Colab, pero siguen tardando unos minutos. `EJECUTAR_DPR = False` la salta. |
| `USE_TF` | En Colab TensorFlow funciona bien, así que la línea no cambia nada ahí (solo acelera un poco el import). Se deja porque es indispensable en máquinas locales; ver abajo. |

**La forma recomendada de llevarlo a clase** es subir la carpeta completa a Google Drive y montarla,
para tener los datos al lado del notebook:

```python
from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/<ruta a la carpeta>/05 Embeddings"
```

## Preparación previa (importante)

### Paquetes (solo para uso local; en Colab lo hace el notebook solo)

```bash
pip install sentence-transformers transformers torch scikit-learn pandas seaborn matplotlib scipy
pip install datasets     # opcional: el notebook 05 trae una copia local de los datos
```

### Descarga previa de los modelos

Los modelos se bajan de Hugging Face la primera vez que se usan y quedan en caché. **Conviene
correr esto antes de la sesión, no durante**: veinte personas descargando al mismo tiempo en la red
del aula es la forma más común de perder media hora de clase.

```python
import os
os.environ["USE_TF"] = "0"
from sentence_transformers import SentenceTransformer
from transformers import (BertModel, BertTokenizer, AutoTokenizer,
                          DPRContextEncoder, DPRQuestionEncoder)

SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")          #  ~87 MB  (notebooks 04, 05, 06)
BertTokenizer.from_pretrained("bert-base-uncased")                      # ~420 MB  (notebook 05)
BertModel.from_pretrained("bert-base-uncased")
AutoTokenizer.from_pretrained("facebook/dpr-ctx_encoder-multiset-base") # ~846 MB los dos (notebook 06, opcional)
DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-multiset-base")
AutoTokenizer.from_pretrained("facebook/dpr-question_encoder-multiset-base")
DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-multiset-base")
```

Total aproximado: **1.4 GB**. Sin los modelos DPR (sección 3.1 del notebook 06, que puede saltarse
con `EJECUTAR_DPR = False`), son ~510 MB.

### Advertencia técnica: `USE_TF`

Los tres notebooks empiezan con:

```python
import os
os.environ["USE_TF"] = "0"
```

**antes** de importar `transformers` o `sentence_transformers`. Estas librerías buscan TensorFlow
al importarse, y en equipos con procesadores sin instrucciones AVX o con instalaciones incompletas
de TensorFlow, esa búsqueda **tumba el kernel de Jupyter sin mensaje de error legible**. Se
verificó que ocurre en el entorno de este repositorio. La línea es inofensiva donde el problema no
existe, así que se dejó en los tres notebooks. Si un estudiante reporta que "el kernel se muere en
la primera celda", ésta es la causa más probable.

### Datos incluidos

`05 Embeddings/stsbenchmark_muestra.csv` (16 KB) — 200 pares del conjunto de prueba de
STS-Benchmark con su calificación humana de similitud (0 a 5). El notebook 05 intenta primero
descargar el conjunto completo con `datasets` y **usa esta copia local automáticamente** si la
descarga falla o si el paquete no está instalado.

## Nota sobre el idioma de los modelos

Los ejemplos están en inglés a propósito: `all-MiniLM-L6-v2` y `bert-base-uncased` fueron
entrenados solo con texto en inglés. Esto no es un descuido sino **material de la clase**: el
notebook 04 (sección 5) mide el fracaso del modelo en español, y el notebook 05 (sección 1) muestra
la causa en el tokenizador. Para un proyecto real con datos en español hay que cambiar a un modelo
multilingüe (`paraphrase-multilingual-MiniLM-L12-v2` y compañía, ~470 MB); el resto del código no
cambia. Los notebooks señalan en qué línea exacta se hace ese cambio.

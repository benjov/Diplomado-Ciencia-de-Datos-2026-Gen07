# 01 Modelos de regresión lineal

**Sesión del módulo:** Sesión 1 (viernes, esperanza condicional/causalidad/DAGs) y Sesión 2
(sábado, regresión lineal — MCO, bondad de ajuste).
**Notas relacionadas:** `main.tex`, sección "El concepto de esperanza condicional y Causalidad" y
sección de regresión lineal y shrinkage (ridge/lasso).

## Objetivo de la unidad

Distinguir correlación de causalidad usando DAGs (Sesión 1), y luego construir e interpretar
modelos de regresión lineal simple y múltiple, evaluar su bondad de ajuste, y ver cómo la
regularización (ridge/lasso) cambia el problema cuando hay colinealidad (Sesión 2).

## Contenido

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `00_Causalidad_DAGs` (`.Rmd`, R) | Acompaña la Sesión 1: DAGs dibujados con `dagitty` (confusor observado/no observado, variable instrumental, el ejemplo de educación con background no observable) y simulaciones donde se conoce el efecto causal verdadero, para comparar contra lo que estima cada modelo. Incluye también el ejemplo de sesgo de selección/colisionador de Cunningham (2021, talento vs. belleza). | Sí (sección "Para pensar") |
| `01_Ejemplo_Datos_Publicidad` (`.Rmd`, R) | Regresión lineal múltiple con datos de publicidad en medios: ajuste, diagnóstico, interpretación de coeficientes. | No |
| `02_Ejemplo_Datos_Inmuebles24` (`.ipynb`) | Regresión con datos de venta de inmuebles en CDMX: limpieza (ciudades inconsistentes, anuncios duplicados, columnas sin cobertura suficiente, outliers de precio por m²), exploración visual, y comparación de OLS vs. Ridge vs. Lasso con validación cruzada, incluyendo el caso con polinomios donde Lasso sí elimina variables. **Es el ejemplo central del curso para la técnica de LASSO.** Antes coexistía con un `.Rmd` que solo hacía OLS (sin Ridge/Lasso) — se retiró por redundante y para no diluir el foco del ejemplo. | Sí (sección "Para pensar") |
| `03_Ejemplo_Conexión_ServicioWeb` (`.Rmd`, R) | No es modelado: muestra cómo consultar el servicio web del CENACE para descargar Precios Marginales Locales (PML) de electricidad. Es el paso de obtención de datos que alimenta `04_Generando_Datos_PML` y, más adelante, el clustering de series de tiempo de la Sesión 4. | No |
| `04_Generando_Datos_PML` (`.Rmd`, R) | Prepara/genera los archivos `Datos_PML.csv` / `Datos_PML_Wide.csv` a partir de la consulta anterior. Solo genera los datos, no los analiza. | No |

## Nota pedagógica

`03_Ejemplo_Conexión_ServicioWeb` y `04_Generando_Datos_PML` no son ejemplos de regresión en sí
— son la infraestructura de datos que se usa después en clustering de series de tiempo (Sesión
4). Si el tiempo de la Sesión 2 es limitado, priorizar `01_Ejemplo_Datos_Publicidad` y
`02_Ejemplo_Datos_Inmuebles24`, que son los que corresponden directamente al tema de la sesión.

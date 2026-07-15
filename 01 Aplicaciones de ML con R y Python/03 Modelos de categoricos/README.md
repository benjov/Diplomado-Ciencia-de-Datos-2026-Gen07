# 03 Modelos de categóricos

**Sesiones del módulo:** Sesión 5 (viernes) — Modelos categóricos (Logit); Sesión 6 (sábado) —
Logit ordinal + app.
**Prerrequisito:** Sesión 4 (clustering de series de tiempo).
**Notas relacionadas:** `main.tex`, capítulo de modelos de respuesta binaria/multinomial/ordinal
(incluye la derivación de la matriz de información esperada para logit/probit).

## Objetivo de la unidad

Modelar variables de respuesta categórica (binaria y ordinal) con Logit, interpretar
coeficientes vía efectos marginales, y ver una aplicación interactiva del modelo estimado.

## Contenido — Sesión 5 (Logit binario)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `09_Ejemplo_Logit_Delitos` | Logit binario sobre datos de víctimas en carpetas de investigación de la FGJ CDMX (robo a transeúnte con/sin violencia). | Sí (varios) |

## Contenido — Sesión 6 (Logit ordinal + app)

| Carpeta | Qué hace | Tiene ejercicios/reflexión |
|---|---|---|
| `10_Ejemplo_Logit_Ordenado/10_Estimacion_Logit_2024.01.31.Rmd` | Logit binario en R sobre datos SEL, como paso previo al ordinal. | No |
| `10_Ejemplo_Logit_Ordenado/10_Estimacion_OrdinalLogit_2024.01.31.Rmd` | Logit ordinal en R sobre los mismos datos SEL. | No |
| `11_App/App_AB` | App Shiny (`SimulApp.rmd`) que simula predicciones usando los modelos `.rds` entrenados en `10_Ejemplo_Logit_Ordenado`. | N/A (es una app) |

## Nota de higiene menor

En ambos `.Rmd` de `10_Ejemplo_Logit_Ordenado` hay una comilla de más, comentada, en
`install.packages("car"")` — inocuo mientras esté comentado, pero se debe corregir si algún
estudiante la descomenta.

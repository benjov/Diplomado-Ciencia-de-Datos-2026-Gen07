# 12 — Tu página personal con GitHub Pages

**Sesión 12 · Bloque 2 de 2 · Duración estimada: 70 minutos**

**Al terminar vas a tener una página web pública, con tu nombre, en una dirección del tipo
`https://tuusuario.github.io`**, donde vas a enlazar la aplicación que desplegaste en la sesión 11
y tus proyectos del diplomado.

No es un ejercicio decorativo. Cuando alguien quiere saber qué sabes hacer, un enlace a algo que
funciona vale más que una lista de temas en un currículum.

> **Todo se hace desde el navegador.** No hace falta instalar nada, ni usar VS Code, ni escribir un
> solo comando de Git. Si acabas de montar tu entorno local en el bloque anterior, perfecto — pero
> este bloque **no depende de él**, así que nadie se queda fuera por un problema de instalación.

## Por qué GitHub Pages y no Streamlit

Ya desplegaste una app en Streamlit. ¿Por qué otra herramienta? Porque hacen cosas distintas:

| | GitHub Pages | Streamlit Community Cloud |
|---|---|---|
| Qué sirve | Archivos estáticos (HTML, CSS, imágenes) | Una aplicación de Python corriendo |
| Velocidad | Instantánea, no se duerme | Se suspende tras 12 h sin visitas |
| Puede ejecutar Python | No | Sí |
| Buena para | Portafolio, documentación, sitio personal | Herramientas interactivas, demos con modelos |

Una página estática no puede correr tu chatbot; una app de Streamlit es un mal portafolio. Se
complementan: la página es la puerta de entrada y desde ahí enlazas la app.

## Material de apoyo

Este bloque sigue la misma lógica del taller **[De cero a online](https://github.com/benjov/github-pages-workshop)**,
donde hay material para repasar a tu ritmo:

| Material | Para qué |
|---|---|
| [Guía paso a paso ilustrada](https://benjov.github.io/github-pages-workshop/guia/) | Repetir el procedimiento en casa, con capturas de cada pantalla |
| [Demo de portafolio](https://benjov.github.io/github-pages-workshop/demo-egresado/) | Ver a dónde se puede llegar: un portafolio con proyectos desarrollados |

La plantilla que usamos aquí (`plantilla/index.html`, en esta carpeta) está pensada para el cierre
de este módulo: su primera tarjeta es tu app de RAG.

---

## Paso 1 — Crear el repositorio (el nombre es el truco)

GitHub tiene una regla especial: si nombras un repositorio **exactamente**
`TU_USUARIO.github.io`, su contenido se publica en `https://TU_USUARIO.github.io`, sin
configuración extra.

1. Entra a [github.com/new](https://github.com/new).
2. En **Repository name** escribe `TU_USUARIO.github.io`, con tu usuario real. Si tu usuario es
   `benjov`, el repositorio se llama `benjov.github.io`.
3. Marca **Public**. GitHub Pages gratuito solo publica repositorios públicos.
4. Deja lo demás como está y haz clic en **Create repository**.

> **El error más común de este paso** es que el nombre del repositorio no coincida con el del
> usuario. Tiene que ser idéntico, respetando mayúsculas: si tu usuario es `MariaGarcia`, el
> repositorio es `MariaGarcia.github.io`.

---

## Paso 2 — Crear el archivo `index.html` desde el navegador

Una página web es un archivo de texto. Vamos a crearlo dentro de GitHub, sin descargar nada.

1. En tu repositorio recién creado, haz clic en **Add file → Create new file**.
2. En el campo del nombre escribe exactamente **`index.html`**, en minúsculas y sin espacios. Es
   el nombre que los servidores web buscan por omisión; con cualquier otro, la página no aparece.
3. Abre `plantilla/index.html` de esta carpeta, **selecciona todo el contenido y cópialo**.
   (En GitHub, el botón para copiar el archivo completo está arriba a la derecha del código.)
4. Pégalo en el área de edición grande.
5. Baja hasta el final y haz clic en el botón verde **Commit changes**.

Con eso ya tienes una página publicada. Espera **uno a tres minutos** y entra a
`https://TU_USUARIO.github.io`: debe aparecer la plantilla, todavía con los textos de ejemplo.

> Puedes ver el progreso de la publicación en la pestaña **Actions** de tu repositorio: aparece una
> palomita verde cuando termina.

---

## Paso 3 — Personalizar la plantilla

La plantilla tiene comentarios **`<!-- CAMBIA ESTO: ... -->`** en cada punto que debes editar. Para
editar desde el navegador: abre `index.html` en tu repositorio y haz clic en el **ícono del lápiz
(✏️)**, arriba a la derecha.

Los cambios mínimos para que la página sea tuya:

| # | Qué cambias | Dónde |
|---|---|---|
| 1 | El **título de la pestaña** | `<title>` |
| 2 | Tu **inicial** en el avatar | `data-inicial="T"` |
| 3 | Tu **nombre** | `<h1>` |
| 4 | Tu **título profesional** | `<p class="rol">` — por ejemplo "Socióloga y analista de datos" |
| 5 | Tu **biografía** | `<p class="bio">` — dos o tres oraciones concretas |
| 6 | Tus **enlaces** de correo, GitHub y LinkedIn | `<div class="enlaces">` |
| 7 | La **URL de tu app de Streamlit** | primera tarjeta de Proyectos |

Cuando termines, baja y haz clic en **Commit changes** otra vez. Cada *commit* vuelve a publicar la
página sola; en un minuto se ve el cambio.

Dos notas sobre la plantilla:

- **No necesitas subir una foto.** El avatar es un círculo con tu inicial. Si prefieres una foto,
  súbela con **Add file → Upload files** y sigue la instrucción del comentario en esa misma línea.
- **Se adapta a celulares y respeta el modo oscuro** del visitante. Es un solo archivo, sin
  librerías externas: no hay nada que se pueda romper por una dependencia.

### Sobre qué escribir en las tarjetas

Una buena descripción de proyecto menciona **el resultado**, no solo la técnica: *"identifiqué tres
perfiles de consumo que explican el 60 % de la variación"* pesa mucho más que *"apliqué K-means"*.
Si no tienes tres proyectos, borra las tarjetas que sobren — una página corta y honesta se ve mejor
que una rellena con huecos.

---

## Paso 4 — Enlazar tus dos mundos

Cierra el círculo de las dos sesiones:

1. En tu **página personal**, la primera tarjeta ya enlaza a tu **app de Streamlit** (paso 3).
2. En tu **app de Streamlit**, agrega tu nombre y un enlace de regreso. También desde el navegador:
   entra a tu repositorio de la app en GitHub, abre `streamlit_app.py`, dale al lápiz, busca la
   línea del `st.caption(...)` bajo el título y agrega:

   ```python
   st.caption("Hecho por [Tu Nombre](https://TU_USUARIO.github.io)")
   ```

   **Commit changes**, y Streamlit Community Cloud vuelve a desplegar la app solo.

Ahora cualquiera que llegue a tu página puede probar tu asistente, y cualquiera que use tu
asistente sabe quién lo hizo.

---

## Ideas para después

- **Escribe una entrada sobre uno de tus proyectos.** Explicar qué hiciste y por qué es la mejor
  forma de demostrar que lo entendiste. Crea un archivo `proyecto.html` (mismo procedimiento del
  paso 2) y enlázalo desde una tarjeta.
- **Publica tus notebooks.** GitHub los muestra ya renderizados: basta enlazar al archivo `.ipynb`
  dentro de tu repositorio.
- **Usa un dominio propio.** Si compras `tunombre.com`, GitHub Pages lo acepta gratis desde
  *Settings → Pages → Custom domain*.
- **Edita desde tu computadora.** Si montaste el entorno del bloque anterior, puedes clonar el
  repositorio con `git clone` y editarlo en VS Code. Es más cómodo para cambios grandes, pero el
  resultado es exactamente el mismo: no te lo pierdes por haber trabajado en el navegador.

## Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| 404 después de varios minutos | El repositorio no se llama exactamente `TU_USUARIO.github.io`, o es privado. Revísalo en *Settings*. |
| 404 y el nombre sí está bien | Ve a *Settings → Pages* y revisa que en **Source** diga *Deploy from a branch*, con la rama `main` y la carpeta `/ (root)`. |
| La página aparece en blanco | El archivo no se llama `index.html` (revisa mayúsculas y espacios), o está dentro de una carpeta en vez de la raíz. |
| La página sale sin estilos | El navegador guardó la versión anterior. Recarga forzando: `Ctrl+Shift+R` (Mac: `Cmd+Shift+R`). |
| Cambié el archivo y no se ve | ¿Le diste **Commit changes** al final de la página? Editar en el navegador no guarda solo. |
| Se me rompió la página al editar | Abre el historial del archivo (*History*), entra al *commit* anterior y usa el botón de los tres puntos para restaurar esa versión. |

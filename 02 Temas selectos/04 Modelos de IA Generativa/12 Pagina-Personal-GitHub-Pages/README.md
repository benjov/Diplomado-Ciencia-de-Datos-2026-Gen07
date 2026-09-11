# 12 — Tu página personal con GitHub Pages

**Sesión 12 · Bloque 2 de 2 · Duración estimada: 70 minutos**

**Al terminar vas a tener una página web pública, con tu nombre, en una dirección del tipo
`https://tuusuario.github.io`**, donde vas a enlazar la aplicación que desplegaste en la sesión 11
y tus proyectos del diplomado.

No es un ejercicio decorativo. Cuando alguien quiere saber qué sabes hacer, un enlace a algo que
funciona vale más que una lista de temas en un currículum. Y como vamos a editarla con VS Code y
publicarla con Git, es también la primera vez que usas el entorno que acabas de instalar para algo
real.

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

---

## Paso 1 — Crear el repositorio (el nombre importa)

GitHub tiene una regla especial: si nombras un repositorio **exactamente**
`TU_USUARIO.github.io`, su contenido se publica en `https://TU_USUARIO.github.io`, sin
configuración extra.

1. Entra a [github.com/new](https://github.com/new).
2. En **Repository name** escribe `TU_USUARIO.github.io`, con tu usuario real y todo en
   minúsculas. Si tu usuario es `benjov`, el repositorio se llama `benjov.github.io`.
3. Marca **Public** (Pages gratuito requiere repositorio público).
4. Marca **Add a README file**.
5. *Create repository*.

> **El error más común de este paso** es escribir el nombre del repositorio distinto al del
> usuario. Si no coinciden exactamente, la publicación automática no ocurre.

---

## Paso 2 — Clonarlo con VS Code

Abre la terminal (dentro de VS Code: menú *Terminal → New Terminal*):

```bash
git clone https://github.com/TU_USUARIO/TU_USUARIO.github.io.git
cd TU_USUARIO.github.io
code .
```

---

## Paso 3 — Copiar y personalizar la plantilla

Copia el archivo `plantilla/index.html` de esta carpeta a la raíz de tu repositorio recién
clonado. **Tiene que llamarse `index.html`**: es el nombre que los servidores web buscan por
omisión.

Ábrelo en VS Code y cambia, en este orden:

1. **`<title>`** (línea 7) — aparece en la pestaña del navegador y en los resultados de búsqueda.
2. **Tu nombre** en el `<h1>`.
3. **La biografía** — dos o tres oraciones concretas. "Analizo datos de movilidad urbana en la
   Zona Metropolitana" dice mucho más que "me apasiona la ciencia de datos".
4. **Los enlaces de contacto** — correo, GitHub, LinkedIn.
5. **La primera tarjeta de proyecto** — pon ahí la URL real de tu app de Streamlit de la sesión 11.
6. **Las otras dos tarjetas** — tus trabajos del diplomado. Puedes enlazar directamente a un
   notebook dentro de tu repositorio de GitHub.

La plantilla ya se adapta a celulares y cambia sola a modo oscuro si el visitante lo tiene
activado. No necesita ninguna librería externa: es un solo archivo.

> **Sobre la foto.** La plantilla busca una imagen llamada `foto.jpg` junto al `index.html`. Si la
> subes, aparece; si no, la línea se oculta sola y no se rompe nada.

### Verlo antes de publicar

En VS Code, clic derecho sobre `index.html` → *Open with Live Server* (si instalaste esa
extensión), o simplemente abre el archivo con doble clic en tu navegador. Es un archivo estático:
lo que ves en local es exactamente lo que se va a publicar.

---

## Paso 4 — Publicar

```bash
git add .
git commit -m "Mi página personal"
git push
```

Espera **entre uno y tres minutos** y entra a `https://TU_USUARIO.github.io`.

Puedes ver el progreso en la pestaña **Actions** de tu repositorio en GitHub: ahí aparece el
proceso de publicación con una palomita verde cuando termina.

> **Si después de cinco minutos ves un 404:** ve a *Settings → Pages* en tu repositorio y revisa
> que en **Source** diga *Deploy from a branch*, y que la rama sea `main` con carpeta `/ (root)`.

A partir de aquí, cada `git push` actualiza la página automáticamente.

---

## Paso 5 — Enlazar tus dos mundos

Cierra el círculo de las dos sesiones:

1. En tu **página personal**, la primera tarjeta enlaza a tu **app de Streamlit**.
2. En tu **app de Streamlit**, agrega tu nombre y un enlace a tu página personal. Abre
   `streamlit_app.py`, busca la línea del `st.caption(...)` bajo el título y agrégale algo como:

   ```python
   st.caption("Hecho por [Tu Nombre](https://TU_USUARIO.github.io)")
   ```

   Haz `git push` en ese repositorio y Streamlit vuelve a desplegar solo.

---

## Ideas para después

- **Escribe una entrada sobre uno de tus proyectos.** Explicar qué hiciste y por qué es la mejor
  forma de demostrar que lo entendiste. Agrega un `proyecto.html` y enlázalo desde una tarjeta.
- **Usa un dominio propio.** Si compras `tunombre.com`, GitHub Pages lo acepta gratis desde
  *Settings → Pages → Custom domain*.
- **Publica tus notebooks.** GitHub los muestra ya renderizados: basta enlazar al archivo `.ipynb`
  dentro de tu repositorio.

## Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| 404 después de varios minutos | El repositorio no se llama exactamente `TU_USUARIO.github.io`, o es privado. |
| La página sale sin estilos | El navegador guardó la versión anterior. Recarga forzando: `Ctrl+Shift+R` (Mac: `Cmd+Shift+R`). |
| `git push` pide usuario y contraseña y las rechaza | GitHub ya no acepta contraseñas: hay que usar un *personal access token* o configurar SSH. Está explicado en el manual de `00 Notas`. |
| Los cambios no se ven | ¿Hiciste `commit` **y** `push`? Revisa con `git status` que no quede nada pendiente. |
| Se publicó tu archivo `.env` | Revoca la llave de inmediato en console.groq.com y genera otra. Borrar el archivo no basta: queda en el historial. |

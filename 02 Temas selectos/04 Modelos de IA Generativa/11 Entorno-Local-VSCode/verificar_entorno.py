"""Verifica que tu entorno local quedó bien configurado.

Uso:  python verificar_entorno.py

No instala nada ni modifica nada: solo revisa y te dice qué falta.
"""

import importlib.util
import os
import platform
import sys
from pathlib import Path

VERDE, ROJO, AMARILLO, GRIS, FIN = "\033[92m", "\033[91m", "\033[93m", "\033[90m", "\033[0m"
if platform.system() == "Windows" and not os.environ.get("WT_SESSION"):
    VERDE = ROJO = AMARILLO = GRIS = FIN = ""     # consolas viejas de Windows no pintan color

PAQUETES = [
    ("agno", "agno", True),
    ("groq", "groq", True),
    ("python-dotenv", "dotenv", True),
    ("pandas", "pandas", False),
    ("scikit-learn", "sklearn", False),
    ("streamlit", "streamlit", False),
]

resultados = []


def revisar(nombre, ok, detalle="", critico=True):
    marca = f"{VERDE}  OK  {FIN}" if ok else (f"{ROJO} FALTA{FIN}" if critico else f"{AMARILLO} AVISO{FIN}")
    # La pista solo estorba cuando la revisión ya pasó.
    print(f"[{marca}] {nombre}" + (f"{GRIS}  — {detalle}{FIN}" if detalle and not ok else ""))
    resultados.append((nombre, ok, critico))


print("\n" + "=" * 62)
print("  Verificación del entorno — Módulo V, Diplomado de Ciencia de Datos")
print("=" * 62 + "\n")

# 1. Versión de Python -------------------------------------------------------
mayor, menor = sys.version_info[:2]
revisar(
    f"Python 3.12 o superior (tienes {mayor}.{menor})",
    (mayor, menor) >= (3, 12),
    "Agno requiere 3.12+. Instala una versión nueva desde python.org.",
)

# 2. Entorno virtual activo --------------------------------------------------
en_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
revisar(
    "Entorno virtual activado",
    en_venv,
    f"Intérprete: {sys.executable}"
    if en_venv
    else "No estás dentro de un venv. Actívalo antes de instalar paquetes.",
)

# 3. Paquetes ----------------------------------------------------------------
for nombre, modulo, critico in PAQUETES:
    revisar(f"Paquete '{nombre}'", importlib.util.find_spec(modulo) is not None,
            "pip install " + nombre, critico=critico)

# 4. Archivo .env con la llave ----------------------------------------------
ruta_env = Path(".env")
if ruta_env.exists():
    contenido = ruta_env.read_text(encoding="utf-8")
    tiene_llave = "GROQ_API_KEY" in contenido
    valor = ""
    for linea in contenido.splitlines():
        if linea.strip().startswith("GROQ_API_KEY"):
            valor = linea.split("=", 1)[-1].strip().strip('"').strip("'")
    revisar("Archivo .env con GROQ_API_KEY",
            tiene_llave and valor.startswith("gsk_"),
            "La llave debe empezar con 'gsk_'." if tiene_llave else "Falta la línea GROQ_API_KEY=...")
else:
    revisar("Archivo .env con GROQ_API_KEY", False,
            "Crea un archivo .env en esta carpeta con: GROQ_API_KEY=gsk_tu_llave")

# 5. El .env NO debe subirse a git ------------------------------------------
ruta_gitignore = Path(".gitignore")
protegido = ruta_gitignore.exists() and ".env" in ruta_gitignore.read_text(encoding="utf-8")
revisar("'.env' listado en .gitignore", protegido,
        "Agrega una línea '.env' a tu .gitignore ANTES de hacer commit. "
        "Una llave publicada en GitHub se considera comprometida.")

# 6. Git disponible ----------------------------------------------------------
import shutil
revisar("Git instalado", shutil.which("git") is not None,
        "Descárgalo de git-scm.com (ver el manual en '00 Notas').")

# Resumen --------------------------------------------------------------------
fallas = [n for n, ok, critico in resultados if not ok and critico]
avisos = [n for n, ok, critico in resultados if not ok and not critico]

print("\n" + "-" * 62)
if not fallas:
    print(f"{VERDE}Todo listo.{FIN} Tu entorno está preparado para las sesiones de agentes.")
    if avisos:
        print(f"{AMARILLO}Opcionales pendientes:{FIN} " + ", ".join(avisos))
else:
    print(f"{ROJO}Faltan {len(fallas)} cosa(s):{FIN}")
    for f in fallas:
        print(f"   - {f}")
    print("\nRevisa el README de esta carpeta en el paso correspondiente.")
print("-" * 62 + "\n")

sys.exit(1 if fallas else 0)

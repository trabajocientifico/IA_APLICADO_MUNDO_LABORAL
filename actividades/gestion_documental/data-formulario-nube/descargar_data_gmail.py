"""
Descarga automatica de las respuestas de un Google Form
desde la hoja de calculo (Google Sheets) que el formulario alimenta.

No necesita API key ni credenciales: usa el endpoint publico de exportacion
de Google Sheets. Lo unico que hace falta es que la hoja este compartida
como "Cualquier persona con el enlace" (al menos con permiso de Lector).

Requisitos:
    pip install requests

Antes de correr este script:
    1. Abre la hoja de respuestas del formulario en Google Sheets.
    2. Boton "Compartir" -> Acceso general -> "Cualquier persona con el enlace"
       -> rol "Lector". Copia el enlace.
    3. Pega ese enlace en ENLACE_SHEET abajo.
"""

import os
import re
from datetime import datetime

import requests

# ============ CONFIGURACION (edita estos valores) ============

# Pega aqui el enlace de la hoja de calculo de respuestas
ENLACE_SHEET = "https://docs.google.com/spreadsheets/d/1jCNd7s2CIVlPJk9HojriOl0kr7O5wS1kccG5Db9kZYY/edit?usp=sharing"

# Formato de descarga: "xlsx" (todas las hojas) o "csv" (solo una hoja)
FORMATO = "xlsx"

# Carpeta local donde quieres guardar el archivo descargado.
CARPETA_DESTINO = os.getcwd()

# Nombre con el que se guardara localmente (sin extension:
# se agrega automaticamente segun FORMATO)
NOMBRE_ARCHIVO_LOCAL = "respuestas_formulario"

# Si quieres que cada descarga quede con fecha y hora en el nombre,
# en vez de sobrescribir la anterior, pon esto en True.
AGREGAR_FECHA_AL_NOMBRE = False

# ================================================================


def extraer_id(enlace):
    """
    Extrae el ID del documento de cualquier URL de Google Sheets.
    Acepta tanto el enlace completo (.../spreadsheets/d/<ID>/edit?usp=sharing)
    como el ID pelado.
    """
    coincidencia = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", enlace)
    if coincidencia:
        return coincidencia.group(1)

    # Puede que el usuario haya pegado solo el ID
    if re.fullmatch(r"[a-zA-Z0-9-_]{20,}", enlace.strip()):
        return enlace.strip()

    raise ValueError(
        "No se pudo extraer el ID de la hoja desde ENLACE_SHEET. "
        "Revisa que sea un enlace de docs.google.com/spreadsheets/d/..."
    )


def extraer_gid(enlace):
    """
    Extrae el gid (identificador de la pestana concreta) si viene en el enlace.
    Solo se usa para el formato csv, que exporta una sola hoja.
    Devuelve None si no hay gid en la URL.
    """
    coincidencia = re.search(r"[#?&]gid=([0-9]+)", enlace)
    return coincidencia.group(1) if coincidencia else None


def construir_url_exportacion(enlace, formato):
    """
    Construye la URL de exportacion directa de Google Sheets.

    Google expone /export?format=... sin necesidad de autenticacion
    siempre que la hoja este compartida por enlace.
    """
    doc_id = extraer_id(enlace)
    url = f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format={formato}"

    # El csv solo puede contener una hoja: si el enlace apunta a una pestana
    # concreta, respetamos esa pestana.
    if formato == "csv":
        gid = extraer_gid(enlace)
        if gid:
            url += f"&gid={gid}"

    return url


def descargar_sheet():
    """Descarga la hoja de respuestas y la guarda localmente."""

    if FORMATO not in ("xlsx", "csv"):
        raise ValueError(f"FORMATO debe ser 'xlsx' o 'csv', no '{FORMATO}'")

    url = construir_url_exportacion(ENLACE_SHEET, FORMATO)
    respuesta = requests.get(url, allow_redirects=True, timeout=60)

    if respuesta.status_code != 200:
        raise Exception(
            f"Error al descargar la hoja. "
            f"Codigo: {respuesta.status_code}, Detalle: {respuesta.text[:300]}"
        )

    # Si la hoja no es publica, Google no devuelve un error HTTP: responde 200
    # con la pagina HTML de inicio de sesion. Hay que detectarlo a mano.
    tipo = respuesta.headers.get("content-type", "")
    if "text/html" in tipo:
        raise Exception(
            "Google devolvio una pagina web en lugar del archivo. "
            "Casi siempre significa que la hoja NO esta compartida publicamente. "
            "Abrela en Google Sheets -> Compartir -> Acceso general -> "
            "'Cualquier persona con el enlace' con rol 'Lector'."
        )

    # Verificacion del contenido segun el formato pedido
    if FORMATO == "xlsx" and not respuesta.content.startswith(b"PK"):
        raise Exception(
            "El contenido descargado no parece un archivo Excel valido. "
            "Revisa el enlace y los permisos de la hoja."
        )

    nombre = NOMBRE_ARCHIVO_LOCAL
    if AGREGAR_FECHA_AL_NOMBRE:
        nombre += datetime.now().strftime("_%Y%m%d_%H%M%S")
    nombre += f".{FORMATO}"

    os.makedirs(CARPETA_DESTINO, exist_ok=True)
    ruta_local = os.path.join(CARPETA_DESTINO, nombre)

    with open(ruta_local, "wb") as f:
        f.write(respuesta.content)

    return ruta_local, len(respuesta.content)


def main():
    print(f"[{datetime.now()}] Iniciando descarga...")
    try:
        ruta_guardada, tamano = descargar_sheet()
        print(
            f"[{datetime.now()}] Archivo descargado correctamente "
            f"({tamano} bytes) en: {ruta_guardada}"
        )
    except Exception as e:
        print(f"[{datetime.now()}] ERROR: {e}")


if __name__ == "__main__":
    main()

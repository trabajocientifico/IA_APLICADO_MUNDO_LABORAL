"""
Descarga automatica del Excel de resultados de Microsoft Forms
usando un enlace compartido de OneDrive personal (sin Azure AD).

Requisitos:
    pip install requests

Antes de correr este script:
    1. En OneDrive, comparte el archivo Excel y copia el enlace
       (ver instrucciones que te dieron junto con este script).
    2. Pega ese enlace en ENLACE_COMPARTIDO abajo.
"""

import requests
import os
from datetime import datetime
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

# ============ CONFIGURACION (edita estos valores) ============

# Pega aqui el enlace que copiaste al compartir el archivo en OneDrive
ENLACE_COMPARTIDO = "https://1drv.ms/x/c/CBBCFEA5258223FB/IQDL8fmMEyYITq81QTQGn41gAdv4hRcaoXEeqvtc-QTri-4?e=9gWLGe"

# Carpeta local donde quieres guardar el archivo descargado.
# os.getcwd() usa la carpeta desde donde se ejecuta el script (carpeta actual).
CARPETA_DESTINO = os.getcwd()

# Nombre con el que se guardara localmente
NOMBRE_ARCHIVO_LOCAL = "resultados_formulario.xlsx"

# ================================================================


def convertir_a_link_directo(enlace_compartido):
    """
    Convierte un enlace de compartir de OneDrive (1drv.ms o onedrive.live.com)
    en un enlace de descarga directa.

    Basta con agregar el parametro download=1 al propio enlace compartido:
    OneDrive responde con el archivo en lugar de la pagina del visor web.
    (La antigua API api.onedrive.com/v1.0/shares/... ya no permite acceso
    anonimo y devuelve 401 unauthenticated.)
    """
    partes = urlparse(enlace_compartido)
    query = dict(parse_qsl(partes.query))
    query["download"] = "1"
    return urlunparse(partes._replace(query=urlencode(query)))


def descargar_excel():
    """Descarga el archivo usando el enlace compartido y lo guarda localmente."""

    url_directa = convertir_a_link_directo(ENLACE_COMPARTIDO)

    respuesta = requests.get(url_directa, allow_redirects=True)

    if respuesta.status_code != 200:
        raise Exception(
            f"Error al descargar el archivo. "
            f"Codigo: {respuesta.status_code}, Detalle: {respuesta.text[:300]}"
        )

    # Verificacion basica: un .xlsx es un archivo ZIP, debe empezar con 'PK'
    if not respuesta.content.startswith(b"PK"):
        raise Exception(
            "El contenido descargado no parece ser un archivo Excel valido. "
            "Revisa que el enlace compartido sea correcto y siga activo."
        )

    os.makedirs(CARPETA_DESTINO, exist_ok=True)
    ruta_local = os.path.join(CARPETA_DESTINO, NOMBRE_ARCHIVO_LOCAL)

    with open(ruta_local, "wb") as f:
        f.write(respuesta.content)

    return ruta_local


def main():
    print(f"[{datetime.now()}] Iniciando descarga...")
    try:
        ruta_guardada = descargar_excel()
        print(f"[{datetime.now()}] Archivo descargado correctamente en: {ruta_guardada}")
    except Exception as e:
        print(f"[{datetime.now()}] ERROR: {e}")


if __name__ == "__main__":
    main()

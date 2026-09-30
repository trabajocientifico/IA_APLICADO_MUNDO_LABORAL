"""
Sirve el dashboard por HTTP y lo abre en el navegador.

Por que hace falta: el dashboard lee la hoja de respuestas en vivo desde
docs.google.com. Si abres el HTML con doble clic, el navegador lo carga con el
esquema file:// y el origen de la pagina pasa a ser "null"; en ese caso Google
NO devuelve las cabeceras CORS y el navegador bloquea la lectura. Servido por
HTTP (http://localhost) el origen es valido, Google responde con
Access-Control-Allow-Origin y la conexion en vivo funciona.

Uso:
    python servir_dashboard.py

Para detenerlo: Ctrl+C.
"""

import http.server
import os
import socket
import socketserver
import webbrowser

# ============ CONFIGURACION ============

ARCHIVO = "dashboard_formulario.html"

# Puerto inicial. Si esta ocupado, el script prueba los siguientes.
PUERTO = 8000

# Cuantos puertos probar antes de rendirse
INTENTOS = 20

# =======================================


class Handler(http.server.SimpleHTTPRequestHandler):
    """Servidor de archivos estaticos que no deja nada en cache.

    Sin esto el navegador puede quedarse con una version vieja del HTML
    mientras editas el dashboard.
    """

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, formato, *args):
        # Silencia el log por peticion: solo interesa el mensaje de arranque
        pass


def buscar_puerto_libre(inicial, intentos):
    """Devuelve el primer puerto libre a partir de 'inicial'."""
    for puerto in range(inicial, inicial + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", puerto)) != 0:
                return puerto
    raise RuntimeError(
        f"No se encontro un puerto libre entre {inicial} y {inicial + intentos - 1}."
    )


def main():
    # Sirve siempre la carpeta donde vive este script, no la carpeta actual
    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    if not os.path.exists(ARCHIVO):
        print(f"ERROR: no encuentro '{ARCHIVO}' en {carpeta}")
        return

    puerto = buscar_puerto_libre(PUERTO, INTENTOS)
    url = f"http://localhost:{puerto}/{ARCHIVO}"

    # allow_reuse_address evita el "Address already in use" al reiniciar rapido
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("127.0.0.1", puerto), Handler) as servidor:
        print(f"Sirviendo {carpeta}")
        print(f"Dashboard en: {url}")
        print("Ctrl+C para detener.")
        webbrowser.open(url)
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")


if __name__ == "__main__":
    main()

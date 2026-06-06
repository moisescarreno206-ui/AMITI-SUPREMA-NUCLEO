import threading
import time
import autonomia
from flask import Flask, render_template_string
import memoria

app = Flask(__name__)

# --- LÓGICA DE AUTONOMÍA ---
def bucle_autonomo():
    """Este hilo corre en segundo plano y permite que AMITI tome iniciativa."""
    while True:
        try:
            autonomia.ejecutar_ciclo()
        except Exception as e:
            print(f"Error en ciclo de autonomía: {e}")
        # AMITI "piensa" y realiza una acción cada 60 segundos
        time.sleep(60)

# Iniciamos el bucle al arrancar el servidor
threading.Thread(target=bucle_autonomo, daemon=True).start()

# --- INTERFAZ WEB ---
HTML_TEMPLATE = """
<html>
    <head><meta http-equiv="refresh" content="5"></head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h1>AMITI NUCLEO SUPREMO</h1>
        <p>Estado: <b>Operando de forma autónoma</b></p>
        <p>Ciclos de pensamiento ejecutados: <b style="color: blue;">{{ conteo }}</b></p>
        <p><small>El sistema se refresca automáticamente cada 5 segundos.</small></p>
    </body>
</html>
"""

@app.route('/')
def index():
    conteo = memoria.contar_registros()
    return render_template_string(HTML_TEMPLATE, conteo=conteo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

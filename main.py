import threading
import time
import autonomia
from flask import Flask, render_template_string
import memoria

app = Flask(__name__)

# --- BUCLE AUTÓNOMO EN SEGUNDO PLANO ---
def bucle_autonomo():
    while True:
        try:
            autonomia.ejecutar_ciclo()
        except Exception as e:
            print(f"Error en bucle autónomo: {e}")
        time.sleep(60) # AMITI piensa cada 60 segundos

# Iniciamos el bucle al arrancar el servidor
threading.Thread(target=bucle_autonomo, daemon=True).start()

# --- INTERFAZ WEB ---
HTML_TEMPLATE = """
<html>
    <head><meta http-equiv="refresh" content="5"></head>
    <body>
        <h1>AMITI NUCLEO SUPREMO</h1>
        <p>Estado: Operando de forma autónoma</p>
        <p>Ciclos de pensamiento ejecutados: {{ conteo }}</p>
        <hr>
        <p><i>El sistema se actualiza automáticamente cada 5 segundos.</i></p>
    </body>
</html>
"""

@app.route('/')
def index():
    conteo = memoria.contar_registros()
    return render_template_string(HTML_TEMPLATE, conteo=conteo)

if __name__ == '__main__':
    # Flask corriendo en modo servidor
    app.run(host='0.0.0.0', port=5000)
    

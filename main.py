import threading
import time
import autonomia
from flask import Flask, render_template_string
import memoria

app = Flask(__name__)

# Función que corre en segundo plano
def bucle_autonomo():
    while True:
        autonomia.ejecutar_ciclo()
        time.sleep(60) # Espera 60 segundos antes de volver a pensar

# Iniciar el hilo al arrancar
threading.Thread(target=bucle_autonomo, daemon=True).start()

@app.route('/')
def index():
    return "AMITI NUCLEO SUPREMO: Estado activo. Pensando en segundo plano..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

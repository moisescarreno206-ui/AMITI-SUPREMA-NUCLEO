import threading
import time
import autonomia
from flask import Flask, render_template_string
import memoria

app = Flask(__name__)

def bucle_autonomo():
    while True:
        try:
            autonomia.ejecutar_ciclo()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)

threading.Thread(target=bucle_autonomo, daemon=True).start()

@app.route('/')
def index():
    conteo = memoria.contar_registros()
    return render_template_string("<h1>AMITI NUCLEO SUPREMO</h1><p>Ciclos: {{ conteo }}</p>", conteo=conteo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

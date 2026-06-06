from flask import Flask, render_template_string
import autonomia
import memoria

app = Flask(__name__)

# Plantilla de página que se auto-refresca cada 2 segundos
HTML_TEMPLATE = """
<html>
    <head><meta http-equiv="refresh" content="2"></head>
    <body>
        <h1>AMITI NUCLEO SUPREMO</h1>
        <p>Estado: {{ estado }}</p>
        <p>Registros en memoria: {{ conteo }}</p>
    </body>
</html>
"""

@app.route('/')
def index():
    autonomia.ejecutar_ciclo()
    conteo = memoria.contar_registros()
    return render_template_string(HTML_TEMPLATE, estado="Operando con iniciativa", conteo=conteo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

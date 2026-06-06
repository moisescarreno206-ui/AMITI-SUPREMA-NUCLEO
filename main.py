from flask import Flask, request
import modulos.seguridad as seguridad
import modulos.autonomia as autonomia
import modulos.memoria as memoria

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    if request.method == 'HEAD':
        return ""
    
    autonomia.ejecutar_ciclo()
    msg_salida = "AMITI NUCLEO SUPREMO: Estado activo"
    
    if request.method == 'POST':
        # Verificamos seguridad
        if seguridad.verificar(request.form.get("llave")):
            comando = request.form.get("msg")
            msg_salida = f"EJECUTADO: {comando}"
            memoria.registrar(comando, msg_salida)
        else:
            msg_salida = "ERROR: Llave de seguridad inválida"
            
    return msg_salida

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

from flask import Flask, request, render_template_string
from modulos import seguridad, autonomia, memoria

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    if request.method == 'HEAD': return "", 200
    autonomia.ejecutar_ciclo()
    msg_salida = "AMITI NUCLEO SUPREMO: Esperando órdenes."
    if request.method == 'POST':
        if seguridad.verificar(request.form.get("llave")):
            comando = request.form.get("msg")
            msg_salida = f"EJECUTADO: {comando}"
            memoria.registrar(comando, msg_salida)
        else:
            msg_salida = "ACCESO DENEGADO."
    return render_template_string('''
        <body style="background:#000; color:#0f0; font-family:monospace; padding:20px;">
            <h2>AMITI NUCLEO SUPREMO</h2>
            <div style="border:1px solid #0f0; padding:15px;">
                <p>> Respuesta: {{ res }}</p>
                <p>> Registros: {{ count }}</p>
            </div>
            <form method="POST">
                <input name="llave" type="password" placeholder="LLAVE" required style="width:100%; margin-top:10px;">
                <input name="msg" placeholder="COMANDO..." required style="width:100%; margin-top:5px;">
                <button type="submit" style="width:100%; margin-top:5px;">EJECUTAR</button>
            </form>
        </body>
    ''', res=msg_salida, count=memoria.contar_registros())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
  

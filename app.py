
from flask import Flask, request, jsonify, render_template
import bd 


app = Flask(__name__)

@app.route('/')
def home():
    try:
        if consulta:
            return render_template("index.html", login = consulta)
    except NameError:
        return render_template('index.html',login_no = False)

@app.route('/Login')
def log():
    return render_template('login.html')

@app.route('/Login/C0N5UL7A', methods=['POST'])
def log_consulta():
    global consulta
    if request.method == 'POST':
        correo = request.form['correo']
        contra = request.form['contrasena']
        consulta = bd.login(correo,contra)
        if consulta == None:
            return render_template("login.html", error = False)
        elif consulta[0] == correo and consulta[1] == contra:
            return render_template("index.html",login = consulta)

@app.route('/Registrarse')
def reg():
    return render_template('registrarse.html')

@app.route('/Registrarse/C0N5UL7A', methods=['POST'])
def reg_consulta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contra = request.form['contrasena']
        verificar_correo = bd.verificar_correo_exis(correo)
        if verificar_correo == 0:
            consul = bd.Register(nombre,correo,contra)
            return render_template('registrarse.html', accion = consul)
        else:
            return render_template('registrarse.html', accion = False)
        
@app.route('/Registrar/Paquetes')
def reg_paquete():
    try:
        if consulta:
            get = bd.get_paquetes()
            return render_template('regis_paquete.html',login = consulta,datos = get)
    except NameError:
        return render_template("login.html") 

@app.route("/Registrar/Paquetes/C0N5UL7A", methods=['POST'])
def reg_paquete_consulta():
    if request.method == 'POST':
        n_r = request.form['n_r']
        n_d = request.form['n_d']
        d_r = request.form['d_r']
        d_d = request.form['d_d']
        c_r = request.form['c_r']
        c_d = request.form['c_d']
        e_r = request.form['e_r']
        e_d = request.form['e_d']
        ciudad_r = request.form['ciudad_r']
        ciudad_d = request.form['ciudad_d']
        descripcion = request.form['descripcion']
        query = bd.reg_paquetes(n_r, n_d, d_r, d_d, c_r, c_d, e_r, e_d, ciudad_r, ciudad_d, descripcion)
        if query == True:
            get = bd.get_paquetes()
            return render_template("regis_paquete.html", accion = query, login=consulta,datos = get)
        else:
            return render_template("regis_paquete.html", accion = False)
        
@app.route("/Registrar/Paquetes/<int:id>")
def reg_editar(id):
    global query_editar
    query_editar = bd.get_paquetes_editar(id)
    get = bd.get_paquetes()
    return render_template("regis_paquete2.html", edit = query_editar, login=consulta,datos = get)

@app.route("/Registrar/Paquetes/ED174R", methods=['POST'])
def reg_editar_consul():
    if request.method == 'POST':
        n_r = request.form['n_r']
        n_d = request.form['n_d']
        d_r = request.form['d_r']
        d_d = request.form['d_d']
        c_r = request.form['c_r']
        c_d = request.form['c_d']
        e_r = request.form['e_r']
        e_d = request.form['e_d']
        ciudad_r = request.form['ciudad_r']
        ciudad_d = request.form['ciudad_d']
        descripcion = request.form['descripcion']
        query = bd.reg_paquetes_editar(query_editar[0],n_r, n_d, d_r, d_d, c_r, c_d, e_r, e_d, ciudad_r, ciudad_d, descripcion)
        if query == True:
            get = bd.get_paquetes()
            return render_template("regis_paquete.html", accion = query, login=consulta,datos = get)
        else:
            return render_template("regis_paquete.html", accion = False)

@app.route("/Registrar/Paquetes/3L1M1N4R/<int:id>", methods=['POST'])
def reg_eliminar_paquetes(id):
    if request.method == "POST":
        query = bd.reg_paquetes_eliminar(id)
        get = bd.get_paquetes()
        if query == True:
            return render_template("regis_paquete.html", accion = "eliminado", login=consulta,datos = get)
        
@app.route("/Historial_Estados")
def historial_estado():
    try:
        if consulta:
            paquetes = bd.get_paquetes()
            usuarios = bd.get_usuarios()
            historial = bd.get_historial()
            return render_template('historial.html',login = consulta,estados = historial,usuarios=usuarios,datos = paquetes)
    except NameError:
        return render_template("login.html") 
    
@app.route("/Historial_Estados/C0N5UL7A", methods=['POST'])
def historial_consulta():
    if request.method == 'POST':
        id_paquete = request.form['id_paquete']
        estado = request.form['estado']
        lugar = request.form['lugar']
        query = bd.historial_reg(id_paquete,estado,lugar)
        if query == True:
            paquetes = bd.get_paquetes()
            usuarios = bd.get_usuarios()
            historial = bd.get_historial()
            return render_template('historial.html',login = consulta,estados = historial,usuarios=usuarios,datos = paquetes,accion = query)
        else:
            return render_template("regis_paquete.html", accion = False)
        
@app.route("/Rastrear/Paquete", methods=['POST'])
def rastrear():
    if request.method == 'POST':
        id_rastreo = request.form['id_rastreo']
        query = bd.rastreo(id_rastreo)
        paquete = bd.get_paquetes_editar(id_rastreo)
        try:
            if consulta:
                return render_template("index.html", login = consulta,rastreos = query,paquetes = paquete)
        except NameError:
            return render_template('index.html',login_no = False,rastreos = query,paquetes = paquete)

        
if __name__ == '__main__':
    app.run(debug=True)

import conexion

def Register(nombre,correo,contra):
    consulta = conexion.conexion_bd()
    consulta[0].execute("INSERT INTO usuarios(nombre,correo,contrasena) VALUES(%s,%s,%s)",(nombre,correo,contra))
    consulta[1].commit()
    consulta[0].close()
    return True

def verificar_correo_exis(correo):
    consulta = conexion.conexion_bd()
    consul = consulta[0].execute("SELECT correo FROM usuarios WHERE correo=%s",(correo))
    consulta[1].commit()
    consulta[0].close()
    return consul

def login(correo, contra):
    global datos
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT correo,contrasena FROM usuarios WHERE correo=%s AND contrasena=%s",(correo,contra))
    datos = consulta[0].fetchone()
    print(datos)
    consulta[0].close()
    return datos

def get_paquetes():
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT * FROM paquetes")
    datos = consulta[0].fetchall()
    consulta[0].close()
    return datos

def reg_paquetes(n_r, n_d, d_r, d_d, c_r, c_d, e_r, e_d, ciudad_r, ciudad_d, descripcion):
    consulta = conexion.conexion_bd()
    consul = consulta[0].execute("INSERT INTO paquetes(nom_remitente,nom_destinatario,direccion_remitente,direccion_destinatario,cp_remitente,cp_destinatario,estado_remitente,estado_destinatario,ciudad_remitente,ciudad_destinatario,descripcion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(n_r, n_d, d_r, d_d, int(c_r), int(c_d), e_r, e_d, ciudad_r, ciudad_d, descripcion))
    consulta[1].commit()
    consulta[0].close()
    return True
    
def get_paquetes_editar(id):
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT * FROM paquetes WHERE id_paquete = %s",(id))
    datos = consulta[0].fetchone()
    consulta[0].close()
    return datos

def reg_paquetes_editar(id,n_r, n_d, d_r, d_d, c_r, c_d, e_r, e_d, ciudad_r, ciudad_d, descripcion):
    consulta = conexion.conexion_bd()
    consul = consulta[0].execute("UPDATE paquetes SET nom_remitente = %s,nom_destinatario = %s,direccion_remitente = %s,direccion_destinatario = %s,cp_remitente = %s,cp_destinatario = %s,estado_remitente = %s,estado_destinatario = %s,ciudad_remitente = %s,ciudad_destinatario = %s,descripcion = %s WHERE id_paquete = %s",(n_r, n_d, d_r, d_d, int(c_r), int(c_d), e_r, e_d, ciudad_r, ciudad_d, descripcion, id))
    consulta[1].commit()
    consulta[0].close()
    return consul

def reg_paquetes_eliminar(id):
    consulta = conexion.conexion_bd()
    consul = consulta[0].execute("DELETE FROM paquetes WHERE id_paquete = %s",(id))
    consulta[1].commit()
    consulta[0].close()
    return consul

def get_usuarios():
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT id_usuario,nombre,correo FROM usuarios")
    usuarios = consulta[0].fetchall()
    consulta[0].close()
    return usuarios

def get_historial():
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT * FROM historial_estados")
    historial = consulta[0].fetchall()
    consulta[0].close()
    return historial

def historial_reg(id_paquete,estado,lugar):
    consulta = conexion.conexion_bd()
    consul = consulta[0].execute("INSERT INTO historial_estados(paquete_id,estado,lugar) VALUES(%s,%s,%s)",(int(id_paquete),estado,lugar))
    consulta[1].commit()
    consulta[0].close()
    return consul

def rastreo(id):
    consulta = conexion.conexion_bd()
    consulta[0].execute("SELECT * FROM historial_estados WHERE paquete_id = %s",(id))
    historial = consulta[0].fetchall()
    consulta[0].close()
    return historial

data = rastreo(1)
print(data)
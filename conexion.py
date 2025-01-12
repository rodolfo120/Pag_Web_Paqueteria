import pymysql

def conexion_bd():
    conexionbd = pymysql.connect(
    host="sql3.freemysqlhosting.net",
    user="sql3749786",
    password="7Q5y8lZtpw",
    database="sql3749786"
    )
    cursor = conexionbd.cursor()
    return cursor,conexionbd
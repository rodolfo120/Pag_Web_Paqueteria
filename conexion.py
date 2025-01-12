import pymysql

def conexion_bd():
    conexionbd = pymysql.connect(
    host="",
    user="",
    password="",
    database=""
    )
    cursor = conexionbd.cursor()
    return cursor,conexionbd
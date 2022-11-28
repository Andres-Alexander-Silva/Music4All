import pymysql

def obtener_conexion():
    conexion = pymysql.connect(host="54.147.25.136", user= "test", password= "test1_*", db= "Music4All")
    return conexion
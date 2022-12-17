from db import obtener_conexion

class DescargaDao():
    
    @classmethod
    def insertar(self, descarga):
        try:
            conexion = obtener_conexion()
            
            id_url = descarga.getInfoUrl().getIdUrl()
            id_usuario = descarga.getUsuario().getId()
            
            with conexion.cursor() as cursor:
                sql_insert = "INSERT INTO Descarga (id_descarga, url, id_usuario) VALUES (Null, %s, %s)"
                datos = (id_url, id_usuario)
                cursor.execute(sql_insert, datos)
            
            conexion.commit()
            conexion.close()
            
            return "Registro realizado con exito"
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar(self):
        try:
            conexion = obtener_conexion()
            descargas = []
            
            with conexion.cursor() as cursor:
                sql_select = "SELECT * FROM Descarga"
                cursor.execute(sql_select)
                descargas = cursor.fetchall()
            
            conexion.close()
            
            return descargas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def consultar_id(self, id):
        try:
            conexion = obtener_conexion()
            descargas = []
            
            with conexion.cursor() as cursor:
                sql_select_id = "SELECT d.id_usuario , iu.url_nombre FROM Descarga d JOIN InformacionURL iu ON (d.url = iu.url_id) WHERE d.id_usuario = %s;"
                cursor.execute(sql_select_id, (id))
                descargas = cursor.fetchall()
                
            conexion.close()
            
            return descargas
        except Exception as ex:
            raise Exception(ex)
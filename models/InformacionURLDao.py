from db import obtener_conexion

class InformacionURLDao():
    
    @classmethod
    def insertar(self, url):
        try:
            url_name = url.getUrlNombre()
            url_duracion = url.getUrlDuracion()
            url_autor = url.getUrlAutor()
            
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_insert = "INSERT INTO InformacionURL (url_id, url_nombre, url_duracion, url_autor) VALUES (Null, %s, %s, %s)"
                datos = (url_name, url_duracion, url_autor)
                cursor.execute(sql_insert, datos)
                
            conexion.commit()
            conexion.close()
            
            return "URL registrada con exito"
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def consultar(self):
        try:
            conexion = obtener_conexion()
            urls = []
            
            with conexion.cursor() as cursor:
                sql_select = "SELECT * FROM InformacionURL"
                cursor.execute(sql_select)
                urls = cursor.fetchall()
            
            conexion.close()
            
            return urls
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def consultar_id(self, id):
        try:
            conexion = obtener_conexion()
            url = None
            
            with conexion.cursor() as cursor:
                sql_select_id = "SELECT * FROM InformacionURL WHERE url_id = %s"
                cursor.execute(sql_select_id, (id))
                url = cursor.fetchone()
            
            conexion.close()
            
            return url
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def actualizar(self, url, id):
        pass 
    
    @classmethod
    def borrar(self, id):
        try: 
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_delete = "DELETE FROM InformacionURL WHERE id = %s"
                cursor.execute(sql_delete, (id))
            
            conexion.commit()
            conexion.close()
            
            return "Borrado Existoso"
        except Exception as ex:
            raise Exception(ex)             
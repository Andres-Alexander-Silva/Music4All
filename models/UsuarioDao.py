from db import obtener_conexion

class UsuarioDao():
    
    @classmethod
    def insertar(self, usuario):
        try:
            nombre = usuario.getNombre()
            apellido = usuario.getApellido()
            username = usuario.getUsuario()
            password = usuario.getContrasegna()
            
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_insert = "INSERT INTO Usuarios (id, nombre, apellido, usuario, contraseña) VALUES (Null, %s, %s, %s, %s)"
                datos = (nombre, apellido,username, password)
                cursor.execute(sql_insert, datos)
            
            conexion.commit()
            conexion.close()
            
            return True             
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def consultar(self):
        try:
            conexion = obtener_conexion()
            usuarios = []
            
            with conexion.cursor() as cursor:
                sql_select = "SELECT * FROM Usuarios"
                cursor.execute(sql_select)
                usuarios = cursor.fetchall()
                
            conexion.close()
                
            return usuarios
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def consultar_id(self, usuarioI):
        try:
            conexion = obtener_conexion()
            usuario = None
            
            with conexion.cursor() as cursor:
                sql_select_id = "SELECT usuario,contraseña FROM Usuarios WHERE usuario = %s"
                cursor.execute(sql_select_id, (usuarioI))
                usuario = cursor.fetchone()
                
            conexion.close()
                
            return usuario
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def actualizar(self, usuario, password):
        try:
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_update = "UPDATE Usuarios SET contraseña = %s WHERE id = %s"
                datos = (password, usuario)
                cursor.execute(sql_update, datos)
                
            conexion.commit()
            conexion.close()
                
            return "Actualizacion realizada"
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def borrar(self, id):
        try:
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_delete = "DELETE FROM Usuarios WHERE id = %s"
                cursor.execute(sql_delete, (id))
                
            conexion.commit()
            conexion.close()
            
            return "Borrado Exitoso"
        except Exception as ex:
            raise Exception(ex)
from db import obtener_conexion 
class PersonaDao():
    
    @classmethod
    def insertar(self, persona):
        try:
            nombre = persona.getNombre()
            apellido = persona.getApellido()
        
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_insert = "INSERT INTO Persona (id,nombre,apellido) VALUES (Null, %s, %s)"
                datos = (nombre, apellido)
                cursor.execute(sql_insert, datos)
            
            conexion.commit()
            conexion.close()
            
            return "Registrado con Exito"
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def consultar(self):
        try:
            conexion = obtener_conexion()
            personas = []
            
            with conexion.cursor() as cursor:
                sql_select = "SELECT * FROM Persona"
                cursor.execute(sql_select)
                personas = cursor.fetchall()
            
            conexion.close()
            
            return personas
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def consultar_id(self, id):
        try:
            conexion = obtener_conexion()
            persona = None
            
            with conexion.cursor() as cursor:
                sql_select_id = "SELECT * FROM Persona WHERE id = %s"
                cursor.execute(sql_select_id, (id))
                persona = cursor.fetchone()
            
            conexion.close()
            
            return persona
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def actualizar(self, persona, id):
        try:
            conexion = obtener_conexion()
            nombre = persona.getNombre()
            apellido = persona.getApellido()
            
            with conexion.cursor() as cursor:
                sql_update = "UPDATE Persona SET nombre = %s, apellido = %s WHERE id = %s"
                datos = (nombre, apellido, id)
                cursor.execute(sql_update, datos)
            
            conexion.commit()
            conexion.close()
            
            return "Actualizacion Exitosa"
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def borrar(self, id):
        try:
            conexion = obtener_conexion()
            
            with conexion.cursor() as cursor:
                sql_dalete = "DELETE FROM Persona WHERE id = %s"
                cursor.execute(sql_dalete, (id))
                
            conexion.commit()
            conexion.close()
            
            return "Borrado exitoso"
        except Exception as ex:
            raise Exception(ex)
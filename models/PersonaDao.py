class PersonaDao():
    
    @classmethod
    def insert(self, db, persona):
        try:
            nombre = persona.getNombre()
            apellido = persona.getApellido()
            datos = (nombre, apellido)
            sql_insert = 'INSERT INTO Persona (id, nombre, apellido) VALUES (Null, %s, %s)'
            cursor = db.connection.cursor()
            cursor.execute(sql_insert,datos)
            db.connection.commit()
            return "Registrado en la Base de Datos"
        except Exception as ex:
            raise Exception(ex)   
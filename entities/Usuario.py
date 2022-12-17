from werkzeug.security import check_password_hash, generate_password_hash
class Usuario():
    
    def __init__(self, nombre, apellido, usuario, contrasegna):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__contrasegna = contrasegna
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, usuario):
        self.__usuario = usuario
    
    def getContrasegna(self):
        return self.__contrasegna
    
    def setContrasegna(self, contrasegna):
        self.__contrasegna = contrasegna
    
    @classmethod
    def createPassword(self, contrasegna):
        return generate_password_hash(contrasegna)
    
    @classmethod
    def checkPassword(self, hashed_password, contrasegna):
        return check_password_hash(hashed_password, contrasegna)
    
    def __str__(self):
        return "Usuario {"+"\nid= "+str(self.__id)+"\nusuario= "+self.__usuario+"\ncontraseña= "+self.__contrasegna+" }"
import Persona as p

class Usuario(p.Persona):
    
    def __init__(self, id, usuario, contrasegna):
        self.__id = id
        self.__usuario = usuario
        self.__contrasegna = contrasegna
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, usuario):
        self.__usuario = usuario
    
    def getContrasegna(self):
        return self.__contrasegna
    
    def setContrasegna(self, contrasegna):
        self.__contrasegna = contrasegna
    
    def __str__(self):
        return "Usuario {"+"\nid= "+str(self.__id)+"\nusuario= "+self.__usuario+"\ncontraseña= "+self.__contrasegna+" }"
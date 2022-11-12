class Persona():
    
    def __init__(self, nombre, apellido):
        # self.id = id
        self.nombre = nombre
        self.apellido = apellido
    
    # def getId(self):
    #    return self.id
    
    # def setId(self, id):
    #     self.id = id
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getApellido(self):
        return self.apellido
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def __str__(self):
        return "Persona{"+"\nnombre="+self.nombre+"\napellido="+self.apellido+"}"

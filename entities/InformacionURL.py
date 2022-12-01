class InformacionURL():
    
    def __init__(self, url_nombre, url_duracion, url_autor):
        self.url_nombre = url_nombre
        self.url_duracion = url_duracion
        self.url_autor = url_autor
    
    def getUrlNombre(self):
        return self.url_nombre
    
    def setUrlNombre(self, url_nombre):
        self.url_nombre = url_nombre
    
    def getUrlDuracion(self):
        return self.url_duracion
    
    def setUrlDuracion(self, url_duracion):
        self.url_duracion = url_duracion
    
    def getUrlAutor(self):
        return self.url_autor
    
    def setUrlAutor(self, url_autor):
        self.url_autor = url_autor
    
    def __str__(self):
        return "informacion Url {"+"\nid= "+self.id_url+"\nNombre= "+self.url_nombre+"\nDuracion= "+self.url_duracion+"\nAutor= "+self.url_autor+"}"
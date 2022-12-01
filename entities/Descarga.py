import InformacionURL as infoUrl
class Descarga(infoUrl.InformacionURL):
    
    def __init__(self, id_descarga, infoUrl, User):
        self.id_descarga = id_descarga
        self.url = infoUrl
        self.id_usuario = User
    
    def getIdDescarga(self):
        return self.id_descarga

    def setIdDescarga(self, id_descarga):
        self.id_descarga = id_descarga
    
    def getInfoUrl(self):
        return self.url
    
    def setUrl(self, infoUrl):
        self.url = infoUrl
    
    def getUsuario(self):
        return self.id_usuario
    
    def setUsuario(self, User):
        self.id_usuario = User
    
    def __str__(self):
        return "Descarga {"+"\nid= "+str(self.id_descarga)+"\nurl= "+self.url+"\ntipo= "+self.tipo_url+"}"
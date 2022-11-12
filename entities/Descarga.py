import InformacionURL as infoUrl

class Descarga(infoUrl.InformacionURL):
    
    def __init__(self, id_descarga, url, tipo_url):
        self.id_descarga = id_descarga
        self.url = url
        self.tipo_url = tipo_url
    
    def getIdDescarga(self):
        return self.id_descarga

    def setIdDescarga(self, id_descarga):
        self.id_descarga = id_descarga
    
    def getUrl(self):
        return self.url
    
    def setUrl(self, url):
        self.url = url
    
    def getTipoUrl(self):
        return self.tipo_url
    
    def setTipoUrl(self, tipo_url):
        self.tipo_url = tipo_url
    
    def __str__(self):
        return "Descarga {"+"\nid= "+str(self.id_descarga)+"\nurl= "+self.url+"\ntipo= "+self.tipo_url+"}"
class Categoria():
    
    def __init__(self, id_categoria, categoria):
        self.id_categoria = id_categoria
        self.categoria = categoria
    
    def getIdCategoria(self):
        return self.id_categoria
    
    def setIdCategoria(self, id_categoria):
        self.id_categoria = id_categoria
    
    def getCategoria(self):
        return self.categoria
    
    def setCategoria(self, categoria):
        self.categoria =categoria
    
    def __str__(self):
        return "Categorias {"+"\id= "+str(self.id_categoria)+"\nCategoria= "+self.categoria+"}"
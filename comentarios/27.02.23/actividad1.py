class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
        #print('Constructor Activado')        

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha,doc):
        Persona.__init__(self,nombre)
        self.ficha=ficha
        self.doc=doc       
        self.all=self.nombre,self.doc,self.ficha

    def getFicha(self):
        return self.ficha
    def getdoc(self):
        return self.doc
    def getall(self):
        return self.all
app=Aprendiz('Pedro',12345,918273645)
print(app.getFicha())
print(app.getNombre())
print(app.getdoc())
print(app.getall())
print(app.getall())

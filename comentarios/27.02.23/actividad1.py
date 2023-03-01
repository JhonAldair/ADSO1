class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha,doc):
        Persona.__init__(self,nombre)
        self.__ficha=ficha
        self.__doc=doc       
        self.__nombre=nombre
        self.__all=self.__nombre,self.__doc,self.__ficha

    def getFicha(self):
        return self.__ficha
    def getdoc(self):
        return self.__doc
    def getall(self):
        return self.__all
app=Aprendiz('Pedro',12345,918273645)
print(app.getFicha())
print(app.getNombre())
print(app.getdoc())
print(app.getall())
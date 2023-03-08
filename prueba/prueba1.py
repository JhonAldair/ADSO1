class usuario:
    def __init__(self,id,nombre,direccion,telefono,tipo):
        self.__id=id
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.tipo=tipo
    def getinformacion(self):
        return self.__id, self.__nombre, self.__direccion, self.__telefono, self.tipo
    def setinfotmacion(self,id,nombre,direccion,telefono,tipo):
        self.__id=id
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.tipo=tipo
        return self.__id, self.__nombre, self.__direccion, self.__telefono,self.tipo

class estudiante(usuario):
    def __init__(self,id,nombre,direccion,telefono,tipo):
        usuario.__init__(self,id,nombre,direccion,telefono,tipo)
    def setinfotmacion(self, id, nombre, direccion, telefono,tipo):
        super().setinfotmacion(id, nombre, direccion, telefono,tipo)

class maestro(usuario):
    def __init__(self,id,nombre,direccion,telefono,tipo):
        usuario.__init__(self,id,nombre,direccion,telefono,tipo)
    def setinfotmacion(self, id, nombre, direccion, telefono,tipo):
        super().setinfotmacion(id, nombre, direccion, telefono,tipo)

class natural(usuario):
    def __init__(self,id,nombre,direccion,telefono,tipo):
        usuario.__init__(self,id,nombre,direccion,telefono,tipo)
    def setinfotmacion(self, id, nombre, direccion, telefono,tipo):
        super().setinfotmacion(id, nombre, direccion, telefono,tipo)

class material:
    def __init__(self):
        self.mat={'moby dick':{ 'codigo':123,'genero':'aventuras','autor':'Herman Nerville','editorial':'na','tipo':'libro'},
    'pepito':{ 'codigo':234,'genero':'accion','autor':'jhon','editorial':'sena','tipo':'revista'},
    'grillo':{ 'codigo':543,'genero':'comedio','autor':'jhon','editorial':'sena','tipo':'revista'}
}
    def getmaterial(self):
        for esp, en in self.mat.items():
            print('-',esp,':',en)
    def agregarcat(self,titulo,codigo,genero,autor,editorial,tipo):
        self.mat.update({titulo:{'codigo':codigo,'genero':genero,'autor':autor,'editorial':editorial,'tipo':tipo}})
        for esp, en in self.mat.items():
            print('-',esp,':',en)
    def buscautor(self,nombre):
        for x,y in self.mat.items():
            if nombre==y['autor']:
                print('los libros de este autor son: ',x)
class bibliotecario:
    def __init__(self,id,nombre,telefono,direccion):
        self.__id=id
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    def getinformacion(self):
        return self.__id, self.__nombre, self.__direccion, self.__telefono
    def setinfotmacion(self,id,nombre,direccion,telefono):
        self.__id=id
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        return self.__id, self.__nombre, self.__direccion, self.__telefono
    def vercatalogo(self):
        instancia=material()
        instancia.getmaterial()

'''biblio=bibliotecario(12345,'luis lopez','312123','calle 12')
print(biblio.getinformacion())
print(biblio.setinfotmacion(98765,'luisa lopez','312987','calle 11'))
biblio.vercatalogo()'''


'''user=usuario(6754,'jaime guzman','calle 10',321123)
print(user.getinformacion())
print(user.setinfotmacion(6754,'jeime garcia','calle 10',321123))'''

'''estudent=estudiante(6754,'jaime guzman','calle 10',321123,'estudiante')
print(estudent.getinformacion())
estudent.setinfotmacion(6754,'jeime garcia','calle 10',321123,'profesor')
print(estudent.getinformacion())'''
'''prof=maestro(6754,'jaime guzman','calle 10',321123,'estudiante')
print(prof.getinformacion())
prof.setinfotmacion(6754,'jeime garcia','calle 10',321123,'profesor')
print(prof.getinformacion())'''

'''galeria=material()
galeria.getmaterial()
galeria.agregarcat('jaja',1234,'dsads','dsa',23,43)
galeria.buscautor('jhon')'''
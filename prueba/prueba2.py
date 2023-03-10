lista={123:{'nombre':'juan','direccion':'calle12','telefono':312123,'tipo':'estudiante'},
        987:{'nombre':'juana','direccion':'calle13','telefono':314708,'tipo':'maestro'}
}

class material:
    def __init__(self):
        self.mat={12345:{ 'titulo':'moby dick','genero':'aventuras','autor':'Herman Nerville','editorial':'na','tipo':'libro'},
    5421:{ 'titulo':'pepito','genero':'accion','autor':'jhon','editorial':'sena','tipo':'libro'},
    78945:{ 'titulo':'grillo','genero':'comedio','autor':'jhon','editorial':'sena','tipo':'libro'}}
    def getmaterial(self):
        for esp, en in self.mat.items():
            print('-',esp,':',en)
    def agregarcat(self,codigo,titulo,genero,autor,editorial,tipo):
        self.mat.update({codigo:{'titulo':titulo,'genero':genero,'autor':autor,'editorial':editorial,'tipo':tipo}})
        for esp, en in self.mat.items():
            print('-',esp,':',en)

class pedido:
    def __init__(self):
        pass
    def reservar(self,id,codigo):
        reserv=material()
        for i in lista:
            if id==i:
                for k,l in reserv.mat.items():
                    if codigo==k:
                        print('el libro que va a reservar sera:',l['titulo'])
                del(reserv.mat[codigo])    
        for esp, en in reserv.mat.items():
            print('-',esp,':',en)

class lector:
    def __init__(self,id,nombre,direccion,telefono):
        self.nombre=nombre
        self.id=id
        self.direccion=direccion
        self.telefono=telefono
    def getinformacion(self):
        print('nombre:',self.nombre,'\ncedula:',self.id,'\ndireccion:',self.direccion,'\ntelefono',self.telefono)
    def setinfotmacion(self,nombre,id,direccion,telefono):
        self.nombre=nombre
        self.id=id
        self.direccion=direccion
        self.telefono=telefono
        print('nombre:',self.nombre,'\nid:',self.id,'\ndireccion:',self.direccion,'\ntelefono',self.telefono)

class estudiante(lector):
    rol='estudiante'
    def __init__(self,id,nombre,direccion,telefono):
        lector.__init__(self,id,nombre,direccion,telefono)
class maestro(lector):
    rol='maestro'
    def __init__(self,id,nombre,direccion,telefono):
        lector.__init__(self,id,nombre,direccion,telefono)

class bibliotecario:
    def __init__(self,id,nombre,direccion,telefono):
        self.nombre=nombre
        self.id=id
        self.direccion=direccion
        self.telefono=telefono
    def getinformacion(self):
        print('nombre:',self.nombre,'\ncedula:',self.id,'\ndireccion:',self.direccion,'\ntelefono',self.telefono)
    def setinfotmacion(self,nombre,id,direccion,telefono):
        self.nombre=nombre
        self.id=id
        self.direccion=direccion
        self.telefono=telefono
        print('nombre:',self.nombre,'\nid:',self.id,'\ndireccion:',self.direccion,'\ntelefono',self.telefono)
    def vermaterial(self):
        catalogo=material()
        catalogo.getmaterial()
    def agregarmat(self,id,titulo,genero,autor,editorial,tipo):
        catalogo=material()
        catalogo.agregarcat(id,titulo,genero,autor,editorial,tipo)
    def reservarmaterial(self,iduser,idmat):
        reserv=pedido()
        reserv.reservar(iduser,idmat)

a=input('hola!\nbienvenido al sistema bibliotecario\ningrese rol\n-lector\n-bibliotecario:')
if a == 'lector':
    b=input('estudiante o maestro:')
    if b == 'estudiante':
        c=input('ingrese su nombre:')
        d=input('ingrese su direccion:')
        e=input('ingrese su telefono:')
        f=input('ingrese su cedula:')
        lista.update({f:{'nombre':c,'direccion':d,'telefono':e,'tipo':'estudiante'}})
        g=estudiante(f,c,d,e,)
        g.getinformacion()
        h=input('desea cambiar la informacion?')
        if h=='si':
            i=input('ingrese nuevo nombre:')
            j=input('ingrese nueva direccion:')
            k=input('ingrese nuevo telefono:')
            l=input('ingrese nueva cedula:')
            g.setinfotmacion(i,l,j,k)
            g.getinformacion
    if b == 'maestro':
        c=input('ingrese su nombre:')
        d=input('ingrese su direccion:')
        e=input('ingrese su telefono:')
        f=input('ingrese su cedula:')
        lista.update({f:{'nombre':c,'direccion':d,'telefono':e,'tipo':'estudiante'}})
        g=maestro(f,c,d,e,)
        g.getinformacion()
        h=input('desea cambiar la informacion?')
        if h=='si':
            i=input('ingrese nuevo nombre:')
            j=input('ingrese nueva direccion:')
            k=input('ingrese nuevo telefono:')
            l=input('ingrese nueva cedula:')
            g.setinfotmacion(i,l,j,k)
            g.getinformacion
if a == 'bibliotecario':
        c=input('ingrese su nombre:')
        d=input('ingrese su direccion:')
        e=input('ingrese su telefono:')
        f=input('ingrese su cedula:')
        g=bibliotecario(f,c,d,e,)
        g.getinformacion()
        z=input('desea cambiar la informacion?')
        if z=='si':
            i=input('ingrese nuevo nombre:')
            j=input('ingrese nueva direccion:')
            k=input('ingrese nuevo telefono:')
            l=input('ingrese nueva cedula:')
            g.setinfotmacion(i,l,j,k)
            g.getinformacion
        else:
            print('ok')
        h=input('que accion desea realizar:\n-ver el material\n-agregar material\n-reservar al cliente\n-ver usuarios:')
        if h=='agregar material':
            i=input('codigo del material')
            j=input('titulo del material')
            k=input('genero del material')
            l=input('autor del material')
            m=input('editorial del material')
            n=input('tipo de material')
            g.agregarmat(i,j,k,l,m,n)
        if h=='ver el material':
            g.vermaterial()
        if h=='reservar al cliente':
            ñ=int(input('ingrese codigo de usuario'))
            o=int(input('ingrese codigo del material'))
            g.reservarmaterial(ñ,o)
        if h =='ver usuarios':
            for i,j in lista.items():
                print('id =',i,':',j)

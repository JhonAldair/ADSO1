class Persona:                                      #se crea una clase llamda persona
    def __init__(self,nombre):                      #se crea un metodo init que sirve para inicializar el objeto, la funcion self sirve para hacer referencia al objeto, con el parametro nombre
        self.__nombre=nombre                        # se asigna un atributo en la clase, se hace privado un dato con "__"
        #print('Constructor Activado')              

    def getNombre(self):                            #se define una funcion get que sirve para mostrar un dato por separado, con el parametro self que nos ubica en la clase
        return self.__nombre                        #retornara el atributo nombre de la clase

    def setNombre(self,nombre):                     #se define una funcion set que sirve para modificar un dato,con el parametro self que nos ubica en la clase y el parametro nombre que sera el que modificaremos  
        self.__nombre=nombre                        #se redifinira el dato nombre

ob=Persona('Maria')                                 #se crea un objeto con el parametro de la clase persona
print(ob.getNombre())                               #se imprime el modulo "getNombre" con el parametro del objeto
ob.setNombre('Ana')                                 #se llama el metodo setnombre con el parametro nuevo 
print(ob.getNombre())                               #se imprime el modulo "getnombre" con el parametro modificado del modulo setNombre
#print(type(ob))

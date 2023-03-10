from Persona import *                                   #de la clase persona se importan todos sus elementos
#from Curso import * ...en caso de composición
class Aprendiz(Persona):                                #se crea una clase llamada aprendiz, subclase de persona
    def __init__(self,ficha,nombre,documento):          #se crea el iniciador con los paramteros ficha, nombre, documento  
        Persona.__init__(self,nombre,documento)         #se llama al constructor de la superclase 
        self.__ficha=ficha                              #se agrega el atributo ficha
        self.__cursos=[]                                #se agrega una lista vacia llamada cursos
    def getFicha(self):                                 #se define una funcion get
        return self.__ficha                             #se retorna la ficha
    def setNombre(self,ficha):                          #se define una funcion set
        self.__ficha=ficha                              #se cambia el dato de ficha 
    def agregarCurso(self,curso):                       #se define una funcion con el parametro curso
        #c=Curso('python',120)          
        self.__cursos.append(curso)                     #se agregara el parametro curso a la lista vacia llamada cursos
    def getCursos(self):                                #se define una funcion get
        return self.__cursos                            #se retornara la lista llamada cursos
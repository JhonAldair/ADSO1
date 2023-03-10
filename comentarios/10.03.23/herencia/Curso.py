class Curso:                            #se crea una clase llamada curso
    def __init__(self,nombre,horas):    #se abre e constructor con los parameros nombre y horas
        self.__nombre=nombre            #se agrega el atributo nombre
        self.__horas=horas              #se agrega el atributo horas
    def getNombre(self):                #se define una funcion get
        return self.__nombre            #se retorna el nombre
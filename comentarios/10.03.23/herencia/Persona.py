class Persona:                                      #se crea una clase llamada persona
    def __init__(self,nombre,documento):            #se abre un iniciador con los parametros nombre y documento
        self.__nombre=nombre                        #se agrega el atributo nombre
        self.__documento=documento                  #se agregar el atributo documento
    def getNombre(self):                            #se define una funcion get
        return self.__nombre                        #se retornara el nombre
    def getDocumento(self):                         #se crea una funcion get
        return self.__documento                     #se retornara el documento
    def setNombre(self,nombre):                     #se crea una funcion set con el parametro nombre
        self.__nombre=nombre                        #se cambia el dato nombre por el nuevo dato
    def setDocumento(self,documento):               #se crea una funcion set con el parametro documento
        self.__documento=documento                  #se cambia el dato doccumento por el nuevo dato
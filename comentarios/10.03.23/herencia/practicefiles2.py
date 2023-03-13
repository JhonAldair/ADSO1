from Aprendiz import *                                                                      #de la clase aprendiz se importan todos sus datos
from Curso import *                                                                         #de la clase aprendiz se importan todos sus datos

# nombre=input('ingrese nombre del Aprendiz')
# documento=int(input('ingrese documento del aprendiz'))
# ficha=input('ingrese ficha del aprendiz')

# ap=Aprendiz(ficha,nombre,documento)

# nombreCurso=input('ingrese nombre del curso')
# horas=int(input('ingrese intensidad horaria del curso'))
# c1=Curso(nombreCurso,horas)
# ap.agregarCurso(c1)

# with open('herencia/aprendices.txt','a') as flujo:    
#     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

with open('\herencia\aprendices.txt','r') as flujo:                                             #el metodo open permite abrir cualquier archivo del sistema, se pone de parametros, la ruta del archivo, si lo quiere leer,escribir o modificar
    datos=flujo.read()                                                                          #se define una variable para poder leer el texto dentro de flujo
    print(datos)                                                                                #se imprimen los datos en forma de texto que hayan dentro de flujo
    #flujo.write('2560664,maria,123')
aprendices=[]                                                                                   #se abre una lista vacia llamada aprendices
with open('herencia\aprendices.txt','r') as flujo:                
    for linea in flujo:                                                                         #se abre un for que recorrera los datos dentro de flujo
        #print(linea)
        aprendices.append(linea.rsplit())                                                       #se agregan los datos de flujo a la lista aprendices

datosxlinea=[]                                                                                  #se abre uan lista vacia llamda datosxlinea
for aprendiz in aprendices:                                                                     #se abre un for que recorre la lista aprendices
    datosxlinea.append(aprendiz[0].split(','))                                                  #se agregan los datos de aprendices a la lista datosxlinea

#print(ob.getNombre())

print(datosxlinea)                                                                              #se imprime la lista datosxlinea

listaDeObjetos=[]                                                                               #se agrega una lista vacia llamada listadeobjetos
for apr in datosxlinea:                                                                         #se abre un for que recorre la lista datosxlinea
     f=apr[0]                                                                                   #se le asigna el primer valor de la lista a la variable f
     n=apr[1]                                                                                   #se le asigna el segundo valor de la lista a la variable n
     d=apr[2]                                                                                   #se le asigna el tercer valor de la lista a la variable d
     ob=Aprendiz(f,n,d)                                                                         #se crea un objeto de la clase aprendiz con los atributos de las variables con los valores de la lsita listadeobjetos
     print(ob)                                                                                  #se imprime el objeto
     listaDeObjetos.append(ob)                                                                  #se agrega el objeto a la lista listadeobejtos

for xx in listaDeObjetos:                                                                       #se crea un for que recorre listadeobjetos
    print(xx.getNombre())                                                                       #se imprimen los datos del atributo nombre de la clase aprendiz
    print(xx.getDocumento())                                                                    #se imprimen los datos del atributo documento de la clase aprendiz
    print(xx.getFicha())                                                                        #se imprimen los datos del atributo ficha de la clase aprendiz

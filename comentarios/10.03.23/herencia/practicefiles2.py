from Aprendiz import *                                                                      #de la clase aprendiz se importan todos sus datos
from Curso import *                                                                         #de la clase aprendiz se importan todos sus datos

# nombre=input('ingrese nombre del aprendiz')
# documento=int(input('ingrese documento del aprendiz'))
# ficha=input('ingrese ficha del aprendiz')

# ap=Aprendiz(ficha,nombre,documento)

# nombreCurso=input('ingrese nombre del curso')
# horas=int(input('ingrese intensidad horaria del curso'))
# c1=Curso(nombreCurso,horas)
# ap.agregarCurso(c1)

# with open('herencia/aprendices.txt','a') as flujo:    
#     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

with open('herencia/aprendices.txt','r') as flujo:                                              #el metodo open permite abrir cualquier archivo del sistema, se pone de parametros, la ruta del archivo, si lo quiere leer,escribir o modificar; la forma with hace que una vez acabada la  
    datos=flujo.read()                                                                          #
    print(datos)                                                                                #
    #flujo.write('2560664,maria,123')
aprendices=[]                                                                                   #
with open('herencia/aprendices.txt','r') as flujo:                                              #
    for linea in flujo:                                                                         #
        #print(linea)
        aprendices.append(linea.rsplit())                                                       #

datosxlinea=[]                                                                                  #
for aprendiz in aprendices:                                                                     #
    datosxlinea.append(aprendiz[0].split(','))                                                  #

#print(ob.getNombre())

print(datosxlinea)                                                                              #

listaDeObjetos=[]                                                                               #
for apr in datosxlinea:                                                                         #
     f=apr[0]                                                                                   #
     n=apr[1]                                                                                   #
     d=apr[2]                                                                                   #
     ob=Aprendiz(f,n,d)                                                                         #
     print(ob)                                                                                  #
     listaDeObjetos.append(ob)                                                                  #

for xx in listaDeObjetos:                                                                       #
    print(xx.getNombre())                                                                       #
    print(xx.getDocumento())                                                                    #
    print(xx.getFicha())                                                                        #
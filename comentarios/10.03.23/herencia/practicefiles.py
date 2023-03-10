from Aprendiz import *                              #de la clase aprendiz se importan todos sus elementos
from Curso import *                                 #de la clase cursos se importan todos sus elementos

ap=Aprendiz('2560664A','Diego Suarez',123456)       #se crea un objeto de la clase aprendiz con los parametros'2560664A','Diego Suarez',123456
c1=Curso('Python Intermedio',200)                   #se crea un objeto de la clase cursos con los parametros 'Python Intermedio',200
c2=Curso('Python Avanzado',200)                     #se crea un objeto de la clase cursos con los parametros 'Python Avanzado',200
#print(c1.getNombre())
ap.agregarCurso(c1)                                 #se agrega el objeto 'c1' como curso gracias a la funcion agregarcursos en la clase aprendiz (agregacion)
ap.agregarCurso(c2)                                 #se agrega el objeto 'c2' como curso gracias a la funcion agregarcursos en la clase aprendiz (agregacion)

for curso in ap.getCursos():                        #se crea un for que recorrera la lista llamada cursos en la clase aprendiz con los cursos agregados en la funcion agregarcursos
    print(curso.getNombre())                        #se imprimen los cursos ingresados en la funcion agregarcursos
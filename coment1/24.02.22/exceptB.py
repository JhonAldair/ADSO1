values = (1, 5)                                     #la variable que contiene una tupla con los valores 1 y 0
#x,y=10,12                                          #sirve para agregar valores a variables con una linea de codigo
#print(divmod(10,3))                                
try:                                                #try funciona para poder probar errores
    q, r = divmod(*values)                          #la funcion divmod lanza una tupla con dos valores, esta vez los de la variable de la primera linea, el primer valor muestra el resultado de la division, y la segunda el residuo; el asterisco sirve para asignarle rapidamente los valores de la tupla a estas variables y trabajar independientemente con cada una 
    #print('valor de q=',q)                         #una forma de imprimir una variable y un texto en un print
    print(f'q={q}')                                 #una forma mas rapida de imprimir una variable y un texto en un print, se escribe una f al principio del print, y ponemos entre llaves nuestra variable
    print(f'r={r}')                                 
except (ZeroDivisionError, TypeError) as e:         #guarda dos errores en la variable e
    print(type(e), e)                               #si se da el error, imprime el tipo de error
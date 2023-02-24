try:                                        #try funciona para poder probar errores
    #print(1/1))                            #prueba que muestra que si hay un error en la sintaxis, no sigue el programa
    raise SyntaxError                       #llama el error para que siempre de ese tipo de error
except SyntaxError as e:                    #la excepcion sytaxerror le modificamos el nombre a "e"
    print(e)                                #imprime el error con el nombre modificado
    print('Cierra el parentesis')           #imprime el mensaje del supuesto error de la linea 2
    
try:                                        
    #raise ZeroDivisionError                
    print(1/0)                              #imprime uno dividido por cero, que da error
#except (ZeroDivisionError) as e:           
except ZeroDivisionError as zde:
    print(zde)                              
    #print('prueba error')                  
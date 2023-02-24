def try_syntax(numerator, denominator):                             #definimos una funcion y le damos dos parametros
    try:                                                            #try funciona para poder probar errores
        print(f'In the try block: {numerator}/{denominator}')       #imprime de forma corta la division de los dos parametros de la funcion 
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator                            #la variable "result" guarda el resultado de la division de los dos parametros
    except ZeroDivisionError as zde:                                #si se da el error de dividir por cero, se guarda el error "zerodivisionerror" en la variable "zde"
        print(zde)                                                  #imprime el error "zerodivisionerror"
    else:                                                           #una condicion en caso de que no se cumpla el error
        print('The result is:', result)                             #imprime la variable "result"
        return result                                               #retorna la variable "result"
    finally:                                                        #el finally sirve para indicar cuanddo un try ya acabo
        print('Exiting')                                            #imprime "exiting"
        #return "Fallo por zero"
#print(try_syntax(12, 4))           
print(try_syntax(11, 23))                                          #imprime la funcion con los paametro que hayamos escogido
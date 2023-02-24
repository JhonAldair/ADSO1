def divisores(num):                                                 #crea funcion con un parametro
    try:                                                            #try funciona para poder probar errores
        for i in range(num+1):                                      #bucle for que toma el parametro de la funcion mas el numero 1, para que llegue hasta el ultimo numero
            if num%i==0:                                            #si el residuo del parametro dividido por el indice del ciclo for es cero
                print(i,' es divisor')                              #imprime el indice que tiene la condicion anterior
    except ZeroDivisionError:                                       #excepcion que evalua que una division no se pueda dividir por 0
        print('indeterminacion')                                    #imprime "indeterminacion" si se divide por cero
    except TypeError:                                               #excepcion que evalua el tipo de dato que se entregue
        print(type(num),'Tipo de dato no soportado')                #imprime "tipo de dato no soportado" type sirve mostrar el tipo de dato entregado

var=int(input('ingrese numero'))                                    #
divisores(var)
print('El programa continua en esta linea')
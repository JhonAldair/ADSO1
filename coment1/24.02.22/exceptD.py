def edad():                                                     #definicmos una funcion con parametros vacios
    try:                                                        #abre un bloque de codigo donde se haran pruebas
        tuedad=int(input("introduce tu edad"))                  #pide al usuario un numero entero y lo guarda en una variable llamada "tuedad"
        print(f'tu edad es  {tuedad}')                          #imprime de una forma rapida "tu edad es ("tuedad")" combinando texto y variables en un print
        #print('Tu edad es ',tuedad)                            #la misma impresion que la anterior linea de codigo pero de una forma mas larga
    except ValueError as e:                                     #verifica si se da el error valueerror y se guarda en una variable llamada e, 
        print(e)                                                #se imprime valueerror en la varaible e
        print("La edad debe ser un valor numerico...")          #se imprime la cadena "La edad debe ser un valor numerico..." 
        edad()                                                  #se llama la funcion dentro de la funcion para que siga repitiendose la funcion hasta que no de mas el error
    
edad()                                                          #se llama la funcion
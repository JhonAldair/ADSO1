#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número 
# exceda los límites emita un mensaje y finalice el programa
def cifras():
    num1 = int(input('ingrese un numero de maximo 4 cifras: '))
    if num1>=0 and num1<=9:
        return('el numero tiene 1 cifra')
    elif num1>=10 and num1<=99:
        return('el numero tiene dos cifras')
    elif num1>=100 and num1<=999:
        return('el numero tiene tres cifras')
    elif num1>=1000 and num1<=9999:
        return('el numero tiene 4 cifras')
    else:
        return('el numero no es valido')
print(cifras())
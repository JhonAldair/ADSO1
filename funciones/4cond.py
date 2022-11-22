#ingresar una nota y decir si es bajo, medio, buena
def nota():
    num1 = float(input('ingrese una nota: '))
    if num1>=1 and num1<=2:
        return('nota insuficiente')
    elif num1>=3 and num1<=4:
        return('nota baja')
    elif num1>=5 and num1<=6:
        return('nota media')
    elif num1>=7 and num1<=8:
        return('nota buena')
    elif num1>=9 and num1<=10:
        return('excelente')
    else:
        return('numero invalido')
print(nota())
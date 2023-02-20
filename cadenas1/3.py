#3.cuantas veces se repite un caracter dado
def caracter():
    a=input('ingrese palabra:')
    b=input('ingrese letra:')
    for i in a:
        m=a.count(b)
    print('la letra',b, 'se repite ',m,'veces')
caracter()
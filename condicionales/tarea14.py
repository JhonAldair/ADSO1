num1 = float(input('ingrese una nota: '))

if num1>=1 and num1<=2:
    print('nota insuficiente')
elif num1>=3 and num1<=4:
    print('nota baja')
elif num1>=5 and num1<=6:
    print('nota media')
elif num1>=7 and num1<=8:
    print('nota buena')
elif num1>=9 and num1<=10:
    print('excelente')
else:
    print('numero invalido')
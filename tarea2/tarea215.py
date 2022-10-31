num=int(input('digite un numero entero positivo: '))
nu=num+1
if num > 0:
    while nu>0:
        for i in range(1,nu):
            print(i,end='')
        nu-=1
        print()
else:
    print('el numero no esta dentro de los parametros')
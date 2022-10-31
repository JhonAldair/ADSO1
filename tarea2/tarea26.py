# Calcular el máximo de números positivos introducidos por
#teclado, sabiendo que metemos números hasta que
#introduzcamos uno negativo. El negativo no cuenta. 

num1=0
num2=0
while(num1>=0):
    num1=int(input('introduzca los numeros:'))
    if num1>0:
        num2+=1
    else:
        print('esta fue la cantidad de numeros registrados',num2)
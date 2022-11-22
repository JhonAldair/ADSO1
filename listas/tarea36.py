'''fibonacci'''
import random
vector=[]
aux=True
a=0
b=1
c=1
while aux:
    rango=int(input('elija numero de fibonacci: '))
    if rango>=5 and rango<20:
        aux=False
    else:
        print('deben ser minimo 5 elementos y maximo 20')
for _ in range(rango):
    c=a+b
    a=b
    b=c
    vector.append(c)
print('la lista con los valores de fibonacci hasta la posicion insertada es ',vector)
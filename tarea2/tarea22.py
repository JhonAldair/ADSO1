n=int(input('introduzca un numero para determinar si es primo o no:'))
i=1
c=0

while n>i:
    if n%i ==0:
        c+=1
    i+=1
if c > 2 or n <=1:
    print('no es primo')
else:
    print('es primo')
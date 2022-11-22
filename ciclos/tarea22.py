# Determinar si un numero es o no es primo 

num1 = int(input("Digite el numero: "))
j=0
for i in range(1, num1 + 1): 
    if num1%i==0: 
        j=j + 1
if j==2: 
    print('Es primo')
else: 
    print('no es primo')

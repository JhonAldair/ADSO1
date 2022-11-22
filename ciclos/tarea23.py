#Determinar si un número es o no es perfecto.

num1=int(input('Digite el numero: '))
i=1 
j=0
while(i<num1):
    if num1%i==0:
        j=j+i 
    i=i+1 
if j==num1: 
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")
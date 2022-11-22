#Determinar si un número es o no es perfecto.
def perfe():
    num1=int(input('Digite el numero: '))
    i=1 
    j=0
    while(i<num1):
        if num1%i==0:
            j=j+i 
        i=i+1 
    if j==num1: 
        return("El numero es perfecto")
    return("El numero no es perfecto")
print(perfe())
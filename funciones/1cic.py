##Determinar los divisores de un número introducido por teclado 
def divi():
    num1=int(input('divisores de un numero:'))
    i=1
    while(num1>=i):
        if num1%i==0:
            return(i)
        i+=1
print(divi())
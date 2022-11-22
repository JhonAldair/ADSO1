#Algoritmo para hallar el m.c.d de dos números m y n por
#el algoritmo de Euclides.

num1=int(input('primer numero: '))
num2=int(input('segundo numero: '))
while num2 != 0:
    a=num1
    b=num2
    if num1<0:
        num1=a
        num2=b
    if num2<0:
        num1=a
        num2=-b
    else:
        num1=b
        num2=a%b
print(num1) 
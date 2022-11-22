#Solicitar 2 números al usuario e imprimir el cociente y el
#residuo del mayor en el menor sin utilizar la división ni el mod. 

num1=int(input('ingrese el primer numero:'))
num2=int(input('ingrese el segundo numero: '))
num3=num1
cont=0
if num2>num1:
    num1=num2
    num2=num3
while num1>num2:
    num1-=num2
    cont+=1
print('el cociente es:',cont,'y el residuo es:',num1)

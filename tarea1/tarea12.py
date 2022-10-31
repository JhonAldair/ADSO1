#Escribe un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos

num1 = int(input('ingrese el primer numero:'))
num2 = int(input('ingrese el segundo numero:'))
num3 = int(input('ingrese el tercer numero:'))

if num1 == num2 == num3:
    print('los tres numeros son iguales')
elif num1 == num2:
    print('los dos primeros numeros son igaules')
elif num2 == num3:
    print('los dos ultimos numeros son iguales')
elif num1 == num3:
    print('el primero y el ultimo son iguales')
else:
    print('los tres numeros son diferentes')
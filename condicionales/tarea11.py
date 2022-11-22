#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos

num1 = int(input('ingresar primer número '))
num2 = int(input('ingresar segundo número '))
num3 = int(input('ingresar tercer número'))

menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
media = (num1+num2+num3) - menor - mayor
if num1 == num2 == num3:
    print('los numeros son iguales')

else:
    print('el numero medio es ',media)

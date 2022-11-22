#Escribe un programa que pida tres números y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos
def numdis():
    num1 = int(input('ingrese el primer numero:'))
    num2 = int(input('ingrese el segundo numero:'))
    num3 = int(input('ingrese el tercer numero:'))
    if num1 == num2 == num3:
        return('los tres numeros son iguales')
    elif num1 == num2:
        return('los dos primeros numeros son igaules')
    elif num2 == num3:
        return('los dos ultimos numeros son iguales')
    elif num1 == num3:
        return('el primero y el ultimo son iguales')
    else:
        return('los tres numeros son diferentes')
print(numdis())
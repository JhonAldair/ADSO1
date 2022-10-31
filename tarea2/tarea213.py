#Solicitar al usuario un número de hasta 9 dígitos e
#imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576

r=0
n=int(input('ingrese un numero: '))
while n != 0:
    c=n%10
    r=r*10+c
    n //= 10
print(r)
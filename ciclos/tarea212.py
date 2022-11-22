#Escribir un programa que visualice la siguiente figura,
#utilizando ciclos. El usuario decide cuantas líneas quiere
#imprimir
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * *
#* * * * * * * * *

n=int(input('hasta donde quiere ver le triangulo: '))
for i in range(n):
    for _ in range(i+1):
        print('*',end='')
    print('')
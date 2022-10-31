#Calcular todos los números de 3 cifras tales que la suma
#de los cubos de las cifras es igual al valor del número. 

valor=0
for n in range(100,1000):
    valor=n
    u=n%10
    n=n//10
    d=n%10
    n=n//10
    c=n%10
    u**=3
    d**=3
    c**=3
    suma=u+d+c
    if suma == valor:
        print(valor)

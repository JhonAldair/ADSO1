"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Muestre cuales y cuantos son primos"""
def divi():
    num1=vector
    i=1
    while(num1>=i):
        if num1%i==0:
            print(i)
        i+=1
import random
tam=random.randint(10,25)
vector = [round(random.random()*100) for _ in range(tam)]
print(vector.__len__())
a=[]
for i in range(tam):
    if divi()==2:
        a.append(vector[i])
print('la cantidad total de pares fue ',len(a))
print('la suma de los pares es ',a)
"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Encuentre la mediana de los números de la lista"""


import random
random1=[]
rango=random.randint(10,25)
mediana=0
longitud=len(random1)
for _ in range(rango):
    random1.append(round(random.random()*100))
    random1.sort()
    longitud=len(random1)
    if longitud%2>0:
        mediana=random1[longitud//2]
    if longitud%2==0:
        med=random1[longitud//2]
        mad=random1[(longitud//2)-1]
        mediana=((mad+med)//2)
print('la lista es: ',random1)
print(len(random1))
print('la mediana es: ',mediana)
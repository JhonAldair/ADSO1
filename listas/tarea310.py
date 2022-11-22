"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Encuentre la desviación estandar"""


import random
random1=[]
rango=random.randint(10,25)
suma=0
promedio=0
desviacion=0
tamaño2=0
for contador, i in enumerate(range (rango), start=1):
    random1.append(round(random.random()*100))
    suma+=random1[i]
    promedio=suma//contador
    random1.sort()
    tamaño=len(random1)
    tamaño2=tamaño-1
desviacion=(suma-promedio)**2
dividir=desviacion//tamaño2
resultado_final=dividir**0.5
print('la lista es: ',random1)
print('esta es la desviacion estandar: ',resultado_final)
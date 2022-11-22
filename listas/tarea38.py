"""llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Encuentre la moda de los números de la lista"""

"""import random
tam=random.randint(10,25)
vec=[]
vecCant=[]
print(vec)
cont=0
for i in range(len(vec)): 
    cont=0
    for j in vec:    
        if vec[i] == j:
            cont+=1 
    if cont!=0:
        vecCant.append(cont)
mayor=0
pos=0
for i in range(len(vec)):
    if mayor<vecCant[i]:
       mayor=vecCant[i]
for j in range(len(vecCant)):
    if mayor==vecCant[j]:
        print('la moda es ',vec[j])"""


import random
vec=[]
veccant=[]
rango=random.randint(10,25)
for i in range(rango):
    vec.append(round(random.random()*100))
cont=0
for i in range(len(vec)):
    cont=0
    for j in vec:
        if vec[i]==j:
            cont+=1
    if cont!=0:
        veccant.append(cont)
    else:
        veccant.append(0)
print(vec)
mayor=0
for i in range(len(vec)):
    if mayor<veccant[i]:
        mayor=veccant[i]
for j in range(len(veccant)):
    if mayor==veccant[j]:
        a=vec[j]
        z=('el numero que mas se repite es',a,mayor,'veces')
    if mayor==1:
        z=('no hay moda')
print(z)
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)
'''


import random
tam=random.randint(10,25)
veccant=[]
vector = [round(random.random()*100) for _ in range(tam)]
print(vector)
band=False
while not band:
    band=True
    for i in range(len(vector)-1):
        if vector[i]> vector[i+1]:
            aux=vector[i]
            vector[i]=vector[i+1]
            vector[i+1]=aux
            band=False
print('ordenado de menor a mayor ',vector, '\nordenado al reves es: ',vector[::-1])

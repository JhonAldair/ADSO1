'''suma y promedio de la lista'''
import random
tam=random.randint(10,25)
vector=[]
veccant=[]
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
cont=0
var1=0
cant=0
var2=0
mediana=(vector.__len__())/2
for i in range(tam):
    cont+=1
    var1+=vector[i]    
print('la suma de los numeros es ',var1)
print('el promedio es ',var1//len(vector))


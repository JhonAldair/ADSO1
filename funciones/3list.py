'''sacar suma de pares y promedio de los impares'''
def parimpar():
    import random
    tam=random.randint(10,25)
    vector=[]
    for i in range(tam):
        vector.append(round(random.random()*100))
    print(vector)
    a=[]
    b=[]
    cant=0
    var1=0
    var2=0
    for i in range(tam):
        if vector[i]%2==0:
            var1+=vector[i]
            a.append(vector[i])
        else:
            cant+=1
            var2+=vector[i]
            b.append(vector[i])
    print('los pares son',a)
    print('la suma de los pares es ',var1)
    print('los impares son',b)
    print('el promedio de los impares es ',var2//cant)
parimpar()
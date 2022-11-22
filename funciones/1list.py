'''decir si los numeros de la listas son mayor, igual o menor al promedio'''
def masmenos():
    import random
    tam=random.randint(10,25)
    vector = [round(random.random()*100) for _ in range(tam)]
    print(vector)
    var1=0
    for cont, i in enumerate(range(tam), start=1):
        var1+=vector[i]
        prom=var1//cont
    print(vector.__len__())
    print('el promedio es ',prom)
    for n in vector: 
        if n < prom:
            print('el numero',n,' es menor al promedio ')
        if n > prom:
            print('el numero ',n,'es mayor al promedio ')
        else:
            print('el numero ',n,' es igual al promedio')
masmenos()
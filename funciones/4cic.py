#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?
def numper():
    for n in range(1,1000):
        i=1
        contador=0
        while(n>i):
            if n%i==0:
                contador+=i
            i+=1
        if n == contador:
            print(n,'es perfecto') 
(numper())
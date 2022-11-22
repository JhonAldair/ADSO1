#¿Cuáles y cuántos son los números primos comprendidos
# entre 1 y 1000?
def numprim():
    for num1 in range(2,1000):
        i=1
        num2=0
        while num1>=i:
            if num1%i ==0:
                num2+=1
            i+=1
        if num2 <= 2 or num1 <= 1:
            print( num1,'es primo')
numprim()
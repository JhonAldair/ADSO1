def maximo(a):
    b=-99999999999999999
    for i in (a):
        if i>b:
            b=i
    return(b)

def prom(a):
    vacio=0
    for i in (a):
        vacio+=i
    resultado=vacio//(len(a))
    return(resultado)

def perfe(num1):
    i=1 
    j=0
    while(i<num1):
        if num1%i==0:
            j=j+i 
        i=i+1 
    if j==num1: 
        return("El numero es perfecto")
    return("El numero no es perfecto")

def min(a):
    b=99999999999999999
    for i in (a):
        if i<b:
            b=i
    return(b)

def mult(a):
    b=1
    for i in (a):
        b*=i
    return (b)

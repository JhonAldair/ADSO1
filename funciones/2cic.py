# Determinar si un numero es o no es primo 
def primo():
    num1 = int(input("Digite el numero: "))
    j=0
    for i in range(1, num1 + 1): 
        if num1%i==0: 
            j=j + 1
    return 'Es primo' if j==2 else 'no es primo'
print(primo())

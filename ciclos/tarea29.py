#Calcular la operación x n sin utilizar la función pow

num1=int(input('ponga la base;'))
num2=int(input('ponga el exponente;'))
pot=num1
for _ in range(1, num2):
    pot*=num1
if num2<=0:
    pot=1
print(pot)
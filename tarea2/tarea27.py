# Encontrar un número natural n más pequeño tal que la suma
#de los n primeros números naturales (1 + 2 + 3 + 4…..)
#exceda de una cantidad (máximo) introducida por el teclado.
#Es decir cuantos números de la serie de los naturales debo
#sumar para superar el dato máximo. 

data_max=int(input('introduzca un numero de dato maximo: '))
n=0
cont=0
suma=0
while (suma<=data_max):
    n+=1
    suma = sum(range(n+1))
print(n,'es el numero natural minimo requerido para superar el dato maximo')
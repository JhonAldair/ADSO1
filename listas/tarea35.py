'''pedir un numero, si ya esta en la lista, decir en que posicion, si no esta, agregarlo al final'''

import random
rango=random.randint(10,25)
cont=0
posicion=''
vector = [round(random.random()*100) for _ in range(rango)]
print(vector)
numero=int(input('elija el numero: '))
for i in range(rango):
    if numero==vector[i]:
        posicion += f'{str(i)}'
        cont+=1
if cont == 0:
    vector.append(numero)
    print('el numero se agrego al final de la lista')
    print(vector)
elif cont == 1:
    print('el numero de la lista ',numero,'esta una vez y esta en la posicion ',posicion)
else:
    print('el numero de la lista ',numero,'esta ',cont,' veces y esta en las posiciones ',posicion)
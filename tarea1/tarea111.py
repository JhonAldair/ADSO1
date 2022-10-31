#Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la
#hora que será dentro de 1 segundo
hora=int(input('ingrese la hora:'))
min=int(input('ingrese los minutos:'))
seg=int(input('ingrese los segundos:'))+1
if seg<61 and min<60 and hora<13:
    if seg>=59:
        seg=0
        min += 1
    if min>=59:
        min=0
        hora+=1
    if hora>12:
        hora=1
    print('la hora es ',hora,':',min,':',seg)
else:
    print('ingrese un numero correcto')

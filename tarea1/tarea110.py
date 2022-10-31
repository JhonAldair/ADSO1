#Solicite al usuario la hora en formato hh:mm:ss (hora militar, 24 horas). El
#programa debe responder que hora será un segundo después. Ej: ingreso
#11:59:59, el programa responde 12:00:00. 
hora=int(input('ingrese la hora:'))
min=int(input('ingrese los minutos:'))
seg=int(input('ingrese los segundos:'))+1
if seg<61 and min<60 and hora<24:
    if seg>=59:
        seg=0
        min += 1
    if min>=59:
        min=0
        hora+=1
    if hora>23:
        hora=1
    print('la hora es ',hora,':',min,':',seg)
else:
    print('ingrese un numero correcto')

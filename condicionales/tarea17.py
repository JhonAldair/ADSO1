'''7. Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 horas y $5000 por cada hora extra'''

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

if horas_trabajadas > 40:
    horas_extras = horas_trabajadas - 40
    paga = (40*2600) + (horas_extras*5000)
else:
    paga = horas_trabajadas * 2600
    print("El salario semanal recibido en",horas_trabajadas,"horas es COP",paga)

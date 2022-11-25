#funcion cuadratica
import math
while True:
    try:
        z=input('suma o resta?:')
        if z=='suma' or z=='resta':
            a=float(input('ingrese primer numero: '))
            b=float(input('ingrese segundo numero: '))
            c=float(input('ingrese tercer numero; '))
            suma=-b+math.sqrt(b**2-4*a*c)/(2*a)
            resta=-b-math.sqrt(b**2-4*a*c)/(2*a)
            if z=='suma':
                print(suma)
            if z=='resta':
                print(resta)
        else: 
            print('eliga una de las dos opciones')
    except ZeroDivisionError:
        print('no se puede dividir entre cero')
    except ValueError:
        print('no se puede hacer la funcion cuadratica con estos numeros')
            
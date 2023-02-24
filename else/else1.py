def val():
    try:
        numero1=int(input('ingresa primer numero a sumar:'))
        numero2=int(input('ingresa segundo numero:'))
        a=numero1+numero2
    except ValueError:
        return('ingrese un numero valido')
    else:
        return(a)
print(val())

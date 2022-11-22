#Pida un numero al usuario que representa días del año. Diga a que mes del año 
# corresponde así. Si el número es menor o igual a 31 indica que esta en enero, 
# Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
# cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días
def mes():
    num1 = int(input('ingrese los dias del año: '))
    if num1>=1 and num1<=31:
        return('enero')
    elif num1>=32 and num1<=59:
        return('febrero')
    elif num1>=60 and num1<=90:
        return('marzo')
    elif num1>=91 and num1<=120:
        return('abril')
    elif num1>=121 and num1<=151:
        return('mayo')
    elif num1>=152 and num1<=181:
        return('junio')
    elif num1>=182 and num1<=212:
        return('julio')
    elif num1>=213 and num1<=243:
        return('agosto')
    elif num1>=244 and num1<=273:
        return('septiembre')
    elif num1>=274 and num1<=304:
        return('octubre')
    elif num1>=305 and num1<=334:
        return('noviembre')
    elif num1>=335 and num1<=365:
        return('diciembre')
    else:
        return('el numero no es valido')
print(mes())
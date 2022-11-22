#Pida un numero al usuario que representa días del año. Diga a que mes del año 
# corresponde así. Si el número es menor o igual a 31 indica que esta en enero, 
# Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
# cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días

num1 = int(input('ingrese los dias del año: '))

if num1>=1 and num1<=31:
    print('enero')
elif num1>=32 and num1<=59:
    print('febrero')
elif num1>=60 and num1<=90:
    print('marzo')
elif num1>=91 and num1<=120:
    print('abril')
elif num1>=121 and num1<=151:
    print('mayo')
elif num1>=152 and num1<=181:
    print('junio')
elif num1>=182 and num1<=212:
    print('julio')
elif num1>=213 and num1<=243:
    print('agosto')
elif num1>=244 and num1<=273:
    print('septiembre')
elif num1>=274 and num1<=304:
    print('octubre')
elif num1>=305 and num1<=334:
    print('noviembre')
elif num1>=335 and num1<=365:
    print('diciembre')
else:
    print('el numero no es valido')
#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codigo():
    a=input('ingrese palabra:')
    b=int(input('cuantos numeros quiere sumar al cifrado:'))
    for i in a:
        w=(ord(i))
        w=w+b
        print(chr(w),end='')
codigo()

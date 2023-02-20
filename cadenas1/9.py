#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codigo():
    a=input('ingrese palabra:')
    b=int(input('cuantos numeros quiere sumar al cifrado:'))
    for i in a:
        w=(ord(i))
        w=w+b
        print(chr(w),end='')
codigo()

def desencriptado():
    a=input('caul es el codigo:')
    b=int(input('cuantos numeros quiere restar'))
    for i in a:
        w=(ord(i))
        w=w-b
        t=(chr(w))
        print(t,end='')
(desencriptado())

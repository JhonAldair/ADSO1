#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codigo():
    a=input('ingrese palabra:')
    for i in a:
        w=(ord(i))
        w=w+10
        print(chr(w),end='')
codigo()

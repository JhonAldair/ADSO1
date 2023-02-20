#2. Pida una cadena por teclado y diga cual es su valor al sumar sus codigos
def sum():
    a=input('ingrese una palabra:')
    a=(list(a))
    d=0
    b='la suma de los codigos es:'
    for i in a:
        a=ord(i)
        d+=a
    
    return b,d
print(sum())

#4.Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def mayus():
    letra=input('ingrese una palabra:')
    print(letra.capitalize())
    print(letra.lower())
    print(letra.swapcase())
    print(letra.title())
    print(letra.upper())
mayus()

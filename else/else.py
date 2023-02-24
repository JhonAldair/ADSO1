def look():
    list=[1,2,3,4,5,6,7,8,9]
    num1=int(input('que posicion de la lista quiere ver:'))
    try:    
        a=(list[num1])
    except LookupError:
        return('no existe esta posicion en la lista')
    else:
        return(a)
print(look())

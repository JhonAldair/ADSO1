#- Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def tipo():
    a=input('ingrese palabra:')
    if chr(225) in a or chr(233) in a or chr(237) in a or chr(243) in a or chr(250) in a:
        for i in a[-2:]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('aguda')
            else:
                continue
        for i in a[-4:-2]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('grave')
            else:
                continue
        for i in a[-7:-4]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('esdrujula')
            else:
                continue
        for i in a[:-7]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('sobreesdujula')
    else:
        return('esta palabra no tiene tilde')
print(tipo())
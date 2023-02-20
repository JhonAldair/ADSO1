#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def vocal():
    a=input('ingrese palabra:').lower()
    vocal=[]
    cons=[]
    tild=[]
    esp=[]
    for i in a:
        if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
            tild.append(i)
        if chr(98) in i or chr(99) in i or chr(100) in i or chr(102) in i or chr(103) in i   or chr(104) in i or chr(106) in i or chr(107) in i or chr(108) in i or chr(109) in i or chr(110) in i or chr(241) in i or chr(112) in i or chr(113) in i or chr(114) in i or chr(115) in i or chr(116) in i or chr(118) in i or chr(120) in i or chr(121) in i or chr(122) in i:
            cons.append(i)
        if chr(97) in i or chr(101) in i or chr(105) in i or chr(111) in i or chr(117) in i:
            vocal.append(i)
        if chr(32) in i or chr(33) in i or chr(34) in i or chr(35) in i or chr(36) in i or chr(37) in i or chr(38) in i or chr(39) in i or chr(40) in i or chr(41) in i or chr(42) in i or chr(43) in i or chr(44) in i or chr(45) in i or chr(46) in i or chr(47) in i or chr(58) in i or chr(59) in i or chr(60) in i or chr(61) in i or chr(62) in i or chr(63) in i or chr(64) in i or chr(91) in i or chr(92) in i or chr(93) in i or chr(94) in i or chr(95) in i or chr(96) in i or chr(123) in i or chr(124) in i or chr(125) in i or chr(126) in i: 
            esp.append(i)
    print('la palabra tiene,',vocal.__len__(),'vocal(es)\nla palabra tiene',cons.__len__(),'consonante(s)\nla palabra tiene',tild.__len__(),'vocal(es) con tilde\ny tiene',esp.__len__(),'caracteres especiales')    
(vocal())


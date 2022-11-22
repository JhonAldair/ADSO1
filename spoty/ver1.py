musica={
    'la cosa mas bella'
    :{'artista':'eros ramazzoti','duracion':3.00,'genero':'pop'},
    'monotonia'
    :{'artista':'shakira','duracion':2.30,'genero':'regueton'},
    'te felicito'
    :{'artista':'shakira','duracion':3.30,'genero':'regueton'},
    'noche de entierro'
    :{'artista':'wisin y yandel''daddy yankee''zion','duracion':5.00,'genero':'regueton'},
    'flow natural'
    :{'artista':'tito','duracion':5.50,'genero':'regueton'},
    'fatalidad'
    :{'artista':'julio jaramillo','duracion':3.00,'genero':'bolero'}
}
def buscar(musica):
        a=input('ingrese la cancion que quiera buscar: ')
        if a in musica:
            print('la cancion',a,'\nel artista es',musica[a]['artista'],'\nla duracion es',musica[a]['duracion'],'\nel genero es',musica[a]['genero'])
        print('esta cancion no esta en la playlist')
def agregar(musica):
    b=input('ingrese el nombre de la cancion: ')
    c=input('ingrese el artista: ')
    d=input('ingrese la duracion: ')
    e=input('ingrese el genero: ')
    musica.update({b:{'artistas':c,'duracion':d,'genero':e}})
    for esp, en in musica.items():
        print('-',esp,':',en)
def max():
    dur=[]
    for y,x in musica.items():
        duracion=x['duracion'],y
        dur.append(duracion)
        dur.sort()
    print('la cancion con mayor duracion',dur[-1])
def min():
    dur=[]
    for y,x in musica.items():
        duracion=x['duracion'],y
        dur.append(duracion)
        dur.sort()
    print('la cancion con menor duracion',dur[0])
def buscart():
    cancion=input('ingrese el nombre del artista: ')
    for x,y in musica.items():
        if cancion==y['artista']:
            print('la cancion de este artista es: ',x)
def eliminar():
    for esp, en in musica.items():
        print('-',esp,':',en)
    cancion=input('busca la cancion que quieras eliminar')
    if cancion in musica:
        del(musica[cancion])
        for esp, en in musica.items():
            print('-',esp,':',en)
def visu():
        for esp, en in musica.items():
            print('-',esp,':',en)
z=input('presione "1" si quiere ver la informacion de una cancion\nPresione "2" si quiere visualizar la list\nPresione "3" si quiere añadir una cancion\npresione "4" si quiere ver la cancion mas larga\nPresione "5" si quiere ver la lista mas corta\nPresione 6 si quiere buscar las canciones de un artista\nPresione 7 si quiere eliminar una cancion: ')
if z=='1':
    (buscar(musica))
if z=='2':
    visu()
if z=='3':
    (agregar(musica))  
if z=='4':
    (max())
if z=='5':
    min()
if z=='6':
    buscart()
if z=='7':
    (eliminar())    
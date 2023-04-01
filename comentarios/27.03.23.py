import sqlite3                                                          #se importa el paquete sqlite3
#con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\pythondb.db')      
con=sqlite3.connect('pythonsqlite/pythondb.db')                         #se crea un objeto que guarda la coneccion con la base de datos
print(type(con))                                                        #se imprime el objeto de coneccion 
micursor=con.cursor()                                                   #se crea un objeto que guarda a que tabla se quiere modificar en la base de datos (cursor)
print(type(micursor))                                                   #se imprime el objeto cursor
new_sql="SELECT * from Persona;"                                        #se crea una variable con una cadena de texto, la cadena de texto indica que accion queremos hacer en la base de datos
micursor.execute(new_sql)                                               #se ejecuta la accion que queremos hacer llamando a la variable dentro del cursor
lista=micursor.fetchall()                                               #se crea una lista con todos los datos de la lista del cursor
for fila in lista:                                                      #se crea un for que recorrera toda la lista 
    print(fila[0])                                                      #se imprime la primera posicion de la lista
    print(fila[1])                                                      #se imprime la segunda posicionde la lista
    print(fila[2])                                                      #se imprime la tercera posicion de la lista
    print(fila[3])                                                      #se imprime la cuarta posicion de la lista
    print('*'*50)                                                       #se imprimen unos "*" que servira para separar a los datos de cada persona

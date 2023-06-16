import sqlite3

def crear_bd_puntajes()->None:
    with sqlite3.connect("bd_puntajes.db") as conexion:
        try:
            sentencia = ''' create  table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntajes")                       
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")

def insertar_puntajes(nombre:str, puntaje:int)->None:
    with sqlite3.connect("bd_puntajes.db") as conexion:    
        try:
            conexion.execute("insert into puntajes(nombre,puntaje) values (?,?)", (nombre, puntaje)) 
            conexion.commit()
        except:
            print("Error al escribir la tabla")

def pedir_top_puntajes()->list:
    with sqlite3.connect("bd_puntajes.db") as conexion:
        try:
            cursor = conexion.execute("select * from puntajes order by puntaje desc limit 10")
            lista = cursor.fetchall()
            #print(lista)
        except:
            print("Error de registros")
            lista = []

        return lista
    
    
def eliminar_puntajes()->None:
    lista = pedir_top_puntajes(11)
    if len(lista) > 10:
        puntaje_minimo = lista[9][2]
        with sqlite3.connect("bd_puntajes.db") as conexion:
            try:
                cursor = conexion.execute("delete * from puntajes where puntaje < ?", (puntaje_minimo))
            except:
                print("Error al borrar registros")
    


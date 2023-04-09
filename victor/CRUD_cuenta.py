import sqlite3

with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar_cuenta(c, id_cue, id_usu, id_ser, costo_ext):
    sentencia=f"INSERT INTO 'cuenta' ('id_cue', 'id_usu', 'id_ser', 'costo_ext') VALUES ('{id_cue}','{id_usu}','{id_ser}','{costo_ext}',)"
    c.execute(sentencia)
    a.commit()
    print('La cuenta ha sido agrgada exitosamente')

def consultar_cuenta(c, Id):
    sentencia=f"SELECT * FROM 'cuenta' WHERE id_cue='{Id}'"
    x=c.execute(sentencia)
    for fila in x.fetchall():
        print('id de la cuenta:',fila[0])
        print('id del usuario:',fila[1])
        print('id del servicio:',fila[2])
        print('cuenta total:',fila[3])

def eliminar_cuenta(c, Id):
    sentencia=f"DELETE FROM 'cuenta' WHERE id_cue='{Id}'"
    c.execute(sentencia)
    a.commit()
    print('La cuenta ha sido eliminada con exito')

def modificar_cuenta(c, Id, cuenta):
    sentencia=f"UPDATE 'cuenta' SET costo_ext = '{cuenta}' WHERE id_cue = '{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')


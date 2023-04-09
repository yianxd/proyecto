import sqlite3

with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar_reserva(c, id_res, id_hab, fecha_lleg, fecha_sal, id_usu ):
    sentencia=f"INSERT INTO 'reserva' ('id_res', 'id_hab', 'fecha_lleg', 'fecha_sal', 'id_usu') VALUES ('{id_res}','{id_hab}','{fecha_lleg}','{fecha_sal}','{id_usu}')"
    c.execute(sentencia)
    a.commit()
    print('Su reserva ha sido agragada exitosamente')

def consultar_reserva(c, Id):
    sentencia=f"SELECT * FROM 'reserva' WHERE id_hab='{Id}'"
    b=c.execute(sentencia)
    for fila in b.fetchall():
        print('ID reserva: ',fila[0])
        print('ID habitacion:',fila[1])
        print('ID usuario:',fila[2])
        print('Fecha de llegada:',fila[3])
        print('Fecha de salida:',fila[4])

def eliminar_reservas(c, codigo):
    sentencia=f"DELETE FROM 'reserva' WHERE id_res='{codigo}'"
    c.execute(sentencia)
    a.commit()
    print('La reserva se ha eliminado exitosamente')

def modificar_llegada(c, id, fecha):
    sentencia=f"UPDATE 'reserva' SET fecha_lleg = '{fecha}' WHERE id_res = '{id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')

def modificar_salida(c, id, fecha):
    sentencia=f"UPDATE 'reserva' SET fecha_sal = '{fecha}' WHERE id_res = '{id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')


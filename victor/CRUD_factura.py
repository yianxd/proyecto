import sqlite3

with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar_factura(c, id_fac, id_cue, total_fac):
    sentencia=f"INSERT INTO 'factura' ('id_fac', 'id_cue', 'total_fac') VALUES ('{id_fac}','{id_cue}','{total_fac}',)"
    c.execute(sentencia)
    a.commit()
    print('La factura ha sido agragada exitosamente')

def consultar_factura(c, Id):
    sentencia=f"SELECT * FROM 'cuenta' WHERE id_fac='{Id}'"
    b=c.execute(sentencia)
    for fila in b.fetchall():
        print('id de la factura:',fila[0])
        print('id de la cuenta:',fila[1])
        print('total de la factura:',fila[2])

def eliminar_facturas(c, Id):
    sentencia=f"DELETE FROM 'factura' WHERE id_fac='{Id}'"
    c.execute(sentencia)
    a.commit()
    print('La factura se ha eliminado exitosamente')

def modificar_total(c, Id, total):
    sentencia=f"UPDATE 'factura' SET total_fac = '{total}' WHERE id_fac = '{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')
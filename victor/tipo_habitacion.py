import sqlite3

with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agragar_tipo(c, id_tha, tipo_tha):
    sentencia=f"INSET INTO 'tipo_habitacion ('id_tha', 'tipo_tha')' VALUES ('{id_tha}','{tipo_tha}')"
    c.execute(sentencia)
    a.commit()
    print('Su tipo de habitacion ha sido agragada exitosamente')

def consultar_tipo(c, Id):
    sentencia=f"SELECT * FROM 'tipo_habitacion' WHERE id_tha='{Id}'"
    b=c.execute(sentencia)
    for fila in b.fetchall():
        print('id del tipo de habitacion:',fila[0])
        print('tipo de habitacion:',fila[1])

def eliminar_tipo(c, Id):
    sentencia=f"DELETE FROM 'tipo_habitacion' WHERE id_tha='{Id}'"
    c.execute(sentencia)
    a.commit()
    print('El tipo de habitacion se ha eliminado exitosamente')

def modificar_tipo(c, Id, tipo):
    sentencia=f"UPDATE 'tipo_habitacion' SET tipo_tha = '{tipo}' WHERE id_tha='{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')
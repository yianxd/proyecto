import sqlite3 
with sqlite3.connect('proyecto.db') as con:
    cursor=con.cursor()

def agregar(conexion,id_tip,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
    cur=conexion.cursor()
    sentencia=f"INSERT INTO usuarios (id_tip,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu) VALUES ({id_tip},'{nombre_usu}','{apellido_usu}','{email_usu}','{telefono_usu}','{direccion_usu}','{contraseña_usu}')"
    cur.execute(sentencia)
    print("registro logrado con exito!")
    sentencia=f"SELECT * FROM usuarios WHERE telefono_usu='{telefono_usu}'"
    print(cur.execute(sentencia).fetchone())
    

# agregar(con, 1, "juan", "calles", "adsf@gmail.com", "343-134-334", "paaaaaaa", "AKj123")
"""plantilla:
    cur=conexion.cursor()
    sentencia=f""
    cur.execute(sentencia)
"""
def eliminar(conexion,campo,operador,dato):
    cur=conexion.cursor()
    sentencia=f"DELETE FROM usuarios WHERE '{campo}'='{dato}'"
    cur.execute(sentencia)
    conexion.commit()
    print("se elimino con exito")

#eliminar(con, "id_usu", "=", "52")

def actualizar(conexion,campo,dato,condicion,dato2):
    cur=conexion.cursor()
    sentencia=f"UPDATE usuarios SET '{campo}'='{dato}' WHERE {condicion}='{dato2}'"
    cur.execute(sentencia)
    conexion.commit()
    print("se actualizo con exito")


actualizar(con, "nombre_usu", "no se", "id_usu", 2)

def consultarTodo(conexion):
    cur=conexion.cursor()
    sentencia=f"SELECT * FROM USUARIOS"
    print(cur.execute(sentencia).fetchall())

def consultar(conexion,condicion,condicion2,condicion3):
    cur=conexion.cursor()
    sentencia=f"SELECT * FROM usuarios WHERE {condicion}{condicion2}'{condicion3}'"
    print(cur.execute(sentencia).fetchall())


consultar(con,'id_usu','>','27')
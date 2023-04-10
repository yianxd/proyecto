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


#agregar(con, input("ingrese el numero del tipo de usuario: "), input("ingrese el nombre: "), input("ingrese apellido: "), input("ingrese el email: "), input("ingrese el telefono "), input("ingrese direccion: "), input("ingrese una contraseña: "))
"""plantilla:
    cur=conexion.cursor()
    sentencia=f""
    cur.execute(sentencia)
"""
def eliminar(conexion,campo,operador,dato):
    cur=conexion.cursor()
    sentencia=f"DELETE FROM usuarios WHERE {campo}{operador}'{dato}'"
    cur.execute(sentencia)
    conexion.commit()
    print("se elimino con exito")

#eliminar(con, input("ingrese la campo de referencia: "), input("ingrese un operador, pero si el anterior campo es texto use el =,si no cualquier otro"), input("ingrese el dato de referencia"))

def actualizar(conexion,campo,dato,condicion,dato2):
    cur=conexion.cursor()
    sentencia=f"UPDATE usuarios SET '{campo}'='{dato}' WHERE {condicion}='{dato2}'"
    cur.execute(sentencia)
    conexion.commit()
    print("se actualizo con exito")


#actualizar(con, input("ingrese el campo donde se va actualizar: "),input("ingrese el nuevo dato: "), input("Ingrese el campo de referencia: "), input("ingrese un dato de referencia: "))

def consultarTodo(conexion):
    cur=conexion.cursor()
    sentencia=f"SELECT * FROM USUARIOS"
    print(cur.execute(sentencia).fetchall())
#consultarTodo(con)
def consultar(conexion,condicion,condicion2,condicion3):
    cur=conexion.cursor()
    sentencia=f"SELECT * FROM usuarios WHERE {condicion}{condicion2}'{condicion3}'"
    print(cur.execute(sentencia).fetchall())
#consultar(con,input("ingrese nombre de la tabla "),input(ingrese un operador),input("ingrese un valor"))
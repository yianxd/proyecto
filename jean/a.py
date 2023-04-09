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
    

agregar(con, 1, "juan", "calles", "adsf@gmail.com", "343-134-334", "paaaaaaa", "AKj123")
#DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def eliminar(conexion,condicion1,operador,condicion2):
    print("terminar esto")
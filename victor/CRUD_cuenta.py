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

def consultar_todo(c):
    sentencia=f"SELECT * FROM 'cuenta'"
    p=c.execute(sentencia)
    for fila in p.fetchall():
        print('id de la cuenta:',fila[0])
        print('id del usuario:',fila[1])
        print('id del servicio:',fila[2])
        print('cuenta total:',fila[3])

def eliminar_cuenta(c, Id):
    sentencia=f"DELETE FROM 'cuenta' WHERE id_cue='{Id}'"
    c.execute(sentencia)
    a.commit()
    print('La cuenta ha sido eliminada con exito')

def modificar_Extra(c, Id, Extra):
    sentencia=f"UPDATE 'cuenta' SET costo_ext = '{Extra}' WHERE id_cue = '{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')

def menu_cuenta():

    print("Bienvenido al menu de la cuenta en que le podemos colaborar? ")
    while True:
        print("1. Agregar una cuenta")
        print("2. Consultar una cuenta")
        print("3. Eliminar una cuenta")
        print("4. Modificar el costo Extra")
        print("5. Salir")
        eleccion=int(input("Seleccione la opcion: "))


        if eleccion == 1:
            archivo=open("historial_res.csv","a")
            id_cue=int(input("Ingrese el Id de la cuenta"))
            id_usu=int(input("Ingrese el ide del usuario"))
            id_ser=int(input("Ingrese el id del servicio"))
            costo_ext=int(input("Ingrese el costo extra"))
            archivo.write("Agregacion\n")
            archivo.write("Id de la cuenta: ",id_cue,"\n")
            archivo.write("Id del usuario: ",id_usu,"\n")
            archivo.write("Id del servicio: ",id_ser,"\n")
            archivo.write("Ingrese el costo extra: ",costo_ext,"\n")
            archivo.close()
            agregar_cuenta(c, id_cue, id_usu, id_ser, costo_ext)


        elif eleccion == 2:
            while True:
                print("1. Consultar una cuenta")
                print("2. Consultar todo")
                print("3. salir")
                opcion=int(input("Escriba el numero de su eleccion: "))

                if opcion == 1:
                    Id= int(input("Escriba el id de la cuenta: "))
                    consultar_cuenta(c,Id)

                elif opcion == 2:
                    consultar_todo(c)

                elif opcion == 3:
                    menu_cuenta()

        elif eleccion == 3:
            archivo= open("historial_res.csv","a")
            Id=int(input("Escriba la Id de la cuenta la cualquiere eliminar: "))
            archivo.write("Eliminacion de cuenta")
            archivo.write("Id: ",Id,"\n")
            archivo.close()
            eliminar_cuenta(c, Id)

        elif eleccion == 4:
            archivo=open("historial_res.csv","a")
            Id=int(input("Escriba el Id e la cuenta la cual va a modificar: "))
            Extra=int(input("Escriba el nuevo Extra: "))
            archivo.write("Modificacion de el Extra")
            archivo.write("id: ",Id,",")
            archivo.write("Extras costos: ",Extra,"\n")
            archivo.close()
            modificar_Extra(c, Id, Extra)

        elif eleccion == 5:
            exit()

menu_cuenta()

    
    


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

def consultar_todo(c):
    sentencia=f"SELECT * FROM 'reservas'"
    p=c.execute(sentencia)
    for fila in p.fetchall():
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


def modificar_llegada(c, Id, fecha):
    sentencia=f"UPDATE 'reserva' SET fecha_lleg = '{fecha}' WHERE id_res = '{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')


def modificar_salida(c, Id, fecha):
    sentencia=f"UPDATE 'reserva' SET fecha_sal = '{fecha}' WHERE id_res = '{Id}'"
    c.execute(sentencia)
    a.commit()
    print('Actualizacion completada con exito')


def menu_reservas():

    print("Bienvenido al menu de reservas e que le podemos colaborar?")
    while True:
        print("1. Agregar una reserva")
        print("2. Consultar una reserva")
        print("3. Eliminar una reserva")
        print("4. Modificar la fecha de llegada")
        print("5. Modificar la fecha de salida")
        print("6. Salir")
        eleccion=int(input("Seleccione una opcion: "))

        if eleccion == 1:
            archivo=open("historial_res.csv","a")
            id_res=int(input("Ingrese el id de la reserva"))
            id_hab=int(input("Ingrese el id de la habitacion"))
            fecha_lleg=int(input("Ingrese la fecha en la que empezara su estadia"))
            fecha_sal=int(input("Ingrese la fecha en la que terminara su estadia"))
            id_usu=int(input("Ingrese el id del usuario"))
            archivo.write("Agregacion\n")
            archivo.write("Id reserva: ")
            archivo.write(str(id_res))
            archivo.write("\n")
            archivo.write("Id de la habitacion: ")
            archivo.write(str(id_hab))
            archivo.write("\n")
            archivo.write("Fecha de llegada: ")
            archivo.write(str(fecha_lleg))
            archivo.write("\n")
            archivo.write("Fecha de salida: ")
            archivo.write(str(fecha_sal))
            archivo.write("\n")
            archivo.write("Id del usuario: ")
            archivo.write(str(id_usu))
            archivo.write("\n")
            archivo.close()
            agregar_reserva(c, id_res, id_hab, fecha_lleg, fecha_sal, id_usu)


        elif eleccion == 2:
            while True:
                print("1. Consultar un registro")
                print("2. Consultar todo")
                print("3. salir")
                opcion=int(input("Escriba el numero de su eleccion: "))

                if opcion == 1:
                    Id= int(input("Escriba el id de la reserva: "))
                    consultar_reserva(c,Id)

                elif opcion == 2:
                    consultar_todo(c)

                elif opcion == 3:
                    menu_reservas()


        elif eleccion == 3:
            archivo= open("historial_res.csv","a")
            codigo=int(input("Escriba la Id de la reserva la cualquiere eliminar: "))
            archivo.write("Eliminacion de reserva")
            archivo.write("Id: ",codigo,"\n")
            archivo.write(str(codigo))
            archivo.write("\n")
            archivo.close()
            eliminar_reservas(c, codigo)

        elif eleccion == 4:
            archivo=open("historial_res.csv","a")
            Id=int(input("Escriba el Id e la reserva la cual va a modificar: "))
            fecha=int(input("Escriba la nueva fecha de llegada: "))
            archivo.write("Modificacion de el dia de llegada")
            archivo.write("id: ")
            archivo.write(str(Id))
            archivo.write("\n")
            archivo.write("Fecha_llegada: ")
            archivo.write(str(fecha))
            archivo.write("\n")
            archivo.close()
            modificar_llegada(c, Id, fecha)

        elif eleccion == 5:
            archivo=open("historial_res.csv","a")
            Id=int(input("Escriba el Id e la reserva la cual va a modificar: "))
            fecha=int(input("Escriba la nueva fecha de salida: "))
            archivo.write("Modificacion de el dia de salida")
            archivo.write("id: ")
            archivo.write(str(Id))
            archivo.write("\n")
            archivo.write("Fecha_llegada: ")
            archivo.write(str(fecha))
            archivo.write("\n")
            archivo.close()
            modificar_salida(c, Id, fecha)

        elif eleccion == 6:
            exit()

menu_reservas()


                






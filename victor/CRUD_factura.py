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

def consultar_todo(c):
    sentencia=f"SELECT * FROM 'cuenta'"
    p=c.execute(sentencia)
    for fila in p.fetchall():
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

def menu_cuenta():

    print("Bienvenido al menu de la cuenta en que le podemos colaborar? ")
    while True:
        print("1. Agregar una factura")
        print("2. Consultar una factura")
        print("3. Eliminar una factura")
        print("4. Modificar el total")
        print("5. Salir")
        eleccion=int(input("Seleccione la opcion: "))

        if eleccion == 1:
            archivo=open("historial_res.csv","a")
            id_fac=int(input("Ingrese el Id de la factura"))
            id_cue=int(input("Ingrese el Id de la cuenta"))
            total_fac=int(input("Ingrese el total de la factura"))
            archivo.write("Agregacion\n")
            archivo.write("Id factura: ",id_fac,"\n")
            archivo.write("Id cuenta: ",id_cue,"\n")
            archivo.write("Total a pagar: ",total_fac,"\n")
            archivo.close()
            agregar_factura(c, id_fac, id_cue, total_fac)


        elif eleccion == 2:
            while True:
                print("1. Consultar una factura")
                print("2. Consultar todo")
                print("3. salir")
                opcion=int(input("Escriba el numero de su eleccion: "))

                if opcion == 1:
                    Id= int(input("Escriba el id de la factura: "))
                    consultar_factura(c,Id)

                elif opcion == 2:
                    consultar_todo(c)

                elif opcion == 3:
                    menu_cuenta()


        elif eleccion == 3:
            archivo= open("historial_res.csv","a")
            Id=int(input("Escriba la Id de la factura la cualquiere eliminar: "))
            archivo.write("Eliminacion de factura")
            archivo.write("Id: ",Id,"\n")
            archivo.close()
            eliminar_facturas(c, Id)

        
        elif eleccion == 4:
            archivo=open("historial_res.csv","a")
            Id=int(input("Escriba el Id e la cuenta la cual va a modificar: "))
            total=int(input("Escriba el nuevo total: "))
            archivo.write("Modificacion de el total")
            archivo.write("id: ",Id,",")
            archivo.write("Fecha_llegada: ",total,"\n")
            archivo.close()
            modificar_total(c, Id, total)


        elif eleccion == 5:
            exit()

menu_cuenta()
          
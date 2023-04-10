import sqlite3

with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar_tipo(c, id_tha, tipo_tha):
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

def menu_tipohabitacion():

    print("Bienvenido al menu de el tipo de habitacion en que le podemos colaborar? ")
    while True:
        print("1. Agregar una tipo")
        print("2. Consultar un tipo")
        print("3. Eliminar un tipo")
        print("4. Modificar el tipo")
        print("5. Salir")
        eleccion=int(input("Seleccione la opcion: "))

        if eleccion == 1:
            archivo=open("historial_tipohab.csv","a")
            id_tha=int(input("Ingrese el Id de el tipo de habitacion"))
            tipo_tha=int(input("Ingrese el tipo de habitacion"))
            archivo.write("Agregacion\n")
            archivo.write("Id factura: ")
            archivo.write(str(id_tha))
            archivo.write("\n")
            archivo.write("Tipo de habitacion: ")
            archivo.write(str(tipo_tha))
            archivo.write("\n")
            archivo.close()
            agregar_tipo(c, id_tha, tipo_tha)


        elif eleccion == 2:
            Id= int(input("Escriba el id de la factura: "))
            consultar_tipo(c,Id)

        elif eleccion == 3:
            archivo= open("historial_tipohab.csv","a")
            Id=int(input("Escriba la Id de el tipo de habitacion el cual quiere eliminar: "))
            archivo.write("Eliminacion de el tipo de habitacion")
            archivo.write("Id: ")
            archivo.write(str(Id))
            archivo.write("\n")
            archivo.close()
            eliminar_tipo(c, Id)

        elif eleccion == 4:
            archivo=open("historial_tipohab.csv","a")
            Id=int(input("Escriba el Id de el tipo de habitacion cual va a modificar: "))
            tipo=int(input("Escriba el nuevo tipo de habitacion: "))
            archivo.write("Modificacion de el tipo de habitacion")
            archivo.write("Id factura: ")
            archivo.write(str(id_tha))
            archivo.write("\n")
            archivo.write("Tipo de habitacion: ")
            archivo.write(str(tipo_tha))
            archivo.write("\n")
            archivo.close()
            modificar_tipo(c, Id, tipo)

        elif eleccion == 5:
            exit()

menu_tipohabitacion()
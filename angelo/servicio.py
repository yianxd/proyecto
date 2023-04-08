import sqlite3
ñ=50*"_"
with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar(c,tipo_ser,costo_ser):
    sentecia=f"INSERT INTO 'servicios' ('tipo_ser', 'costo_ser') VALUES ('{tipo_ser}','{costo_ser}');"
    c.execute(sentecia)
    a.commit()
    print('Agregacion exitosa')

    
def consultaruno(c,id_ser):
    sentencia=f"SELECT * FROM 'servicios' WHERE id_ser='{id_ser}'"
    print(ñ)
    x=c.execute(sentencia)
    for fila in x.fetchall():
        print("ID: *",fila[0])
        print("tipo de servicio: ",fila[1])
        print("costo: ",fila[2])
    print(ñ)


def consultartodo(c):
    sentencia=f"SELECT * FROM 'servicios'"
    p=c.execute(sentencia)
    for fila in p.fetchall():
        print(ñ)
        print("ID: *",fila[0])
        print("Tipo de servicio: ",fila[1])
        print("Cost : ",fila[2])
        print(ñ)
    

def modificartipo(c,tipo_ser,id_ser):
    sentencia=f"UPDATE 'servicios' SET tipo_ser = '{tipo_ser}' WHERE id_ser='{id_ser}'"
    c.execute(sentencia)
    a.commit()
    print('Modificación del tipo de servicio fue un exito')
        

def modificarcos(c,id_ser,costo_ser):
    sentencia=f"UPDATE 'servicios' SET costo_ser ='{costo_ser}' WHERE id_ser='{id_ser}'"
    c.execute(sentencia)
    a.commit()
    print('Modificación de costo de servicio fue un exito')
        

def modificartodo(c,id_ser,tipo_ser,costo_ser):
    sentencia=f"UPDATE 'servicios' SET tipo_ser = '{tipo_ser}' WHERE id_ser='{id_ser}'"
    sentencia2=f"UPDATE 'servicios' SET costo_ser ='{costo_ser}' WHERE id_ser='{id_ser}'"
    c.execute(sentencia)
    c.execute(sentencia2)
    a.commit()
    print('Modificación exitosa')


def eliminar(c,id_ser):
    sentencia=f"DELETE FROM 'servicios' WHERE id_ser='{id_ser}'"
    c.execute(sentencia)
    a.commit()
    print('Eliminación con exito')

def menuservicio():
    print("Bienvenido Al Menu de servicios porfavor ingrese un numero para continuar :)")
    while True:
        print("1. Agregar servicios")
        print("2. Consultar servicios")
        print("3. Modificar servicios")
        print("4. Eliminar servicios")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))


        if opcion == 1:
            tipo_ser=input("Ingrese el tipo de servicio: ")
            costo_ser=int(input("Ingresa el costo del servicio: "))
            agregar(c,tipo_ser,costo_ser)


        elif opcion == 2:
            while True:
                print("1. Consultar un servicio")
                print("2. Consultar todo los servicios")
                print("3. Atras")
                op=int(input("Seleccione una opción: "))
                if op == 1:
                    id_ser = int(input("Ingrese la id del servicio: "))
                    consultaruno(c,id_ser)
                elif op == 2:
                    consultartodo(c)
                elif op == 3:
                    menuservicio()

    
        elif opcion == 3:
            while True:
                print("1. Modificar tipo de servicio")
                print("2. Modificar costo del servicio")
                print("3. modificar tipo de servicio y costo")
                print("4. Atras")
                opcion1=int(input("Seleccione una opción: "))
                if opcion1 == 1:
                    id_ser=int(input("Ingrese el id: "))
                    tipo_ser=input("Ingrese el tipo de servicio: ")
                    modificartipo(c,tipo_ser,id_ser)
                elif opcion1 == 2:
                    id_ser=int(input("Ingrese el id: "))
                    costo_ser=int(input("Ingrese el costo del servicio: "))
                    modificarcos(c,id_ser,costo_ser)
                elif opcion1 == 3:
                    id_ser=int(input("Ingrese el id: "))
                    tipo_ser=input("Ingrese el tipo de servicio: ")
                    costo_ser=int(input("Ingrese costo de servicio: "))
                    modificartodo(c,id_ser,tipo_ser,costo_ser)
                elif opcion1 == 4:
                    menuservicio()


        elif opcion == 4:
            id_ser=int(input("ingrese la id que va a eliminar: "))
            eliminar(c,id_ser)
    
    
        elif opcion == 5:
            exit()
menuservicio()
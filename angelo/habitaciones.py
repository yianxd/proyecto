import sqlite3
ñ=50*"_"
with sqlite3.connect('proyecto.sqbpro') as a:
    c=a.cursor()

def agregar(c,tipo_tha,descripcion_hab):
    sentecia=f"INSERT INTO 'habitaciones' ('tipo_tha', 'descripcion_hab') VALUES ({tipo_tha},'{descripcion_hab}');"
    c.execute(sentecia)
    a.commit()
    print('Agregacion exitosa')

    
def consultaruno(c,dato):
    sentencia=f"SELECT * FROM 'habitaciones' WHERE id_hab='{dato}'"
    print(ñ)
    x=c.execute(sentencia)
    for fila in x.fetchall():
        print("ID: *",fila[0])
        print("tipo habitacion: ",fila[1])
        print("descricion : ",fila[2])
    print(ñ)


def consultartodo(c):
    sentencia=f"SELECT * FROM 'habitaciones'"
    p=c.execute(sentencia)
    for fila in p.fetchall():
        print(ñ)
        print("ID: *",fila[0])
        print("tipo habitacion: ",fila[1])
        print("descricion : ",fila[2])
        print(ñ)
    

def modificartipo(c,tipo,id):
    sentencia=f"UPDATE 'habitaciones' SET tipo_tha = {tipo} WHERE id_hab='{id}'"
    c.execute(sentencia)
    a.commit()
    print('Modificación del tipo de habitacion fue un exito')
        

def modificardes(c,id,descripcion):
    sentencia=f"UPDATE 'habitaciones' SET descripcion_hab ='{descripcion}' WHERE id_hab='{id}'"
    c.execute(sentencia)
    a.commit()
    print('Modificación de descripcion fue un exito')
        

def modificartodo(c,id,tipo,descripcion):
    sentencia=f"UPDATE 'habitaciones' SET tipo_tha = {tipo} WHERE id_hab='{id}'"
    sentencia2=f"UPDATE 'habitaciones' SET descripcion_hab ='{descripcion}' WHERE id_hab='{id}'"
    c.execute(sentencia)
    c.execute(sentencia2)
    a.commit()
    print('Modificación exitosa')


def eliminar(c,id):
    sentencia=f"DELETE FROM 'habitaciones' WHERE id_hab='{id}'"
    c.execute(sentencia)
    a.commit()
    print('Eliminación con exito')

def menuhabitacion():

    print("Bienvenido Al Menu de habitaciones porfavor ingrese un numero para continuar :)")
    while True:
        print("1. Agregar habitacion")
        print("2. Consultar habitaciones")
        print("3. Modificar habitaciones")
        print("4. Eliminar habitaciones")
        print("5. historial")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))


        if opcion == 1:
            archivo= open("historial_hab.csv","a")
            tipo_tha= int(input("Ingrese el tipo de habitacion:\n1. simple\n2. doble\n3. tiple\n4. matrimonial\n= ")) 
            descripcion_hab=input("Ingrese la descripcion de la habitacion: ")
            archivo.write("Agregaron\n")
            archivo.write("tipo de habitacion: ",tipo,"\n")
            archivo.close()
            agregar(c,tipo_tha,descripcion_hab)


        elif opcion == 2:
            while True:
                print("1. Consultar un solo registro")
                print("2. Consultar todo los registro")
                print("3. Atras")
                op=int(input("Seleccione una opción: "))
                if op == 1:
                    id = int(input("Ingrese la id de la habitacion: "))
                    consultaruno(c,id)
                elif op == 2:
                    consultartodo(c)
                elif op == 3:
                    menuhabitacion()

    
        elif opcion == 3:
            while True:
                print("1. Modificar tipo de habitacion")
                print("2. Modificar descripcion")
                print("3. modificar tipo de habitacion y descripcion")
                print("4. Atras")
                opcion1=int(input("Seleccione una opción: "))
                if opcion1 == 1:
                    archivo= open("historial_hab.csv","a")
                    id=int(input("Ingrese el id: "))
                    tipo=int(input("Ingrese el tipo de habitacion:\n1. simple\n2. doble\n3. tiple\n4. matrimonial\n= "))
                    archivo.write("modificaron tipo de habitacion\n")
                    archivo.write("id: ",id,",")
                    archivo.write("tipo de habitacion: ",tipo,"\n")
                    archivo.close()
                    modificartipo(c,tipo,id)
                elif opcion1 == 2:
                    archivo=open("historial_hab","a")
                    id=int(input("Ingrese el id: "))
                    descripcion=input("Ingrese descripcion de la habitacion: ")
                    archivo.write("Modificaron descripcion de la habitacion\n")
                    archivo.write("id: ",id,",")
                    archivo.write("descripcion: ",descripcion,"\n")
                    archivo.close()
                    modificardes(c,id,descripcion)
                elif opcion1 == 3:
                    archivo=open("historial_hab","a")
                    id=int(input("Ingrese el id: "))
                    tipo=int(input("Ingrese el tipo de habitacion:\n1. simple\n2. doble\n3. tiple\n4. matrimonial\n= "))
                    descripcion=input("Ingrese descripcion de la habitacion: ")
                    archivo.write("Modificaron un registro\n")
                    archivo.write("id: ",id,",")
                    archivo.write("descripcion: ",descripcion,"\n")
                    archivo.close()
                    modificartodo(c,id,tipo,descripcion)
                elif opcion1 == 4:
                    menuhabitacion()


        elif opcion == 4:
            archivo= open("historial_hab.csv","a")
            id=int(input("ingrese la id que va a eliminar: "))
            archivo.write("Eliminaron registro")
            archivo.write("id: ",id,"\n")
            archivo.close()
            eliminar(c,id)
    
        elif opcion == 5:
            while True:
                print("1. Ver todo el historial")
                print("2. Eliminar historial")
                print("3. Atras")
                opcional=int(input("Selecione una opcion: "))
                if opcional==1:
                    archivo= open("historial_hab.csv")
                    archivo.read()
                    archivo.close()
                elif opcional==2: 
                    archivo= open("historial_hab.csv","a")
                    archivo.truncate()
                    print("Eliminaste el historial")
                    archivo.close()
                elif opcional==3:
                    menuhabitacion()   


        elif opcion == 6:
            exit()
menuhabitacion()
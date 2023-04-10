from angelo import habitacione,servicio
from victor import CRUD_cuenta,CRUD_factura,CRUD_resrvas,CRUD_tipo_habitacion
from jean import a
import sqlite3

print("--Bienvenido de prueba---\n actualmente no contamos con un algoritmo que pueda validar los usuarios en el sistema, asi que le daremos estos usuarios para que los pruebe:)")
print("Administador: \n usuario: admin1032 \n contraseña: 1023 \nRecepcionita: \n  usuario: rec4301 \n contraseña:4312 \nCliente \n usuario: usu131 \n contraseña: 1235  ")
cuentas=["admin1032","1023","rec4301","4312","usu131","1235"]
print("por favor ingresar el usuario y la contraseña para continuar")
entrada=input("Usuario: ")
entrada3=0
while True:
    match entrada:
     case "admin1032": #comentario para entender donde comienza cada menu
        with sqlite3.connect('proyecto.db') as con:
            while True:
                entrada=input("ingrese su contraseña: ")
                if entrada in cuentas:
                    print("Acciones a realizar: \n1.Gestionar usuarios\n2.Gestionar habitaciones\n3.Gestionar servicios\n4.Cancelar reservas\n5.Revisar cuentas\n6.Revisar facturas")
                    entrada2=int(input())
                    match entrada2:
                        case 1:
                            print("--Gestionar usuarios \n1.Agregar un nuevo usuario \n2.Eliminar usuario \n3.Actualizar usuarios \n4.Consultar usuarios")
                            entrada==input()
                            match entrada:
                                case 1:
                                    a.agregar(con, input("ingrese el numero del tipo de usuario: "), input("ingrese el nombre: "), input("ingrese apellido: "), input("ingrese el email: "), input("ingrese el telefono "), input("ingrese direccion: "), input("ingrese una contraseña: "))
                                case 2:
                                    a.eliminar(con, input("ingrese la campo de referencia: "), input("ingrese un operador, pero si el anterior campo es texto use el =,si no cualquier otro"), input("ingrese el dato de referencia"))
                                case 3:
                                    a.actualizar(con, input("ingrese el campo donde se va actualizar: "),input("ingrese el nuevo dato: "), input("Ingrese el campo de referencia: "), input("ingrese un dato de referencia: "))
                                case 4:
                                    print("1.Consultar un registro\n2.Consultar todos los registros")
                                    if entrada3==1:
                                        a.consultar(con,input("ingrese nombre de la tabla "),input("ingrese un operador"),input("ingrese un valor"))
                                    elif entrada3==2:
                                        a.consultarTodo(con)  
                                    else:
                                        print("no hay mas opciones")                                    
                        case 2:
                            habitacione.menuhabitacion()
                        case 3:
                            servicio.menuservicio()
                        case 4:
                            CRUD_resrvas.eliminar_reservas(con, input("ingrese el codigo"))
                        case 5:
                            print("1.Consultar una cuenta \n2.Consultar todas")
                            entrada3=int(input())
                            if entrada3==1:
                                CRUD_cuenta.consultar_cuenta(con, input("ingrese la id de la cuenta"))
                            elif entrada3==2:
                                CRUD_cuenta.consultar_todo(con)
                            else:
                                print("no mas opciones")
                        case 6:
                            print("1.Consultar una factura \n2.Consultar todas")
                            entrada3=int(input())
                            if entrada3==1:
                                CRUD_factura.consultar_factura(con, input("ingrese la id de la factura"))
                            elif entrada3==2:
                                CRUD_factura.consultar_todo(con)
                            else:
                                print("no mas opciones")
                else:   
                    print("contraseña incorrecta intente de nuevo")
     case "rec4312": #comentario para entender donde comienza el menu de recepcion
        with sqlite3.connect('proyecto.db') as con:
            while True:
                entrada=input("ingrese su contraseña: ")
                if entrada in cuentas:
                    CRUD_resrvas.menu_reservas()
                else:   
                    print("contraseña incorrecta intente de nuevo")
     case "usu131":
        with sqlite3.connect('proyecto.db') as con:
            while True:
                entrada=input("ingrese su contraseña: ")
                if entrada in cuentas:
                    print("1.Consultar una reserva\n2,consultar habitaciones")
                    entrada3=int(input())
                    if entrada3==1:
                        CRUD_resrvas.agregar_reserva(con, "ingrese la id de reserva", "ingrese la id de habitacion", "ingrese la fecha cuando va a llegar", "ingrese la fecha cuando va a salir", "ingrese la id de usuario")
                else:   
                    print("contraseña incorrecta intente de nuevo")
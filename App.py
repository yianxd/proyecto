from victor import *
from angelo import *
from jean import *
import sqlite3

print("--Bienvenido de prueba---\n actualmente no contamos con un algoritmo que pueda validar los usuarios en el sistema, asi que le daremos estos usuarios para que los pruebe:)")
print("Administador: \n usuario: admin1032 \n contraseña: 1023 \nRecepcionita: \n  usuario: rec4301 \n contraseña:4312 \nCliente \n usuario: usu131 \n contraseña: 1235  ")
cuentas=["admin1032","1023","rec4301","4312","usu131","1235"]
print("por favor ingresar el usuario y la contraseña para continuar")
entrada=input("Usuario: ")
while True:
    match entrada:
     case "admin1032":
        while True:
            entrada=input("ingrese su contraseña: ")
            if entrada in cuentas:
                print("Acciones a realizar: \n1.Gestionar usuarios\n2.Gestionar habitaciones\n3.Gestionar servicios\n4.Cancelar reservas\n6.Revisar cuentas\n6.Revisar facturas")
                entrada2=int(input())
                match entrada2:
                    case 1:
                        pass
                    case 2:
                        menuhabitaciones()
            else:
                print("contraseña incorrecta intente de nuevo")
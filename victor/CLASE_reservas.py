from CRUD_resrvas import *

class reserva:
    def __init__(self, id_res, id_hab, fecha_lleg, fecha_sal, id_usu ):
        self.__id_res=id_res
        self.__id_hab=id_hab
        self.fecha_lleg=fecha_lleg
        self.fecha_sal=fecha_sal
        self.__id_usu=id_usu

    def getId(self):
        return self.__id_res
    
    def getHabitacion(self):
        return self.__id_hab
    
    def getLlegada(self):
        return self.fecha_lleg
    
    def getSalida(self):
        return self.fecha_sal
    
    def getUsuario(self):
        return self.__id_usu
    
    def consultarTodo(self):
        datos={"Id de la reserva":self.__id_res,
        "Id de la habitacion":self.__id_hab,
        "Fecha de llegada":self.fecha_lleg,
        "Fecha de salida":self.fecha_sal,
        "Id de el usuario":self.__id_usu,}
        return datos
    
    def setLlegada(self,new):
        self.fecha_lleg=new
        return self.fecha_lleg
    
    def setSalida(self,new):
        self.fecha_sal=new
        return self.fecha_sal
    
ob=reserva(12345,101,"01/03/2023","15/03/2023",1)

print(ob.consultarTodo())
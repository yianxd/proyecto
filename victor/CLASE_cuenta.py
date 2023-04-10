from CRUD_cuenta import *

class cuenta:
    def __init__(self, id_cue, id_usu, id_ser, costo_ext):
        self.__id_cue=id_cue
        self.__id_usu=id_usu
        self.__id_ser=id_ser
        self.costo_ext=costo_ext

    def getId(self):
        return self.__id_cue
    
    def getUsuario(self):
        return self.__id_usu
    
    def getServicio(self):
        return self.__id_ser
    
    def getExtras(self):
        return self.costo_ext
    
    def consultarTodo(self):
        datos={"Id de la cuenta":self.__id_cue,
               "Id de el usuario":self.__id_usu,
               "Id de el servicio":self.__id_ser,
               "Costos Extras":self.costo_ext}
        return datos
    
    def setExtras(self,new):
        self.costo_ext=new
        return self.costo_ext
    
ob=cuenta(12,1,69,200.000)
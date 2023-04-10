class servicio:
    
    def __init__(self,id_ser,tipo_ser,costo_ser):
        self.__id_ser=id_ser
        self.tipo_ser=tipo_ser
        self.costo_ser=costo_ser
    
    def getId(self):
        return self.__id_ser
    
    def getTiposer(self):
        return self.tipo_ser
    
    def getCosto(self):
        return self.costo_ser
    
    def setTodo(self):
        datos={"Id de servicio: ":self.__id_ser,
        "Tipo de servicio: ":self.tipo_ser,
        "Costo de servicio: ":self.costo_ser}
        return datos
        
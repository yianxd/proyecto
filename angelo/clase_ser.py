class servicios:
    
    def __init__(self,id_ser,tipo_ser,costo_ser):
        self.__id_ser=id_ser
        self.tipo_ser=tipo_ser
        self.costo_ser=costo_ser
    
    def agregar_ser(self,tipo_ser,costo_ser):
        self.tipo_ser=tipo_ser
        self.costo_ser=costo_ser  
    
    def consultar_ser(self,id_ser,tipo_ser,costo_ser):
        self.__id_ser=id_ser
        self.tipo_ser=tipo_ser
        self.costo_ser=costo_ser
    
    def modificar_tip(self,id_ser,tipo_ser):
        self.__id_ser=id_ser
        self.tipo_ser=tipo_ser
    
    def modificar_cos(self,id_ser,costo_ser):
        self.__id_ser=id_ser
        self.costo_ser=costo_ser
    
    def modificar_tod(self,id_ser,tipo_ser,costo_ser):
        self.__id_ser=id_ser
        self.tipo_ser=tipo_ser
        self.costo_ser=costo_ser
    
    def eliminar_ser(self,id_ser):
        self.__id_ser=id_ser
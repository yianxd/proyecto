class habitaciones:
    
    def __init__(self,id_hab,tipo_tha,descripcion_hab):
        self.__id_hab=id_hab
        self.tipo_than=tipo_tha
        self.descripcion_hab=descripcion_hab
    
    def agregar_hab(self,tipo_tha,descripcion_tha):
        self.tipo_than=tipo_tha
        self.descripcion_hab=descripcion_tha    
    
    def consultar_hab(self,id_hab,tipo_tha,descripcion_hab):
        self.__id_hab=id_hab
        self.tipo_than=tipo_tha
        self.descripcion_hab=descripcion_hab
    
    def modificar_tip(self,id_hab,tipo_hab):
        self.__id_hab=id_hab
        self.tipo_hab=tipo_hab
    
    def modificar_des(self,id_hab,descripcion_hab):
        self.__id_hab=id_hab
        self.descripcion_hab=descripcion_hab
    
    def modificar_tod(self,id_hab,tipo_hab,descripcion_hab):
        self.__id_hab=id_hab
        self.tipo_hab=tipo_hab
        self.descripcion_hab=descripcion_hab
    
    def eliminar_hab(self,id_hab):
        self.__id_hab=id_hab

class habitacione:

    def __init__(self,id_hab,tipo_tha,descripcion_hab):
        self.__id_hab=id_hab
        self.tipo_than=tipo_tha
        self.descripcion_hab=descripcion_hab
    
    def getId(self):
        return self.__id_hab
    
    def getTipo_hab(self):
        return self.tipo_than
    
    def getdescripcion(self):
        return self.descripcion_hab
    
    def getTodo(self):
        datos={"Id de habiatcion: ":self.__id_hab,
        "Tipo de habitacion":self.tipo_than,
        "Descripcion de habitacion":self.descripcion_hab}
        return datos

ab=habitacione(2,2,"asdf")

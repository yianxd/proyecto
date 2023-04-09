class usuario:
    def __init__(self,id_usu,id_tip,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_usu=id_usu
        self.__id_tip=id_tip
        self.nombre_usu=nombre_usu
        self.apellido_usu=apellido_usu
        self.email_usu=email_usu
        self.telefono_usu=telefono_usu
        self.direccion_usu=direccion_usu
        self.__contraseña_usu=contraseña_usu

    def getId(self):
        return self.__id_usu
    
    def getTipo(self):
        return self.__id_tip

    def getNombre(self):
        return self.nombre_usu

    def getApellido(self):
        return self.apellido_usu
    
    def getEmail(self):
        return self.email_usu

    def getTelefono(self):
        return self.telefono_usu

    def getDireccion(self):
        return self.direccion_usu

    def getContraseña(self):
        return self.__contraseña_usu

    
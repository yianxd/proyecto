class Usuario:
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_usu=id_usu
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
    


    def setNombre(self,new):
        self.nombre_usu=new
        return self.nombre_usu

    def setApellido(self,new):
        self.apellido_usu=new
        return self.apellido_usu

    def setEmail(self, new):
        self.email_usu=new
        return self.email_usu

    def setTelefono(self,new):
        self.telefono_usu=new
        return self.telefono_usu

    def setDireccion(self,new):
        self.direccion_usu=new
        return self.direccion_usu

    def setContraseña(self,new):
        self.__contraseña_usu=new
        return self.__contraseña_usu


class Cliente(Usuario):
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_tip=1
        Usuario.__init__(self, id_usu, nombre_usu, apellido_usu, email_usu, telefono_usu, direccion_usu, contraseña_usu)  
    def verTodo(self):
        datos={"id": Usuario.getId(self),
        "tipo de usuario":self.__id_tip,
        "nombre":self.nombre_usu,
        "apellido":self.apellido_usu,
        "email":self.email_usu,
        "telefono":self.telefono_usu,
        "direccion":self.direccion_usu,
        "contraseña":Usuario.getContraseña(self)}
        return datos 

class Recepcionista(Usuario):
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_tip=3
        Usuario.__init__(self, id_usu, nombre_usu, apellido_usu, email_usu, telefono_usu, direccion_usu, contraseña_usu)  
    def verTodo(self):
        datos={"id": Usuario.getId(self),
        "tipo de usuario":self.__id_tip,
        "nombre":self.nombre_usu,
        "apellido":self.apellido_usu,
        "email":self.email_usu,
        "telefono":self.telefono_usu,
        "direccion":self.direccion_usu,
        "contraseña":Usuario.getContraseña(self)}
        return datos 
class Administrador(Usuario):
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_tip=2
        Usuario.__init__(self, id_usu, nombre_usu, apellido_usu, email_usu, telefono_usu, direccion_usu, contraseña_usu)  
    def verTodo(self):
        datos={"id": Usuario.getId(self),
        "tipo de usuario":self.__id_tip,
        "nombre":self.nombre_usu,
        "apellido":self.apellido_usu,
        "email":self.email_usu,
        "telefono":self.telefono_usu,
        "direccion":self.direccion_usu,
        "contraseña":Usuario.getContraseña(self)}
        return datos


class Bar(Usuario):
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_tip=4
        Usuario.__init__(self, id_usu, nombre_usu, apellido_usu, email_usu, telefono_usu, direccion_usu, contraseña_usu)  
    def verTodo(self):
        datos={"id": Usuario.getId(self),
        "tipo de usuario":self.__id_tip,
        "nombre":self.nombre_usu,
        "apellido":self.apellido_usu,
        "email":self.email_usu,
        "telefono":self.telefono_usu,
        "direccion":self.direccion_usu,
        "contraseña":Usuario.getContraseña(self)}
        return datos 
class Limpieza(Usuario):
    def __init__(self,id_usu,nombre_usu,apellido_usu,email_usu,telefono_usu,direccion_usu,contraseña_usu):
        self.__id_tip=5
        Usuario.__init__(self, id_usu, nombre_usu, apellido_usu, email_usu, telefono_usu, direccion_usu, contraseña_usu)  
    def verTodo(self):
        datos={"id": Usuario.getId(self),
        "tipo de usuario":self.__id_tip,
        "nombre":self.nombre_usu,
        "apellido":self.apellido_usu,
        "email":self.email_usu,
        "telefono":self.telefono_usu,
        "direccion":self.direccion_usu,
        "contraseña":Usuario.getContraseña(self)}
        return dato 
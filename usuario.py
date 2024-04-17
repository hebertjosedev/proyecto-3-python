from persona import Persona
#from cuenta import Cuenta

class Usuario(Persona):
    
    def __init__(self, nombre, apellido, cedula, nombre_usuario, clave_usuario, cuentas_usuario):
         super().__init__(nombre, apellido, cedula)
         self.nombre_usuario = nombre_usuario
         self.clave_usuario = clave_usuario
         self.cuentas_usuarios = cuentas_usuario


class UsuarioDto:
    
    def __init__(self, id_usuario: int, nombre: str, apellido: str, cedula: str, cargo: str, usuario: str, passw: str,):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.cargo = cargo
        self.usuario = usuario
        self.passw = passw        


class DocenteDto:
    
    def __init__(self, id: int, nombre: str, apellido: str, titulo: str, estado: str, ci: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.titulo = titulo
        self.estado = estado
        self.ci = ci
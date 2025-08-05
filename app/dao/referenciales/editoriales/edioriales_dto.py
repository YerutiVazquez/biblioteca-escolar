from ..cursos.curso_dto import CursoDto

class EditorialDto:
    
    def __init__(self, id: int, nombres_editorial: str, pais: str):
        self.id = id
        self.nombres_editorial = nombres_editorial
        self.pais = pais
from ..cursos.curso_dto import CursoDto

class EstudianteDto:
    
    def __init__(self, id: int, nombres: str, apellidos: str, ci: str, sexo: str, curso: CursoDto):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.sexo = sexo
        self.id_curso = curso.descripcion


class LibrosDto:
    
    def __init__(self, id: int, titulo: str, autor: str, ISBN: int, ano: int, genero: str, cantidad: int, ubicacion: str, id_editoriales: int,):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.ano = ano
        self.genero = genero
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.id_editoriales = id_editoriales
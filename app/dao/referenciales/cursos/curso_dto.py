class CursoDto:
    def __init__(self, id: int, descripcion: str):
        self.__id = id
        self.__descripcion = descripcion
        
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, value: int) -> None:
        
        if not isinstance(value, int):
            raise ValueError("El valor ingresado no es entero")
        elif value <= 0:
            raise ValueError("El identificador debe ser entero y positivo")
        
        self.__id = value
        
    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @descripcion.setter
    def id(self, value: str) -> None:
        
        if not isinstance(value, str):
            raise ValueError("El valor ingresado no del tipo cadena")
        elif len(value.strip()) == 0:
            raise ValueError("Verifique la cadena, puede estar vacia")
        
        self.__descripcion = value.strip().upper()
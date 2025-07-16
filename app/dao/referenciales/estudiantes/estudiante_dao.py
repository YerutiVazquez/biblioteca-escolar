from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.estudiantes.estudiante_dto import EstudianteDto

class EstudianteDao:
    
    def leer(self):
        sql = "SELECT id, nombres, apellidos, ci FROM estudiantes;"
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": estudiante[0]
                    , "nombres": estudiante[1]
                    , "apellidos": estudiante[2]
                    , "ci": estudiante[3]
                } for estudiante in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, estudiante: EstudianteDto) -> bool:
        pass
    
    def baja(self, id) -> bool:
        pass
    
    def modificacion(self, estudiante: EstudianteDto) -> bool:
        pass
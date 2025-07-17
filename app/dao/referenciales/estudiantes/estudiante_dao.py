from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.estudiantes.estudiante_dto import EstudianteDto

class EstudianteDao:
    
    def leer(self):
        sql = """
        SELECT 
            e.id, e.nombres, e.apellidos, e.ci, e.sexo, c.descripcion 
        FROM 
            estudiantes as e
        INNER JOIN 
            cursos as c on e.id_curso = c.id
        """
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
                    , "sexo": estudiante[4]
                    , "curso_descripcion": estudiante[5]
                } for estudiante in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, estudiante: EstudianteDto) -> bool:
        insertsql = """
        INSERT INTO public.estudiantes(nombres, apellidos, ci, sexo, id_curso)
	    VALUES (%s, %s, %s, %s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (estudiante.nombres, estudiante.apellidos, estudiante.ci, estudiante.sexo, estudiante.id_curso,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
        return False
    
    def baja(self, id) -> bool:
        pass
    
    def modificacion(self, estudiante: EstudianteDto) -> bool:
        pass
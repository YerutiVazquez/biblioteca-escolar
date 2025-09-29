from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.docentes.docente_dto import DocenteDto

class DocenteDao:
    
    def leer(self):
        sql = """
        SELECT 
            id_docentes, nombre, apellido, ci, materia 
        FROM 
            docentes 
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id_docentes": docente[0]
                    , "nombre": docente[1]
                    , "apellido": docente[2]
                    , "ci": docente[3]
                    , "materia": docente[4]
                } for docente in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, docente: DocenteDto) -> bool:
        insertsql = """
        INSERT INTO public.docentes(nombre, apellido, ci, materia)
	    VALUES (%s, %s, %s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (docente.nombre, docente.apellido, docente.ci, docente.materia,))
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
    
    def modificacion(self, docente: DocenteDto) -> bool:
        pass
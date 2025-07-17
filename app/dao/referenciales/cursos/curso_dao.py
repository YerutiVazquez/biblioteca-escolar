from flask import current_app as app
from app.conexion.conexion import Conexion

class CursoDao:
    
    def leer(self):
        sql = """
        SELECT 
            id, descripcion 
        FROM 
            cursos
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": curso[0]
                    , "descripcion": curso[1]
                } for curso in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
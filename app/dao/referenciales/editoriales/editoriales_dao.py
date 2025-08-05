from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.editoriales.edioriales_dto import EditorialDto

class EditorialDao:
    
    def leer(self):
        sql = """
        SELECT 
            id_editoriales, nombre_editorial, pais
        FROM 
            editoriales
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": editorial[0]
                    , "nombre_editorail": editorial[1]
                    , "pais": editorial[2]
                } for editorial in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, editorial: EditorialDto) -> bool:
        insertsql = """
        INSERT INTO public.editoriales(nombre_editorial, pais)
	    VALUES (%s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (editorial.nombres_editorial, editorial.pais,))
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
    
    def modificacion(self, editorial: EditorialDto) -> bool:
        pass
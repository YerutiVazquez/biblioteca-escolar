from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.autores.autores_dto import AutoresDto

class AutoresDao:
    
    def leer(self):
        sql = """
        SELECT 
            id_autor, nombre_autor
        FROM 
            autores
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id_autor": autores[0]
                    , "nombre_autor": autores[1]
                } for autores in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, autores: AutoresDto) -> bool:
        insertsql = """
        INSERT INTO public.autores(nombre_autor)
	    VALUES (%s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (autores.nombre_autor,))
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
    
    def modificacion(self, autores: AutoresDto) -> bool:
        pass
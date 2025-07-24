from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.perso_adm.persoadm_dto import PersoadmDto

class PersoadmDao:
    
    def leer(self):
        sql = """
        SELECT 
            id, nombre, apellido, ci, titulo, estado 
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
                    "id": persoadm[0]
                    , "nombre": persoadm[1]
                    , "apellido": persoadm[2]
                    , "ci": persoadm[3]
                    , "estado": persoadm[4]
                    
                } for persoadm in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, persoadm: PersoadmDto) -> bool:
        insertsql = """
        INSERT INTO public.docentes(nombre, apellido, titulo, estado, ci)
	    VALUES (%s, %s, %s, %s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (persoadm.nombre, persoadm.apellido, persoadm.ci, persoadm.estado,))
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
    
    def modificacion(self, persoadm: PersoadmDto) -> bool:
        pass
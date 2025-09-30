from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.usuario.usuario_dto import UsuarioDto

class UsuarioDao:
    
    def leer(self):
        sql = """
        SELECT 
            id_usuario, nombre, apellido, cedula, cargo, usuario, passw 
        FROM 
            usuario 
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": usuario[0]
                    , "nombre": usuario[1]
                    , "apellido": usuario[2]
                    , "cedula": usuario[3]
                    , "cargo": usuario[4]
                    , "usuario": usuario[5]
                    , "passw": usuario[6]
                    
                } for usuario in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, usuario: UsuarioDto) -> bool:
        insertsql = """
        INSERT INTO usuario(nombre, apellido, cedula, cargo, usuario, passw)
	    VALUES (%s, %s, %s, %s, %s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (usuario.nombre, usuario.apellido, usuario.cedula, usuario.cargo, usuario.usuario, usuario.passw))
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
    
    def modificacion(self, usuario: UsuarioDto) -> bool:
        pass
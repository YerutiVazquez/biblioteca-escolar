from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.libros.libros_dto import LibrosDto

class LibrosDto:
    
    def leer(self):
        sql = """
        SELECT id_libros, titulo, autor, "ISBN", "año_publicacion", genero, cantidad_disponible, ubicacion, id_editoriales
	FROM libros; 
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": libros[0]
                    , "nombre": libros[1]
                    , "apellido": libros[2]
                    , "titulo": libros[3]
                    , "estado": libros[4]
                    , "ci": libros[5]
                } for libros in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()

    def alta(self, libros: LibrosDto) -> bool:
        insertsql = """
        INSERT INTO public.libros(titulo, autor, "ISBN", "año_publicacion", genero, cantidad_disponible, ubicacion, id_editoriales)
	    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (libros.titulo, libros.autor, libros.ISBN, libros.año_publicacion, libros.genero, libros.cantidad_disponible, libros.ubicacion, libros.id_editoriales))
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

    def modificacion(self, libros: LibrosDto) -> bool:
        pass
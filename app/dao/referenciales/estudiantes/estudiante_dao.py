from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.referenciales.estudiantes.estudiante_dto import EstudianteDto
from datetime import date

class EstudianteDao:
    
    def leer(self):
        sql = """
       SELECT id_estudiantes, nombre, apellido, ci, telef, curso, turno
	FROM public.estudiantes;
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql)
            lista = cur.fetchall()
            return [{
                    "id": estudiante[0]
                    , "nombre": estudiante[1]
                    , "apellido": estudiante[2]
                    , "ci": estudiante[3]
                    , "telef": estudiante[4]
                    , "curso": estudiante[5]
                    , "turno": estudiante[6]
                } for estudiante in lista ] if len(lista) != 0 else []
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
            
    def leerPorId(self, id):
        sql = """
        SELECT id_estudiantes, nombre, apellido, ci, telef, curso, turno
	FROM public.estudiantes;
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(sql, (id,))
            estudiante = cur.fetchone()
            return {
                    "id": estudiante[0]
                    , "nombre": estudiante[1]
                    , "apellido": estudiante[2]
                    , "ci": estudiante[3]
                   , "telef": estudiante[4]
                    , "curso": estudiante[5]
                    , "turno": estudiante[6]
                }
            
        except con.Error as e:
            app.logger.error(e)
        finally:
            cur.close()
            con.close()
    
    def alta(self, estudiante: EstudianteDto) -> bool:
        insertsql = """
        INSERT INTO public.estudiantes(nombre, apellido, ci, telef, curso, turno)
	        VALUES (?, ?, ?, ?, ?, ?);
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            cur.execute(insertsql, (estudiante.nombre, estudiante.apellido, estudiante.ci, estudiante.telef, estudiante.curso, estudiante.turno))
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
        """Actualiza un estudiante existente en la base de datos (UPDATE)."""
        updatesql = """
        UPDATE public.estudiantes
	SET id_estudiantes=?, nombre=?, apellido=?, ci=?, telef=?, curso=?, turno=?
	WHERE id_estudiantes=%s;
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        
        try:
            # La tupla de parámetros incluye todos los campos, y el ID al final para el WHERE
            cur.execute(updatesql, (
                estudiante.nombres, 
                estudiante.apellidos, 
                estudiante.ci, 
                estudiante.telef, 
                estudiante.curso,
                estudiante.turno # Clave para la cláusula WHERE
            ))
            con.commit()
            return True
        except con.Error as e:
            # Mantiene la estructura de manejo de errores de 'alta'
            # app.logger.error(e)
            print(f"ERROR en MODIFICACION: {e}") # Log de simulación
        finally:
            cur.close()
            con.close()
        return False
        pass
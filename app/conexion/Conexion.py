import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=biblioteca_db user=postgres host=127.0.0.1 password=1")

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con
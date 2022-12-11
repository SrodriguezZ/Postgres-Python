from logger_base import log
import sys
import psycopg2 as bd

class Conexion:

    _database='test_db'
    _username='postgres'
    _password='admin'
    _da_port='5432'
    _host='127.0.0.1'
    _conexion=None
    _cursor=None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(database=cls._database,
                                           user=cls._username,
                                           password=cls._password,
                                           port=cls._da_port,
                                           host=cls._host)
                log.debug(f'CONEXION SEGURA: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'OCURRIO UN ERROR CONEXION:{e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'CONEXION SEGURA DE CURSOR_{cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'OCURRIO UN ERROR CURSOR:{e}')

        else:
            return cls._cursor
if __name__=='__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
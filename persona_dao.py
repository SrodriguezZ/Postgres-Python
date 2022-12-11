from conexion import Conexion
from persona import Persona
from logger_base import log


class PersonaDAO:
    '''
    DAO: DATA ACCESS OBJETC
    CRUD: CREATE-READ-UPDATE-DELETE
    '''

    _seleccion= 'SELECT * FROM persona ORDER BY id_persona'
    _insetar  = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s,%s,%s)'
    _actualizar = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s  WHERE id_persona=%s'
    _delete = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccion(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._seleccion)








from ..modelos.estudiantes import Matricula
from ..conexion.conexion_matricula import (select_all, 
                                             select_by_codigo, 
                                             crear_matricula,
                                             eliminar_matricula)

def servicio_matricula_all():
    matriculas = select_all()
    print(matriculas)
    return matriculas

def servicio_consultar_codigo(codigo: str):
    if len(codigo) !=0:
        matriculas = select_by_codigo(codigo)
        print("mostramos la consulta: ", matriculas)
        return matriculas
    else:
        return select_all()
    
def servicio_crear_matricula(matricula: dict):
    matricula = Matricula(**matricula)
    print(matricula)
    return crear_matricula(matricula)

def servicio_eliminar_matricula(id: int):
    return eliminar_matricula(id)
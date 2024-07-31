from ..modelos.estudiantes import *
from ..conexion.asig_periodo_conexion import *

def servicio_asig_periodo_all():
    valores = select_all()
    print(valores)
    return valores

def servicio_consultar_codigo(codigo: str):
    if len(codigo) !=0:
        valoress = select_by_codigo(codigo)
        print("mostramos la consulta: ", valoress)
        return valoress
    else:
        return select_all()
    
def servicio_crear_asig_periodo(asignatura_periodo: dict):
    objeto = AsignaturaPeriodo(**asignatura_periodo)
    print(objeto)
    return crear_asignatura_periodo(objeto)

def servicio_eliminar_asig_periodo(id: int):
    return servicio_eliminar_asig_periodo(id)
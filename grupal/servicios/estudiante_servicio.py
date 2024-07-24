from ..modelos.estudiantes import Estudiantes
from ..conexion.conexion_estudiantes import (select_all, 
                                             select_by_cedula, 
                                             crear_estudiante,
                                             eliminar_estudiante)

def servicio_estudiantes_all():
    estudiantes = select_all()
    print(estudiantes)
    return estudiantes

def servicio_consultar_cedula(cedula: str):
    if len(cedula) !=0:
        estudiantes = select_by_cedula(cedula)
        print("mostramos la consulta: ", estudiantes)
        return estudiantes
    else:
        return select_all()
    
def servicio_crear_estudiante(nombres: str, 
                              apellidos: str, 
                              cedula:str, 
                              correo: str, 
                              celular: str, 
                              direccion: str, 
                              fono: str):
    estudiate = servicio_consultar_cedula(cedula)
    print(estudiate)
    if not estudiate:
        nuevo_estudiante = Estudiantes(nombres,apellidos,cedula,correo,celular,direccion,fono)
        return crear_estudiante(nuevo_estudiante)
    else:
        return "El estudiante ya existe"

def servicio_eliminar_estudiante(id: int):
    return eliminar_estudiante(id)
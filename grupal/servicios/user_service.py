from ..conexion.user_conexion import *

def servicio_autentificacion(username:str, password:str) -> bool:
    return autentificar_usuario(username, password)

def servicio_crear_user(username:str, password:str, estudiante_id: int):
    return crear_user(username, password, estudiante_id)
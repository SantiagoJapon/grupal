import reflex as rx

class ModeloCurso(rx.Model):
    """ Definir un metodo iniciador para los atributos """
    def __init__(self, nombre: str, descripcion: str, duracion: int, responsable:str ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.responsable = responsable
    
    def __str__(self):
        return f'{self.nombre} estara habilitado por {self.duracion} dias '
    
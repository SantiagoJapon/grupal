from ..modelos.estudiantes import Estudiantes
from .conexion import connect
from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy.exc import SQLAlchemyError

# a partir de qui generamos el ORM del proyecto
# istar(obtenerner todos), crear, actualizar, borrar

def select_all():
    # crear una lista de estudiantes
    engine = connect()
    with Session(engine) as session:
        consulta = select(Estudiantes)
        estudiantes = session.exec(consulta)
        return estudiantes.all()

# buscar estudiantes por numero de cedula
def select_by_cedula(cedula:str):
    engine = connect()
    with Session(engine) as session:
        consulta = select(Estudiantes).where(Estudiantes.cedula == cedula)
        resultado = session.exec(consulta)
        return resultado.all()
    

# crear un estudiante
def crear_estudiante(estudiante: Estudiantes):
    engine = connect()
    try:
        with Session(engine) as session:
            session.add(estudiante)
            session.commit()
            print(estudiante)
            if estudiante.id is not None:
                consulta = select(Estudiantes).where(Estudiantes.id == estudiante.id)
                resultado = session.exec(consulta)
                return resultado.all()
            else:
                return None
    except SQLAlchemyError as e:
        print(e)

# eliminar registro
def eliminar_estudiante(id : int):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(Estudiantes).where(Estudiantes.id == id)
            estudiante = session.exec(consulta).one_or_none()
            if estudiante:
                session.delete(estudiante)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

# actualizar registro
def actualizar_estudiante(estudiante: Estudiantes):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(Estudiantes).where(Estudiantes.id == estudiante.id)
            estudiante_actual = session.exec(consulta).one_or_none()
            if estudiante_actual:
                session.update(estudiante)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

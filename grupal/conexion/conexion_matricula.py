from ..modelos.estudiantes import Matricula
from .conexion import connect
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

# a partir de qui generamos el ORM del proyecto
def select_all():
    # crear una lista de estudiantes
    engine = connect()
    with Session(engine) as session:
        consulta = select(Matricula).options(selectinload(Matricula.estudiante))
        matriculas = session.exec(consulta)
        return matriculas.all()

# buscar estudiantes por numero de cedula
def select_by_codigo(codigo:str):
    engine = connect()
    with Session(engine) as session:
        consulta = select(Matricula).where(Matricula.codigo == codigo)
        resultado = session.exec(consulta)
        return resultado.all()

# crear un estudiante
def crear_matricula(matricula: Matricula):
    engine = connect()
    try:
        with Session(engine) as session:
            session.add(matricula)
            session.commit()
            print(matricula)
            if matricula.id is not None:
                consulta = select(Matricula).where(Matricula.id == matricula.id)
                resultado = session.exec(consulta)
                return resultado.all()
            else:
                return None
    except SQLAlchemyError as e:
        print(e)

# eliminar registro
def eliminar_matricula(id : int):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(Matricula).where(Matricula.id == id)
            matricula = session.exec(consulta).one_or_none()
            if matricula:
                session.delete(matricula)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

# actualizar registro
def actualizar_matricula(matricula: Matricula):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(Matricula).where(Matricula.id == matricula.id)
            matricula_actual = session.exec(consulta).one_or_none()
            if matricula_actual:
                session.update(matricula)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

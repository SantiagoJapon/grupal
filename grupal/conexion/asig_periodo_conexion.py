from ..modelos.estudiantes import *
from .conexion import connect
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

# a partir de qui generamos el ORM del proyecto
def select_all():
    # crear una lista de estudiantes
    engine = connect()
    with Session(engine) as session:
        consulta = select(AsignaturaPeriodo).options(selectinload(AsignaturaPeriodo.estudiante))
        resultado = session.exec(consulta)
        return resultado.all()

# buscar estudiantes por numero de cedula
def select_by_codigo(codigo:str):
    engine = connect()
    with Session(engine) as session:
        consulta = select(AsignaturaPeriodo).where(AsignaturaPeriodo.codigo == codigo)
        resultado = session.exec(consulta)
        return resultado.all()

# crear un estudiante
def crear_asignatura_periodo(asignatura_periodo: AsignaturaPeriodo):
    engine = connect()
    try:
        with Session(engine) as session:
            session.add(asignatura_periodo)
            session.commit()
            print(asignatura_periodo)
            if asignatura_periodo.id is not None:
                consulta = select(AsignaturaPeriodo).where(asignatura_periodo.id == asignatura_periodo.id)
                resultado = session.exec(consulta)
                return resultado.all()
            else:
                return None
    except SQLAlchemyError as e:
        print(e)

# eliminar registro
def eliminar_asignatura_periodo(id : int):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(AsignaturaPeriodo).where(AsignaturaPeriodo.id == id)
            objeto = session.exec(consulta).one_or_none()
            if objeto:
                session.delete(objeto)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

# actualizar registro
def actualizar_matricula(objeto: AsignaturaPeriodo):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(AsignaturaPeriodo).where(AsignaturaPeriodo.id == objeto.id)
            objeto_actual = session.exec(consulta).one_or_none()
            if objeto_actual:
                session.update(objeto_actual)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

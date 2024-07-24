import bcrypt
from ..modelos.estudiantes import User
from .conexion import connect
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

def autenticar_usuario(username:str, password:str)-> bool:
    engine = connect()
    with Session(engine) as session:
        consulta = select(User).where(User.username == username)
        resultado = session.exec(consulta).first()
        if resultado and validar_password(resultado.password, password):
            return True
        return False
    
def validar_password(password_bd:str, passwor_ingresado:str)-> bool:
    return bcrypt.checkpw(passwor_ingresado.encode('utf-8'), password_bd.encode('utf-8'))

def crear_user(username:str, password:str, estudiante_id: int)-> str:
    engine = connect()
    with Session(engine) as session:
        consulta = select(User).where(User.username ==username)
        result = session.exec(consulta).first()
        if result:
            return "El usuario ya existe"
        
        hasshed_password = bcrypt.hashpw(password.endcode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password=hasshed_password, estudiante=estudiante_id)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return "El usuario se ha creado exitosamente"


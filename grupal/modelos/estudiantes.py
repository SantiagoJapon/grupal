import reflex as rx
from typing import Optional, List
from sqlmodel import Field, Relationship

class Estudiantes(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombres: str = Field(index=True)
    apellidos: str
    cedula: str
    correo: str
    celular: str
    direccion: str
    fono: str
    matriculas: List['Matricula'] = Relationship(back_populates="estudiante")
    user: Optional['User'] = Relationship(back_populates="estudiante")

    def getMatriculas(self):
        return self.matriculas

class Matricula(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True)
    fechaMatricula: str
    estado: str
    pagoMatricula: float
    fechaPago: str
    estudiante_id: int = Field(foreign_key="estudiantes.id")
    estudiante: Optional[Estudiantes] = Relationship(back_populates="matriculas")
    asignatura_periodo_id: int = Field(foreign_key="asignaturaperiodo.id")
    asignatura_periodo: Optional['AsignaturaPeriodo'] = Relationship(back_populates="matriculas")

class User(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    estudiante_id: int = Field(foreign_key="estudiantes.id")
    estudiante: Optional[Estudiantes] = Relationship(back_populates="user")

class Carrera(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    tiempo_duracion: str
    modalidad: float
    fecha_creacion: str
    fecha_creacion_registro: str

class Asignatura(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    nombre: str
    num_horas: int
    horas_acad: int
    horas_prac: int
    horas_auto: int
    asignaturas_periodo: List['AsignaturaPeriodo'] = Relationship(back_populates="asignatura")

class Paralelo(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    nombre: str
    numero: int
    asignaturas_periodo: List["AsignaturaPeriodo"] = Relationship(back_populates="paralelo")

class PeriodoAcademico(rx.Model, table=True):
    __tablename__ = "periodo_academico"
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    nombre: str
    descripcion: str
    asignaturas_periodo: List['AsignaturaPeriodo'] = Relationship(back_populates="periodo_academico")

class AsignaturaPeriodo(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    codigo: str
    fecha: str
    estado: str
    asignatura_id: int = Field(foreign_key="asignatura.id")
    asignatura: Optional['Asignatura'] = Relationship(back_populates="asignaturas_periodo")
    paralelo_id: int = Field(foreign_key="paralelo.id")
    paralelo: Optional['Paralelo'] = Relationship(back_populates="asignaturas_periodo")
    periodo_academico_id: int = Field(foreign_key="periodo_academico.id")
    periodo_academico: Optional['PeriodoAcademico'] = Relationship(back_populates="asignaturas_periodo")
    matriculas: List['Matricula'] = Relationship(back_populates="asignatura_periodo")
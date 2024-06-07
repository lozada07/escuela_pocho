from sqlalchemy import Boolean, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from utils.base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    contraseña = Column(String, nullable=True)
    direccion = Column(String)
    telefono = Column(String)
    edad = Column(Integer)
    sexo = Column(String)
    targetas_rojas= Column(Integer, nullable=True)
    targetas_amarillas= Column(Integer, nullable=True)
    goles= Column(Integer, nullable=True)
    partidos= Column(Integer, nullable=True)
    posicion= Column(Enum("Delantero", "Medio", "Portero", "Defensa", "Director tecnico", "Auxiliar tecnico", "Preparador fisico", "Psicólogo deportivo", "Médico" , name="posicion"))
    activo=Column(Enum("Activo", "Inactivo", name="activo"))
    rol = Column(Enum("Jugador", "Equipo Tecnico", "Administrador", name="rol"))
    categoria = Column(Enum("Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B", name="categoria"))

    def __repr__(self):
        return f"<Usuario(id='{self.id}' nombre='{self.nombre}', apellido='{self.apellido}', direccion='{self.direccion}', telefono='{self.telefono}', edad={self.edad}, sexo='{self.sexo}', role='{self.rol}', categoria='{self.categoria}', posicion='{self.posicion}', activo='{self.activo}', targetas_rojas='{self.targetas_rojas}', targetas_amarillas='{self.targetas_amarillas}', goles='{self.goles}', partidos='{self.partidos}')>"


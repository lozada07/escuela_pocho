from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from utils.base import Base



class Partido(Base):
    __tablename__ = 'partidos'

    id = Column(Integer, primary_key=True)
    equipo_visitante = Column(Enum("Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B", name="categoria"))
    equipo_local = Column(Enum("Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B", name="categoria"))
    fecha_partido = Column(String)  
    hora_partido = Column(String)  
    goles_visitante = Column(Integer,  default=0)
    goles_local = Column(Integer,  default=0)
    estado_partido = Column(Enum("Proximo", "Hoy", "En Juego","Finalizado", name="estado"), default="Proximo")


    def __repr__(self):
        return f"<Partido(id='{self.id}', equipo_visitante='{self.equipo_visitante}', equipo_local='{self.equipo_local}', fecha_partido='{self.fecha_partido}', hora_partido='{self.hora_partido}', goles_visitante={self.goles_visitante}, goles_local={self.goles_local}, estado_partido='{self.estado_partido}')>"
        
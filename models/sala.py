from sqlalchemy import Column, String, Date, BigInteger
from sqlalchemy.orm import declarative_base
#creacion de sala como entidad
Base = declarative_base()

class Sala(Base):
    __tablename__ = "salas"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String(50), nullable=False)  # equivalente a @NotEmpty + @Size(2,50)
    descripcion = Column(String, nullable=True)
    fecha = Column(Date, nullable=True)
    creador_id = Column(BigInteger, nullable=True)
    isActiva = Column(BigInteger, nullable=True)  # podrías usar Boolean si quieres

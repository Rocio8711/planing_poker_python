from sqlalchemy import Column, String, Date, BigInteger
from models.base import Base

class Sala(Base):
    __tablename__ = "sala"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=True)
    fecha = Column(Date, nullable=True)
    creador_id = Column(BigInteger, nullable=True)
    isActiva = Column("is_activa", BigInteger, nullable=True)


from sqlalchemy import Column, BigInteger, Integer
from models.base import Base

class Votacion(Base):
    __tablename__ = "votacion"

    usuario_id = Column(BigInteger, primary_key=True)
    sala_id = Column(BigInteger, primary_key=True)
    tarea_id = Column(BigInteger, primary_key=True)
    valor = Column(Integer, nullable=False)

from sqlalchemy import Column, Integer, ForeignKey
from models.base import Base

class SalaHasTarea(Base):
    __tablename__ = 'sala_has_tarea'

    sala_id = Column(Integer, ForeignKey("sala.id"), primary_key=True)
    tarea_id = Column(Integer, ForeignKey("tarea.id"), primary_key=True)

    valor_final = Column(Integer, default=0)
    finalizada = Column(Integer, default=0)


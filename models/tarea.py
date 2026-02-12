from sqlalchemy import Column, String, BigInteger
from models.base import Base

class Tarea(Base):
    __tablename__ = "tarea"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String(45), nullable=True)
    url = Column(String(500), nullable=True)

from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from database import Base

class UsuarioHasSala(Base):
    __tablename__ = "usuario_has_sala"

    usuario_id = Column(BigInteger, ForeignKey("usuarios.id"), primary_key=True)
    sala_id = Column(BigInteger, ForeignKey("salas.id"), primary_key=True)

    estado = Column(Integer, nullable=False)

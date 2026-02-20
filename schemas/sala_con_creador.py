from pydantic import BaseModel
from datetime import date

class SalaConCreadorDTO(BaseModel):
    id_sala: int | None = None
    nombre_sala: str | None = None
    descripcion: str | None = None
    fecha: date | None = None
    creador_id: int | None = None
    is_activa: int | None = None

    nombre_creador: str | None = None
    apellido: str | None = None
    email: str | None = None
    password: str | None = None

    class Config:
        from_attributes = True
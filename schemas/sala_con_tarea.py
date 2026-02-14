from pydantic import BaseModel
from datetime import date


class SalaConTareaDTO(BaseModel):
    id_sala: int | None = None
    nombre_sala: str | None = None
    descripcion: str | None = None
    fecha: date | None = None
    creador_id: int | None = None
    is_activa: int | None = None

    id_tarea: int | None = None
    nombre_tarea: str | None = None
    url: str | None = None

    class Config:
        from_attributes = True

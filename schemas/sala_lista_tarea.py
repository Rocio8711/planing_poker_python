from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from schemas.tarea import TareaResponse


class SalaListaTareaDTO(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    creador_id: Optional[int] = None
    is_activa: Optional[int] = None

    listaTareas: List[TareaResponse] = []

    class Config:
        from_attributes = True
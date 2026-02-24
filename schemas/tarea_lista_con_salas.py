from pydantic import BaseModel
from typing import List, Optional


class SalaSimple(BaseModel):
    id: int
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    creador_id: Optional[int] = None
    is_activa: Optional[int] = None


class TareaListaConSalas(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    url: Optional[str] = None
    lista_salas: Optional[List[SalaSimple]] = []
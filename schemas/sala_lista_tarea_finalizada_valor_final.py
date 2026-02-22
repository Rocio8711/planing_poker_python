from pydantic import BaseModel
from typing import List, Optional
from .tarea_con_finalizada import TareaConFinalizada

class SalaListaTareaFinalizadaValorFinal(BaseModel):
    id: int
    nombre: Optional[str] = None
    isActiva: Optional[int] = None
    listaTareas: List[TareaConFinalizada]
    sumaDeLasTareas: Optional[int] = 0

    model_config = {
        "from_attributes": True
    }
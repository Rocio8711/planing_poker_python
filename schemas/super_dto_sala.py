from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from schemas.tarea_con_finalizada import TareaConFinalizada
from schemas.usuarios_con_estado import UsuariosConEstado
from schemas.votacion import VotacionResponse


class SuperDtoSalaConListasDetareasYUsuarios(BaseModel):
    id: int
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    creador_id: Optional[int] = None
    isActiva: Optional[int] = None

    listaTareas: List[TareaConFinalizada] = []
    listaUsuario: List[UsuariosConEstado] = []
    listaVotacion: List[VotacionResponse] = []

    sumaDeLasTareas: float = 0.0

    model_config = {
        "from_attributes": True
    }
from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from schemas.usuarios_con_estado import UsuariosConEstado

class TareaConFinalizada(BaseModel):
    id: int
    nombre: Optional[str] = None
    url: Optional[str] = None
    finalizada: Optional[int] = None
    valor_final: Optional[int] = None


class VotacionResponse(BaseModel):
    id: int
    usuario_id: int
    tarea_id: int
    valor: int


class SuperSala(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    creador_id: Optional[int] = None
    is_activa: Optional[int] = None

    lista_tareas: Optional[List[TareaConFinalizada]] = []
    lista_usuarios: Optional[List["UsuariosConEstado"]] = []
    lista_votaciones: Optional[List[VotacionResponse]] = []

    suma_de_las_tareas: Optional[float] = None
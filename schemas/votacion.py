# schemas/votacion.py
from pydantic import BaseModel
from typing import Annotated
from pydantic import Field

class VotacionBase(BaseModel):
    usuario_id: int
    sala_id: int
    tarea_id: int
    valor: int

class VotacionCreate(VotacionBase):
    pass

class VotacionResponse(VotacionBase):

    model_config = {
        "from_attributes": True
    }

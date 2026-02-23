from pydantic import BaseModel

class VotacionBase(BaseModel):
    usuario_id: int
    sala_id: int
    tarea_id: int

class VotacionCreate(VotacionBase):
    valor: int

class VotacionResponse(VotacionBase):
    valor: int | None = None

    model_config = {
        "from_attributes": True
    }
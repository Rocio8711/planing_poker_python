from pydantic import BaseModel

class SalaHasTareaBase(BaseModel):
    sala_id: int
    tarea_id: int
    valor_final: int = 0
    finalizada: int = 0

class SalaHasTareaCreate(BaseModel):
    sala_id: int
    tarea_id: int

class SalaHasTareaResponse(SalaHasTareaBase):
    model_config = {
        "from_attributes": True
    }

class SalaHasTareaUpdate(BaseModel):
    valor_final: int
    finalizada: int
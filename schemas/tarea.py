from pydantic import BaseModel
from typing import Optional

class TareaBase(BaseModel):
    nombre: Optional[str] = None
    url: Optional[str] = None

class TareaCreate(TareaBase):
    pass

class TareaResponse(TareaBase):
    id: int


    model_config = {
        "from_attributes": True  # Esto reemplaza 'orm_mode' de Pydantic V1
    }
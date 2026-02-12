from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SalaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    creador_id: Optional[int] = None
    is_activa: Optional[int] = None  

class SalaCreate(SalaBase):
    pass

class SalaResponse(SalaBase):
    id: int

    model_config = {
        "from_attributes": True
    }


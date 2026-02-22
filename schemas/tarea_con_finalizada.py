from pydantic import BaseModel
from typing import Optional

class TareaConFinalizada(BaseModel):
    id: int
    nombre: Optional[str] = None
    url: Optional[str] = None
    valor_final: Optional[int] = 0
    finalizada: Optional[int] = 0

    model_config = {
        "from_attributes": True
    }
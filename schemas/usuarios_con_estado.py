from pydantic import BaseModel
from typing import Optional

class UsuariosConEstado(BaseModel):
    usuario_id: int
    nombreUsuario: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    estado: Optional[int] = None

    model_config = {
        "from_attributes": True
    }
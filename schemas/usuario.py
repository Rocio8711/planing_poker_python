from typing import Annotated,Optional
from pydantic import BaseModel, EmailStr, constr

#from typing import Optional



class UsuarioBase(BaseModel):
    nombre: Annotated[str, constr(min_length=2, max_length=50)]
    apellido: Annotated[str, constr(min_length=2, max_length=50)]
    email: EmailStr
    password: Annotated[str, constr(min_length=6, max_length=20)]

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    model_config = {
        "from_attributes": True  # Pydantic V2 reemplaza orm_mode
    }

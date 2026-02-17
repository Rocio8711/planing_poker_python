from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class UsuariosConEstado(BaseModel):
    usuario_id: int
    nombre_usuario: Optional[str] = None
    apellido: Optional[str] = None
    estado: Optional[int] = None

class SalaListaConUsuarios(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    creador_id: Optional[int] = None
    is_activa: Optional[int] = None
    lista_usuarios: Optional[List[UsuariosConEstado]] = []

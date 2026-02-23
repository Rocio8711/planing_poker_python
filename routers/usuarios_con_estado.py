from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from typing import List

from schemas.usuarios_con_estado import UsuariosConEstado
from services import usuarios_con_estado_service as service

router = APIRouter(
    prefix="/api/salaslistausuarioestado",
    tags=["UsuariosConEstado"]
)

class SalaRequest(BaseModel):
    id: int


@router.post(
    "/salalistusuest",
    response_model=List[UsuariosConEstado]
)
def usuarios_con_estado_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return service.usuarios_con_estado_por_sala(db, data.id)
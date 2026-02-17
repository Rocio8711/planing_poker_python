from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.sala_lista_con_usuarios import SalaListaConUsuarios
from services import sala_lista_con_usuarios_service
from pydantic import BaseModel

router = APIRouter(prefix="/api/salaconlistausuarios", tags=["SalaListaConUsuarios"])

class SalaRequest(BaseModel):
    id: int

@router.post("/salaxconlistausuariossinentrar", response_model=SalaListaConUsuarios)
def sala_con_usuarios_sin_entrar_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_lista_con_usuarios_service.sala_con_usuarios_sin_entrar(db, data.id)

@router.post("/salaxconlistausuarios", response_model=SalaListaConUsuarios)
def sala_con_usuarios_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_lista_con_usuarios_service.sala_con_usuarios(db, data.id)

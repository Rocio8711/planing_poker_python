from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import get_db
from schemas.sala_con_creador import SalaConCreadorDTO
from services import salas_con_creador_service

router = APIRouter(prefix="/api/salasconcreador", tags=["SalasConCreador"])

# Request DTO
class CreadorRequest(BaseModel):
    creador_id: int

# Devuelve todas las salas de un creador
@router.post("/salasxidusuariocreado", response_model=List[SalaConCreadorDTO])
def salas_por_creador(data: CreadorRequest, db: Session = Depends(get_db)):
    return salas_con_creador_service.salas_con_creador_por_id(db, data.creador_id)

# Devuelve todas las salas con sus creadores
@router.post("/todaslassalas", response_model=List[SalaConCreadorDTO])
def todas_las_salas(db: Session = Depends(get_db)):
    return salas_con_creador_service.todas_las_salas_con_creador(db)
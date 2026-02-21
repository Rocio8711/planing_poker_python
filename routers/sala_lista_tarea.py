from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from schemas.sala_lista_tarea import SalaListaTareaDTO
from services import sala_lista_tarea_service


router = APIRouter(prefix="/api/salasconlista", tags=["SalaListaTareaDTO"])


class SalaRequest(BaseModel):
    id: int


@router.post("/salacontareas", response_model=SalaListaTareaDTO)
def sala_con_tareas(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_lista_tarea_service.sala_con_lista_tareas(db, data.id)


@router.post("/existenciatareassinvotacion", response_model=bool)
def existencia_tareas_sin_votar(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_lista_tarea_service.existencia_de_tareas_sin_votar(db, data.id)


@router.post("/existenciatareass", response_model=bool)
def existencia_tareas(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_lista_tarea_service.existencia_de_tareas(db, data.id)
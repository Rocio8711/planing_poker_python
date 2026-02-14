from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import sala_con_tarea_service
from schemas.sala_con_tarea import SalaConTareaDTO
from pydantic import BaseModel


router = APIRouter(prefix="/api/salasytarea", tags=["SalaConTareaDTO"])


class SalaRequest(BaseModel):
    id: int


class TareaRequest(BaseModel):
    id: int


# Devuelven una sala con todas sus tareas
@router.post("/salasxidcontareadto", response_model=list[SalaConTareaDTO])
def salas_x_tarea(data: SalaRequest, db: Session = Depends(get_db)):
    return sala_con_tarea_service.salas_con_tarea_por_id(db, data.id)


# Devuelven una tarea en todas las salas
@router.post("/tareasxiconsala", response_model=list[SalaConTareaDTO])
def tarea_x_salas(data: TareaRequest, db: Session = Depends(get_db)):
    return sala_con_tarea_service.tarea_en_todas_las_salas(db, data.id)


# Devuelven todas las salas con todas las tareas
@router.post("/salastareastodas", response_model=list[SalaConTareaDTO])
def salas_tareas_todas(db: Session = Depends(get_db)):
    return sala_con_tarea_service.salas_tareas_todas(db)

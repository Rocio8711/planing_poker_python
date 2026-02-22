from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel

from schemas.sala_lista_tarea_finalizada_valor_final import SalaListaTareaFinalizadaValorFinal
from services import sala_lista_tarea_finalizada_valor_final_service as service

router = APIRouter(
    prefix="/api/salasconlistafinalizadayvalorfinal",
    tags=["SalaListaTareaFinalizadaValorFinal"]
)

class SalaRequest(BaseModel):
    id: int


@router.post("/salalistadocompleto", response_model=SalaListaTareaFinalizadaValorFinal)
def sala_lista_completa_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return service.sala_lista_completa(db, data.id)


@router.post("/salalistasininiciar", response_model=SalaListaTareaFinalizadaValorFinal)
def sala_lista_sin_iniciar_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return service.sala_lista_sin_iniciar(db, data.id)


@router.post("/salalistaenproceso", response_model=SalaListaTareaFinalizadaValorFinal)
def sala_lista_en_proceso_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return service.sala_lista_en_proceso(db, data.id)


@router.post("/salalistafinalizada", response_model=SalaListaTareaFinalizadaValorFinal)
def sala_lista_finalizada_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return service.sala_lista_finalizada(db, data.id)
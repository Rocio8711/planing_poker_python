from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from services import tarea_lista_con_salas_service as service
from schemas.tarea_lista_con_salas import TareaListaConSalas

router = APIRouter(
    prefix="/api/tarealistaconsalas",
    tags=["TareaListaConSalas"]
)


class TareaRequest(BaseModel):
    id: int


@router.post(
    "/tareaensalas",
    response_model=TareaListaConSalas
)
def tarea_en_salas_endpoint(data: TareaRequest, db: Session = Depends(get_db)):

    resultado = service.tarea_en_lista_de_salas(db, data.id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return resultado
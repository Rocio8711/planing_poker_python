from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel

from schemas.super_dto_sala import SuperDtoSalaConListasDetareasYUsuarios
from services import super_sala_service

router = APIRouter(
    prefix="/api/supersala",
    tags=["SuperSala"]
)

class SalaRequest(BaseModel):
    id: int


@router.post(
    "/salaconlistadeusuariosytareasyvotaciones",
    response_model=SuperDtoSalaConListasDetareasYUsuarios
)
def super_sala_endpoint(data: SalaRequest, db: Session = Depends(get_db)):
    return super_sala_service.sala_super_completa(db, data.id)
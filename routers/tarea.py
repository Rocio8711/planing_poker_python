from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.tarea import Tarea
from schemas.tarea import TareaCreate, TareaResponse
from database import get_db

router = APIRouter(prefix="/tarea", tags=["Tareas"])

@router.post("/", response_model=TareaResponse)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = Tarea(**tarea.dict())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

@router.get("/", response_model=List[TareaResponse])
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()

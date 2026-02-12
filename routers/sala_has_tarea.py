from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from database import get_db
from models.sala_has_tarea import SalaHasTarea
from schemas.sala_has_tarea import (
    SalaHasTareaCreate,
    SalaHasTareaResponse,
    SalaHasTareaUpdate
)

router = APIRouter(
    prefix="/api/sala-has-tarea",
    tags=["SalaHasTarea"]
)

# Crear relación sala-tarea
@router.post("/", response_model=SalaHasTareaResponse)
def create_relation(data: SalaHasTareaCreate, db: Session = Depends(get_db)):
    existe = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == data.sala_id,
        SalaHasTarea.tarea_id == data.tarea_id
    ).first()

    if existe:
        raise HTTPException(status_code=409, detail="La relación ya existe")

    nueva = SalaHasTarea(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


# Obtener todas las tareas de una sala
@router.get("/sala/{sala_id}", response_model=List[SalaHasTareaResponse])
def get_tareas_by_sala(sala_id: int, db: Session = Depends(get_db)):
    return db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id
    ).all()


# Obtener suma total de una sala
@router.get("/suma-total/{sala_id}")
def suma_total_sala(sala_id: int, db: Session = Depends(get_db)):
    total = db.query(func.sum(SalaHasTarea.valor_final)).filter(
        SalaHasTarea.sala_id == sala_id
    ).scalar()

    return {"total": total or 0}


# Obtener relación específica sala-tarea
@router.get("/{sala_id}/{tarea_id}", response_model=SalaHasTareaResponse)
def get_relation(sala_id: int, tarea_id: int, db: Session = Depends(get_db)):
    registro = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.tarea_id == tarea_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="No encontrado")

    return registro


# Actualizar relación sala-tarea
@router.put("/{sala_id}/{tarea_id}", response_model=SalaHasTareaResponse)
def update_relation(
    sala_id: int,
    tarea_id: int,
    data: SalaHasTareaUpdate,
    db: Session = Depends(get_db)
):
    registro = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.tarea_id == tarea_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="No encontrado")

    registro.valor_final = data.valor_final
    registro.finalizada = data.finalizada

    db.commit()
    db.refresh(registro)

    return registro


# Eliminar relación sala-tarea
@router.delete("/{sala_id}/{tarea_id}")
def delete_relation(sala_id: int, tarea_id: int, db: Session = Depends(get_db)):
    registro = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.tarea_id == tarea_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="No encontrado")

    db.delete(registro)
    db.commit()

    return {"detail": "Relación eliminada"}

'''
@router.post("/", response_model=SalaHasTareaResponse)
def create_relation(data: SalaHasTareaCreate, db: Session = Depends(get_db)):
    try:
        existe = db.query(SalaHasTarea).filter(
            SalaHasTarea.sala_id == data.sala_id,
            SalaHasTarea.tarea_id == data.tarea_id
        ).first()

        if existe:
            raise HTTPException(status_code=409, detail="La relación ya existe")

        nueva = SalaHasTarea(**data.dict())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear relación: {e}")
'''
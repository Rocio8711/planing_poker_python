from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.sala import Sala
from schemas.sala import SalaCreate, SalaResponse
from database import get_db

router = APIRouter(prefix="/salas", tags=["Salas"])

# Crear sala
@router.post("/", response_model=SalaResponse)
def crear_sala(sala: SalaCreate, db: Session = Depends(get_db)):
    nueva_sala = Sala(**sala.dict())
    db.add(nueva_sala)
    db.commit()
    db.refresh(nueva_sala)
    return nueva_sala

# Listar salas
@router.get("/", response_model=List[SalaResponse])
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).all()

# Obtener sala por id
@router.get("/{sala_id}", response_model=SalaResponse)
def obtener_sala(sala_id: int, db: Session = Depends(get_db)):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    if not sala:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return sala

# Actualizar sala
@router.put("/{sala_id}", response_model=SalaResponse)
def actualizar_sala(sala_id: int, datos: SalaCreate, db: Session = Depends(get_db)):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    if not sala:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    for key, value in datos.dict().items():
        setattr(sala, key, value)
    db.commit()
    db.refresh(sala)
    return sala

# Eliminar sala
@router.delete("/{sala_id}", response_model=dict)
def eliminar_sala(sala_id: int, db: Session = Depends(get_db)):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    if not sala:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    db.delete(sala)
    db.commit()
    return {"mensaje": "Sala eliminada"}


# Obtener sala por id y creador_id
@router.post("/salasusuariocreador", response_model=SalaResponse)
def sala_por_id_y_creador(sala: SalaCreate, db: Session = Depends(get_db)):
    resultado = db.query(Sala).filter(
        Sala.id == sala.id,
        Sala.creador_id == sala.creador_id
    ).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return resultado

# Obtener todas las salas de un creador
@router.post("/salasxidusuariocreado", response_model=List[SalaResponse])
def salas_por_creador(sala: SalaCreate, db: Session = Depends(get_db)):
    return db.query(Sala).filter(Sala.creador_id == sala.creador_id).all()

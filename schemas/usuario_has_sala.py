from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.usuario_has_sala import UsuarioHasSala
from schemas.usuario_has_sala import (
    UsuarioHasSalaCreate,
    UsuarioHasSalaUpdate,
    UsuarioHasSalaResponse
)

router = APIRouter(prefix="/usuario-sala", tags=["UsuarioHasSala"])


# Devuelven todos los usuarios que pertenecen a una sala
@router.get("/sala/{sala_id}", response_model=list[UsuarioHasSalaResponse])
def usuarios_de_sala(sala_id: int, db: Session = Depends(get_db)):
    return db.query(UsuarioHasSala).filter(
        UsuarioHasSala.sala_id == sala_id
    ).all()


# Crean una relación entre un usuario y una sala con estado inicial 0
@router.post("/", response_model=UsuarioHasSalaResponse)
def crear_usuario_sala(datos: UsuarioHasSalaCreate,
                       db: Session = Depends(get_db)):

    nuevo = UsuarioHasSala(
        usuario_id=datos.usuario_id,
        sala_id=datos.sala_id,
        estado=0
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


# Modifican el estado de un usuario dentro de una sala
@router.put("/estado")
def modificar_estado(datos: UsuarioHasSalaUpdate,
                     db: Session = Depends(get_db)):

    registro = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.usuario_id == datos.usuario_id,
        UsuarioHasSala.sala_id == datos.sala_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    registro.estado = datos.estado
    db.commit()

    return {"message": "Estado actualizado correctamente"}

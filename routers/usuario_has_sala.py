from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.usuario_has_sala import UsuarioHasSala

router = APIRouter(prefix="/usuario-sala", tags=["UsuarioHasSala"])


# Devuelven todos los usuarios de una sala que no han entrado (estado = 0)
@router.get("/sin-entrar/{sala_id}")
def usuarios_sin_entrar(sala_id: int, db: Session = Depends(get_db)):
    return db.query(UsuarioHasSala).filter(
        UsuarioHasSala.sala_id == sala_id,
        UsuarioHasSala.estado == 0
    ).all()


# Modifican el estado de un usuario dentro de una sala
@router.put("/estado")
def modificar_estado(usuario_id: int, sala_id: int, nuevo_estado: int,
                     db: Session = Depends(get_db)):

    registro = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.usuario_id == usuario_id,
        UsuarioHasSala.sala_id == sala_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    registro.estado = nuevo_estado
    db.commit()

    return {"message": "Estado actualizado correctamente"}


# Devuelven el estado de un usuario en una sala concreta
@router.get("/estado/{usuario_id}/{sala_id}")
def obtener_estado(usuario_id: int, sala_id: int,
                   db: Session = Depends(get_db)):

    registro = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.usuario_id == usuario_id,
        UsuarioHasSala.sala_id == sala_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"estado": registro.estado}


# Devuelven todas las salas en las que participa un usuario
@router.get("/usuario/{usuario_id}")
def salas_de_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(UsuarioHasSala).filter(
        UsuarioHasSala.usuario_id == usuario_id
    ).all()


# Devuelven todos los usuarios que pertenecen a una sala
@router.get("/sala/{sala_id}")
def usuarios_de_sala(sala_id: int, db: Session = Depends(get_db)):
    return db.query(UsuarioHasSala).filter(
        UsuarioHasSala.sala_id == sala_id
    ).all()


# Crean una relación entre un usuario y una sala con estado inicial 0
@router.post("/")
def crear_usuario_sala(usuario_id: int, sala_id: int,
                       db: Session = Depends(get_db)):

    nuevo = UsuarioHasSala(
        usuario_id=usuario_id,
        sala_id=sala_id,
        estado=0
    )

    db.add(nuevo)
    db.commit()

    return {"message": "Relación creada correctamente"}


# Eliminan la relación entre un usuario y una sala
@router.delete("/{usuario_id}/{sala_id}")
def borrar(usuario_id: int, sala_id: int,
           db: Session = Depends(get_db)):

    registro = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.usuario_id == usuario_id,
        UsuarioHasSala.sala_id == sala_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    db.delete(registro)
    db.commit()

    return {"message": "Relación eliminada correctamente"}

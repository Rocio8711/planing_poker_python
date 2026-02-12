# routers/votacion.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models.votacion import Votacion

router = APIRouter(prefix="/api/votacion", tags=["Votacion"])


@router.get("/suma/{sala_id}")
def suma_total(sala_id: int, db: Session = Depends(get_db)):
    total = db.query(func.sum(Votacion.valor))\
              .filter(Votacion.sala_id == sala_id)\
              .scalar()
    return total or 0


@router.get("/sala/{sala_id}")
def todas_las_votaciones_de_una_sala(sala_id: int, db: Session = Depends(get_db)):
    votaciones = db.query(Votacion)\
                   .filter(Votacion.sala_id == sala_id)\
                   .all()
    return votaciones


# Recuperar valor específico (usuario + sala + tarea)
@router.get("/valor/{usuario_id}/{sala_id}/{tarea_id}")
def recuperar_valor(usuario_id: int, sala_id: int, tarea_id: int, db: Session = Depends(get_db)):
    valor = db.query(Votacion.valor)\
              .filter(
                  Votacion.usuario_id == usuario_id,
                  Votacion.sala_id == sala_id,
                  Votacion.tarea_id == tarea_id
              )\
              .scalar()

    if valor is None:
        raise HTTPException(status_code=404, detail="Votación no encontrada")

    return valor


# Votación específica (devuelve el objeto entero)
@router.get("/votacion/{usuario_id}/{sala_id}/{tarea_id}")
def votacion_especifica(usuario_id: int, sala_id: int, tarea_id: int, db: Session = Depends(get_db)):
    votacion = db.query(Votacion)\
                 .filter(
                     Votacion.usuario_id == usuario_id,
                     Votacion.sala_id == sala_id,
                     Votacion.tarea_id == tarea_id
                 )\
                 .first()

    if not votacion:
        raise HTTPException(status_code=404, detail="Votación no encontrada")

    return votacion


# Crear votación
@router.post("/crear")
def crear_votacion(usuario_id: int, sala_id: int, tarea_id: int, db: Session = Depends(get_db)):

    existe = db.query(Votacion)\
               .filter(
                   Votacion.usuario_id == usuario_id,
                   Votacion.sala_id == sala_id,
                   Votacion.tarea_id == tarea_id
               )\
               .first()

    if existe:
        raise HTTPException(status_code=409, detail="La votación ya existe")

    nueva = Votacion(
        usuario_id=usuario_id,
        sala_id=sala_id,
        tarea_id=tarea_id,
        valor=0  # inicialmente 0 como en tu Spring
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


#Votaciones por sala y tarea
@router.get("/salaytarea/{sala_id}/{tarea_id}")
def votaciones_sala_tarea(sala_id: int, tarea_id: int, db: Session = Depends(get_db)):
    return db.query(Votacion)\
             .filter(
                 Votacion.sala_id == sala_id,
                 Votacion.tarea_id == tarea_id
             )\
             .all()


# Modificar valor
@router.put("/modificar")
def modificar_valor(usuario_id: int, sala_id: int, tarea_id: int, valor: int, db: Session = Depends(get_db)):

    votacion = db.query(Votacion)\
                 .filter(
                     Votacion.usuario_id == usuario_id,
                     Votacion.sala_id == sala_id,
                     Votacion.tarea_id == tarea_id
                 )\
                 .first()

    if not votacion:
        raise HTTPException(status_code=404, detail="Votación no encontrada")

    votacion.valor = valor
    db.commit()

    return {"mensaje": "Valor actualizado correctamente"}

#SPRING
#@Query("SELECT s FROM Votacion s WHERE s.votacionId.sala_id = ?1")

#FastAPI
#db.query(Votacion).filter(Votacion.sala_id == sala_id).all()

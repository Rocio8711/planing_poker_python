from sqlalchemy.orm import Session
from typing import Optional

from models.tarea import Tarea
from models.sala import Sala
from models.sala_has_tarea import SalaHasTarea

from schemas.tarea_lista_con_salas import (
    TareaListaConSalas,
    SalaSimple
)


def tarea_en_lista_de_salas(db: Session, tarea_id: int) -> Optional[TareaListaConSalas]:

    tarea = db.query(Tarea).filter(
        Tarea.id == tarea_id
    ).first()

    if not tarea:
        return None

    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.tarea_id == tarea_id
    ).all()

    lista_salas = []

    for rel in relaciones:
        sala = db.query(Sala).filter(
            Sala.id == rel.sala_id
        ).first()

        if sala:
            lista_salas.append(
                SalaSimple(
                    id=sala.id,
                    nombre=sala.nombre,
                    descripcion=sala.descripcion,
                    creador_id=sala.creador_id,
                    is_activa=sala.is_activa
                )
            )

    return TareaListaConSalas(
        id=tarea.id,
        nombre=tarea.nombre,
        url=tarea.url,
        lista_salas=lista_salas
    )
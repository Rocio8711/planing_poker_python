from sqlalchemy.orm import Session
from models.sala import Sala
from models.tarea import Tarea
from models.sala_has_tarea import SalaHasTarea
from schemas.sala_lista_tarea_finalizada_valor_final import SalaListaTareaFinalizadaValorFinal
from schemas.tarea_con_finalizada import TareaConFinalizada
from typing import List
from sqlalchemy import func


def _crear_respuesta(sala: Sala, tareas: List[SalaHasTarea], db: Session):
    lista_tareas = []
    suma_total = 0

    for rel in tareas:
        tarea = db.query(Tarea).filter(Tarea.id == rel.tarea_id).first()

        if tarea:
            lista_tareas.append(
                TareaConFinalizada(
                    id=tarea.id,
                    nombre=tarea.nombre,
                    url=tarea.url,
                    valor_final=rel.valor_final,
                    finalizada=rel.finalizada
                )
            )

            if rel.valor_final:
                suma_total += rel.valor_final

    return SalaListaTareaFinalizadaValorFinal(
        id=sala.id,
        nombre=sala.nombre,
        isActiva=sala.isActiva,
        listaTareas=lista_tareas,
        sumaDeLasTareas=suma_total
    )


#Lista completa
def sala_lista_completa(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    relaciones = db.query(SalaHasTarea).filter(SalaHasTarea.sala_id == sala_id).all()
    return _crear_respuesta(sala, relaciones, db)


#Sin iniciar (finalizada == 0)
def sala_lista_sin_iniciar(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.finalizada == 0
    ).all()
    return _crear_respuesta(sala, relaciones, db)


# En proceso (finalizada == 1)
def sala_lista_en_proceso(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.finalizada == 1
    ).all()
    return _crear_respuesta(sala, relaciones, db)


# Finalizadas (finalizada == 2)
def sala_lista_finalizada(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id,
        SalaHasTarea.finalizada == 2
    ).all()
    return _crear_respuesta(sala, relaciones, db)
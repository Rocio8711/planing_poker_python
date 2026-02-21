# services/sala_lista_tarea_service.py
from sqlalchemy.orm import Session
from models.sala import Sala
from models.tarea import Tarea
from models.sala_has_tarea import SalaHasTarea
from schemas.sala_lista_tarea import SalaListaTareaDTO


def crear_dto(sala: Sala, lista_tareas: list[Tarea]) -> SalaListaTareaDTO:
    return SalaListaTareaDTO(
        id=sala.id,
        nombre=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        is_activa=sala.isActiva,
        lista_tareas=lista_tareas
    )


def sala_con_lista_tareas(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    if not sala:
        return None

    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id
    ).all()

    lista_tareas = []

    for relacion in relaciones:
        tarea = db.query(Tarea).filter(
            Tarea.id == relacion.tarea_id
        ).first()

        if tarea:
            lista_tareas.append(tarea)

    return crear_dto(sala, lista_tareas)


#Si existe alguna tarea sin votar
def existencia_de_tareas_sin_votar(db: Session, sala_id: int):
    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id
    ).all()

    for r in relaciones:
        # Sin votar si valor_final es 0 o None
        if r.valor_final is None or r.valor_final == 0:
            return True

    return False


#Si la sala tiene tareas
def existencia_de_tareas(db: Session, sala_id: int):
    relaciones = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id
    ).all()

    return len(relaciones) > 0
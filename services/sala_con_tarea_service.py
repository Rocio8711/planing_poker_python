from sqlalchemy.orm import Session
from models.sala import Sala
from models.tarea import Tarea
from schemas.sala_con_tarea import SalaConTareaDTO


def crear_dto(sala: Sala, tarea: Tarea) -> SalaConTareaDTO:
    return SalaConTareaDTO(
        id_sala=sala.id,
        nombre_sala=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        is_activa=sala.isActiva,
        id_tarea=tarea.id,
        nombre_tarea=tarea.nombre,
        url=tarea.url
    )


def salas_con_tarea_por_id(db: Session, sala_id: int):
    lista_tareas = db.query(Tarea).all()
    sala = db.query(Sala).filter(Sala.id == sala_id).first()

    resultado = []

    for tarea in lista_tareas:
        resultado.append(crear_dto(sala, tarea))

    return resultado


def tarea_en_todas_las_salas(db: Session, tarea_id: int):
    lista_salas = db.query(Sala).all()
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()

    resultado = []

    for sala in lista_salas:
        resultado.append(crear_dto(sala, tarea))

    return resultado


def salas_tareas_todas(db: Session):
    lista_salas = db.query(Sala).all()
    lista_tareas = db.query(Tarea).all()

    resultado = []

    for sala in lista_salas:
        for tarea in lista_tareas:
            resultado.append(crear_dto(sala, tarea))

    return resultado

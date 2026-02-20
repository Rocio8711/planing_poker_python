from sqlalchemy.orm import Session
from models.sala import Sala
from models.usuario import Usuario
from schemas.sala_con_creador import SalaConCreadorDTO

def crear_dto(sala: Sala, usuario: Usuario) -> SalaConCreadorDTO:
    return SalaConCreadorDTO(
        id_sala=sala.id,
        nombre_sala=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        is_activa=sala.isActiva,
        nombre_creador=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        password=usuario.password
    )

def salas_con_creador_por_id(db: Session, creador_id: int):
    salas = db.query(Sala).filter(Sala.creador_id == creador_id).all()
    usuario = db.query(Usuario).filter(Usuario.id == creador_id).first()

    resultado = []
    if usuario:
        for sala in salas:
            resultado.append(crear_dto(sala, usuario))
    return resultado

def todas_las_salas_con_creador(db: Session):
    salas = db.query(Sala).all()
    resultado = []
    for sala in salas:
        usuario = db.query(Usuario).filter(Usuario.id == sala.creador_id).first()
        if usuario:
            resultado.append(crear_dto(sala, usuario))
    return resultado
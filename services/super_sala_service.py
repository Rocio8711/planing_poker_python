from sqlalchemy.orm import Session
from models.sala import Sala
from models.tarea import Tarea
from models.usuario import Usuario
from models.votacion import Votacion
from models.sala_has_tarea import SalaHasTarea
from models.usuario_has_sala import UsuarioHasSala

from schemas.super_dto_sala import SuperDtoSalaConListasDetareasYUsuarios
from schemas.tarea_con_finalizada import TareaConFinalizada
from schemas.usuarios_con_estado import UsuariosConEstado
from schemas.votacion import VotacionResponse


def sala_super_completa(db: Session, sala_id: int):

    sala = db.query(Sala).filter(Sala.id == sala_id).first()

    if not sala:
        return None

    # USUARIOS
    lista_usuarios = []
    relaciones_usuario = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.sala_id == sala_id
    ).all()

    for rel in relaciones_usuario:
        usuario = db.query(Usuario).filter(Usuario.id == rel.usuario_id).first()
        if usuario:
            lista_usuarios.append(
                UsuariosConEstado(
                    usuario_id=usuario.id,
                    nombreUsuario=usuario.nombre,
                    apellido=usuario.apellido,
                    email=usuario.email,
                    estado=rel.estado
                )
            )

    # TAREAS
    lista_tareas = []
    suma_total = 0.0

    relaciones_tarea = db.query(SalaHasTarea).filter(
        SalaHasTarea.sala_id == sala_id
    ).all()

    for rel in relaciones_tarea:
        tarea = db.query(Tarea).filter(Tarea.id == rel.tarea_id).first()
        if tarea:
            lista_tareas.append(
                TareaConFinalizada(
                    id=tarea.id,
                    nombre=tarea.nombre,
                    url=tarea.url,
                    finalizada=rel.finalizada,
                    valor_final=rel.valor_final
                )
            )

            if rel.valor_final:
                suma_total += float(rel.valor_final)

    # VOTACIONES
    lista_votaciones = db.query(Votacion).filter(
        Votacion.sala_id == sala_id
    ).all()

    lista_votaciones_schema = [
        VotacionResponse.model_validate(v) for v in lista_votaciones
    ]

    return SuperDtoSalaConListasDetareasYUsuarios(
        id=sala.id,
        nombre=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        isActiva=sala.isActiva,
        listaTareas=lista_tareas,
        listaUsuario=lista_usuarios,
        listaVotacion=lista_votaciones_schema,
        sumaDeLasTareas=suma_total
    )
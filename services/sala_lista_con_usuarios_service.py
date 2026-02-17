from sqlalchemy.orm import Session
from models.sala import Sala
from schemas.sala_lista_con_usuarios import SalaListaConUsuarios, UsuariosConEstado

def sala_con_usuarios_sin_entrar(db: Session, sala_id: int) -> SalaListaConUsuarios:
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    dto = SalaListaConUsuarios(
        id=sala.id,
        nombre=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        is_activa=sala.is_activa,
        lista_usuarios=[]
    )
    for uhs in sala.usuarios:
        if uhs.estado == 0:
            dto.lista_usuarios.append(
                UsuariosConEstado(
                    usuario_id=uhs.usuario.id,
                    nombre_usuario=uhs.usuario.nombre,
                    apellido=uhs.usuario.apellido,
                    estado=uhs.estado
                )
            )
    return dto

def sala_con_usuarios(db: Session, sala_id: int) -> SalaListaConUsuarios:
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    dto = SalaListaConUsuarios(
        id=sala.id,
        nombre=sala.nombre,
        descripcion=sala.descripcion,
        fecha=sala.fecha,
        creador_id=sala.creador_id,
        is_activa=sala.is_activa,
        lista_usuarios=[]
    )
    for uhs in sala.usuarios:
        dto.lista_usuarios.append(
            UsuariosConEstado(
                usuario_id=uhs.usuario.id,
                nombre_usuario=uhs.usuario.nombre,
                apellido=uhs.usuario.apellido,
                estado=uhs.estado
            )
        )
    return dto

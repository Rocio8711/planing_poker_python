from sqlalchemy.orm import Session
from models.usuario import Usuario
from models.usuario_has_sala import UsuarioHasSala
from schemas.usuarios_con_estado import UsuariosConEstado
from typing import List


def usuarios_con_estado_por_sala(db: Session, sala_id: int) -> List[UsuariosConEstado]:

    relaciones = db.query(UsuarioHasSala).filter(
        UsuarioHasSala.sala_id == sala_id
    ).all()

    resultado = []

    for rel in relaciones:
        usuario = db.query(Usuario).filter(
            Usuario.id == rel.usuario_id
        ).first()

        if usuario:
            resultado.append(
                UsuariosConEstado(
                    usuario_id=usuario.id,
                    nombreUsuario=usuario.nombre,
                    apellido=usuario.apellido,
                    email=usuario.email,
                    estado=rel.estado
                )
            )

    return resultado
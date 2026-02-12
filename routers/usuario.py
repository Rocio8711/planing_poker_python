from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/api/users", tags=["Usuarios"])


#Ahora vamos a traducir los métodos del controller:


# Crear usuario
@router.post("/", response_model=UsuarioResponse)
def create_user(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Usuario ya existe")
    nuevo_usuario = Usuario(**user.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Obtener usuario por ID
@router.get("/{user_id}", response_model=UsuarioResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Listar todos los usuarios
@router.get("/", response_model=List[UsuarioResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

# Credenciales: login
@router.post("/credencial", response_model=UsuarioResponse)
def login(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(
        Usuario.email == user.email,
        Usuario.password == user.password
    ).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")
    return db_user

# Modificar usuario
@router.put("/{user_id}", response_model=UsuarioResponse)
def update_user(user_id: int, user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_user.nombre = user.nombre
    db_user.apellido = user.apellido
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

# Borrar usuario
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado"}

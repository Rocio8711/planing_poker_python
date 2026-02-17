from fastapi import FastAPI
from database import engine
from models.base import Base

import models.sala
import models.tarea
import models.usuario
import models.votacion


from routers.sala import router as sala_router
from routers.tarea import router as tarea_router
from routers.usuario import router as usuario_router
from routers.votacion import router as votacion_router
from routers.sala_has_tarea import router as sala_has_tarea_router
from routers.usuario_has_sala import router as usuario_has_sala_router
from routers.sala_con_tarea import router as sala_con_tarea_router
from routers.sala_lista_con_usuarios import router as sala_lista_con_usuarios_router

app = FastAPI(title="Planning Poker API")

Base.metadata.create_all(bind=engine)



app.include_router(sala_router)
app.include_router(tarea_router)
app.include_router(usuario_router)
app.include_router(votacion_router)
app.include_router(sala_has_tarea_router)
app.include_router(usuario_has_sala_router)
app.include_router(sala_con_tarea_router)
app.include_router(sala_lista_con_usuarios_router)

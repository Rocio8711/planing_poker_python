from fastapi import FastAPI
from database import engine
from models.base import Base

import models.sala
import models.tarea

from routers.sala import router as sala_router
from routers.tarea import router as tarea_router

app = FastAPI(title="Planning Poker API")

Base.metadata.create_all(bind=engine)

app.include_router(sala_router)
app.include_router(tarea_router)

from fastapi import FastAPI
from models.sala import Base
from database import engine
from routers.sala import router as sala_router

app = FastAPI(title="Planning Poker API")

Base.metadata.create_all(bind=engine)

app.include_router(sala_router)

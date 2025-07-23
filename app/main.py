from fastapi import FastAPI
from app.controller import route
from app.model import Base
from app.database import engine

app = FastAPI()
app.include_router(route)

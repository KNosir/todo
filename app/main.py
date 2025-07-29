from fastapi import FastAPI
from app.controller import route

app = FastAPI()
app.include_router(route)

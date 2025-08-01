from fastapi import FastAPI
from app.controller import route
from app.database import engine
from app.model import Base

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
app.include_router(route)

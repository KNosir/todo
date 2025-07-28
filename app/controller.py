from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.service import ser_get_todo, ser_create_todo, ser_put_todo, ser_delete_todo
from app.schema import TodoCreate, TodoGet, TodoPut
from app.model import Todo

route = APIRouter()


@route.get("/")
async def main():
    return JSONResponse({"message": "ok"})


@route.get("/todos", response_model=list[TodoGet])
async def route_get_todos(db: AsyncSession = Depends(get_db)):
    return await ser_get_todo(0, db)


@route.get("/todo/{id}", response_model=list[TodoGet])
async def get_todo_by_id(id: int, db: AsyncSession = Depends(get_db)):
    if id == 0:
        return await ser_get_todo(-1, db)
    return await ser_get_todo(id, db)


@route.post("/todo", response_model=TodoGet)
async def route_create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await ser_create_todo(Todo(**todo.model_dump()), db)


@route.put("/todo/{id}", response_model=TodoGet)
async def route_put_todo(id: int, todo: TodoPut, db: AsyncSession = Depends(get_db)):
    return await ser_put_todo(id, todo, db)


@route.delete("/todo/{id}")
async def route_delete_todo(id: int, db: AsyncSession = Depends(get_db)):
    return await ser_delete_todo(id, db)


from fastapi import HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from app.model import Todo
from app.schema import TodoPut
from datetime import datetime


async def ser_get_todo(id: int, db:  AsyncSession):
    if id == 0:
        condition = and_(Todo.is_active == True,
                         Todo.deleted_at == None)
    else:
        condition = and_(Todo.is_active == True,
                         Todo.deleted_at == None,
                         Todo.id == id)

    result = await db.execute(select(Todo).where(condition))
    return result.scalars().all()


async def ser_create_todo(todo: Todo, db: AsyncSession):
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def ser_put_todo(todo_id: int, todo: TodoPut, db: AsyncSession):
    conditions = and_(Todo.id == todo_id,
                      Todo.is_active == True,
                      Todo.deleted_at == None)
    result = await db.execute(select(Todo).where(conditions))
    once_todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for field, value in todo.model_dump(exclude_unset=True).items():
        setattr(once_todo, field, value)

    setattr(once_todo, "updated_at", datetime.utcnow())
    await db.commit()
    await db.refresh(once_todo)

    return once_todo


async def ser_delete_todo(todo_id: int, db: AsyncSession):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    once_todo = result.scalar_one_or_none()

    if not once_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    setattr(once_todo, "deleted_at", datetime.utcnow())
    await db.commit()
    await db.refresh(once_todo)

    return {"message": "done"}

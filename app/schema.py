from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoGet(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class TodoPut(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    updated_at: Optional[datetime] = None

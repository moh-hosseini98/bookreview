from sqlmodel import SQLModel,Field
from typing import Optional
import uuid
from datetime import date, datetime

from auth.schemas import UserRead

class BookBase(SQLModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookRead(BookBase):
    uid : uuid.UUID
    created_at : datetime
    updated_at : datetime


class BookReadWithUser(BookRead):
    user : UserRead 

class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: str | None = Field(default=None,min_length=1,max_length=255)
    
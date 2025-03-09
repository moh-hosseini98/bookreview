from sqlmodel import SQLModel,Field
from typing import Optional
import uuid
from datetime import date, datetime



class ReviewBase(SQLModel):
    uid: uuid.UUID
    rating: int = Field(le=5)
    review_text: str
    user_uid: uuid.UUID | None
    book_uid: uuid.UUID | None
    created_at: datetime

class ReviewCreate(SQLModel):
    rating : int = Field(le=5)
    review_text : str

class ReviewUpdate(SQLModel):
    review_text : str
    
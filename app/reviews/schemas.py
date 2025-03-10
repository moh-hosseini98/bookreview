from sqlmodel import SQLModel,Field
from typing import Optional
import uuid
from datetime import date, datetime

from auth.schemas import UserRead
from books.schemas import BookReadWithUser



class ReviewBase(SQLModel):
    uid: uuid.UUID
    rating: int = Field(le=5)
    review_text: str
    created_at: datetime
    

class ReviewCreate(SQLModel):
    rating : int = Field(le=5)
    review_text : str

class ReviewUpdate(SQLModel):
    review_text : str

class ReviewReadWithUser(ReviewBase):
    user : UserRead
    #book : BookReadWithUser
  
  
    
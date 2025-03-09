from sqlmodel import Column, Field, Relationship, SQLModel
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

from auth.models import User
from books.models import Book



class Review(SQLModel,table=True):

    __tablename__ = "reviews"

    uid : uuid.UUID  = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            default=uuid.uuid4,
            nullable=False
        )
    )
    rating : int = Field(le=5)
    review_text : str = Field(sa_column=Column(pg.VARCHAR,nullable=False))
    user_uid : uuid.UUID | None = Field(default=None,foreign_key="users.uid")
    user : User | None = Relationship(back_populates="reviews")
    book_uid : uuid.UUID | None = Field(default=None,foreign_key="books.uid")
    book : Book | None = Relationship(back_populates="reviews")
    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
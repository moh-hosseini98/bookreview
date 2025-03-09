from sqlmodel import Column, Field, Relationship, SQLModel
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

from auth.models import User

class Book(SQLModel,table=True):

    __tablename__ = "books"

    uid : uuid.UUID  = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            default=uuid.uuid4,
            nullable=False
        )
    )
    title : str
    author : str
    publisher : str
    published_date : str
    page_count : int
    language : str
    user_uid : uuid.UUID | None = Field(default=None,foreign_key="users.uid",ondelete="CASCADE")
    user : User | None = Relationship(back_populates="books")
    reviews: list["Review"] = Relationship(
        back_populates="book", sa_relationship_kwargs={"lazy": "selectin"}
    )

    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))

    def __repr__(self):
        return f"<Book {self.title}>"



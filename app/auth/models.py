from sqlmodel import Column, Field, Relationship, SQLModel
import sqlalchemy.dialects.postgresql as pg
from pydantic import EmailStr
import uuid
from datetime import datetime

class User(SQLModel,table=True):

    __tablename__ = "users"

    uid : uuid.UUID  = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            default=uuid.uuid4,
            nullable=False
        )
    )
    email: EmailStr = Field(nullable=False,sa_column_kwargs={"unique": True})
    full_name : str | None = Field(default=None,max_length=255)
    hashed_password : str
    books : list["Book"] = Relationship(
        back_populates="user",sa_relationship_kwargs={"lazy": "selectin"}
    )
    reviews : list["Review"] = Relationship(
        back_populates="user",sa_relationship_kwargs={"lazy":"selectin"}
    )
    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))


    def __repr__(self) -> str:
        return f"<User {self.email}>"
    
from sqlmodel import SQLModel,Field
from pydantic import EmailStr
import uuid
from datetime import date, datetime


class UserBase(SQLModel):
    email : EmailStr
    full_name : str | None = Field(default=None,max_length=255)
   
    
class UserCreate(UserBase):
    password : str = Field(min_length=6)


class UserRead(UserBase):
    uid : uuid.UUID

class UserUpdate(SQLModel):
    pass

class UserLogin(SQLModel):
    email : EmailStr
    password : str = Field(min_length=6)

class Token(SQLModel):
    access_token: str
    token_type: str = "Bearer"
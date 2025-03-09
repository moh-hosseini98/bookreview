from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from pydantic import EmailStr
from datetime import datetime

from .models import User
from .schemas import UserCreate
from .utils import generate_hashed_password

class UserService:
    async def get_user_by_email(self,email : EmailStr , session : AsyncSession):
        stmt = select(User).where(User.email == email)
        result = await session.exec(stmt)
        user = result.first()
        return user

    async def user_exists(self , email : EmailStr , session : AsyncSession):
        user = await self.get_user_by_email(email,session)
        return True if user is not None else False

    async def create_user(self,user_data : UserCreate , session : AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.hashed_password = generate_hashed_password(user_data_dict["password"])

        session.add(new_user)
        await session.commit()
        return new_user



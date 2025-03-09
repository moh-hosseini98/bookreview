from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from core.db import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from datetime import datetime

from .service import UserService
from .models import User
from .schemas import UserCreate,UserRead,UserLogin,Token
from .utils import verify_password,create_access_token,get_current_user


auth_router = APIRouter()
user_service = UserService()

@auth_router.post(
    "/signup",response_model=UserRead,status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data : UserCreate , 
    session : AsyncSession = Depends(get_session)
):
    user_exists = await user_service.user_exists(user_data.email,session)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists"
        )
    new_user = await user_service.create_user(user_data,session)

    return new_user    

@auth_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=Token
)
async def login_user(
    user_data : UserLogin, 
    session : AsyncSession = Depends(get_session)
):
    user = await user_service.get_user_by_email(user_data.email,session)
    if user is not None:
        password_valid = verify_password(user_data.password,user.hashed_password)
        if password_valid:
            access_token = create_access_token(
                email=user.email,user_uid=str(user.uid)
            )
            return {"access_token":access_token}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid Email Or Password"
    )        

@auth_router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return user
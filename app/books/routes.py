import uuid
from fastapi import APIRouter,Depends,HTTPException,status
from core.db import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from datetime import datetime

from .service import BookService
from .models import Book
from .schemas import BookCreate,BookRead,BookUpdate,BookReadWithUser
from auth.utils import get_current_user





book_router = APIRouter()
book_service = BookService()

@book_router.get("/",response_model=list[Book])
async def get_all_books(
    session : AsyncSession = Depends(get_session),
):

    books = await book_service.get_all_books(session)
    return books

@book_router.get(
    "/user/{user_uid}",response_model=list[Book]
)
async def get_user_books(
    user_uid : uuid.UUID, 
    session : AsyncSession = Depends(get_session)
):
    books = await book_service.get_user_books(user_uid,session)
    return books

@book_router.post("/",response_model = Book)
async def create_book(
    book_data : BookCreate,
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session)
):

    new_book = await book_service.create_book(book_data , user.get('user_uid'), session)
    return new_book

@book_router.get("/{book_uid}",response_model=BookReadWithUser)
async def get_book(
    book_uid : uuid.UUID , 
    session : AsyncSession = Depends(get_session)
):

    book = await book_service.get_book_with_user(book_uid,session)
    if book is None:
        raise HTTPException(
            status_code = 404,
            detail = " Book not found"
        )
    return book 


@book_router.patch("/{book_uid}",response_model=Book)
async def update_book(
    book_uid : uuid.UUID, 
    update_data : BookUpdate, 
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session),
):

    book =  await book_service.updated_book(book_uid,user.get('user_uid'),update_data,session)
       
    return book    


@book_router.delete("/{book_uid}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_uid : uuid.UUID , 
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session),
):

    book =  await book_service.delete_book(book_uid,user.get('user_uid'),session)
        
    return {}


    
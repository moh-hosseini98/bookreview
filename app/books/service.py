import uuid
from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from sqlalchemy.orm import joinedload,selectinload
from datetime import datetime

from .models import Book
from .schemas import BookCreate,BookUpdate


class BookService:

    """ this class provides methods to CRUD books """

    async def get_all_books(self , session : AsyncSession):
        
        stmt = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(stmt)

        return result.all()

    async def get_user_books(
        self,user_uid : uuid.UUID , session : AsyncSession
    ):
        stmt = (
            select(Book)
            .where(Book.user_uid == user_uid)
            .order_by(desc(Book.created_at))
        )    

        result = await session.exec(stmt)

        return result.all()

    async def create_book(
        self, book_data: BookCreate, user_uid: uuid.UUID, session: AsyncSession
    ):
        book_data_dict = book_data.model_dump()
        new_book = Book(
            **book_data_dict
        )
        
        new_book.user_uid = user_uid
        session.add(new_book)
        await session.commit()

        return new_book

    async def get_book(
        self , book_uid : uuid.UUID, session : AsyncSession
    ):
        
        stmt = select(Book).where(Book.uid == book_uid)
        result = await session.exec(stmt)
        book = result.first() 

        return book if book is not None else None

    async def get_book_with_user(
        self,book_uid : uuid.UUID, session : AsyncSession
    ):
        stmt = (
            select(Book)
            .options(selectinload(Book.user))
            .where(Book.uid == book_uid)
        )    
        
        result = await session.exec(stmt)
        book = result.first()

        return book if book is not None else None

    async def updated_book(
        self , book_uid : uuid.UUID ,user_uid : uuid.UUID,update_data : BookUpdate, session : AsyncSession
    ):
        book = await self.get_book(book_uid,session)

        if book.user_uid != user_uid:
            raise HTTPException(
                status_code=403,
                detail="Only the creator can edit"
            )

        if book is not None:
            update_data_dict = update_data.model_dump()
            for k,v in update_data_dict.items():
                setattr(book,k,v)
            await session.commit()
            return book

        return None

    async def delete_book(
        self , book_uid : uuid.UUID , user_uid : uuid.UUID ,session : AsyncSession
    ):
        book =  await self.get_book(book_uid,session)
        
        if book.user_uid != user_uid:
            raise HTTPException(
                status_code=403,
                detail="Only the creator can delete"
            )

        if book is not None:
            await session.delete(book)    
            await session.commit()
            return {}

        return None    
        




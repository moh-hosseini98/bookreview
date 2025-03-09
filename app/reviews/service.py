import uuid
from fastapi import HTTPException,status
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from sqlalchemy.orm import joinedload
from datetime import datetime

from books.models import Book
from books.service import BookService
from auth.service import UserService


from .models import Review
from .schemas import ReviewCreate,ReviewUpdate


book_service = BookService()
user_service = UserService()

class ReviewService:
    """ this class provides methods to CRUD reviews """

    async def create_review(
        self, 
        book_uid : uuid.UUID,
        user_uid : uuid.UUID,
        review_data : ReviewCreate,
        session : AsyncSession
    ):
        book = await book_service.get_book(book_uid, session)

        if not book:
            raise HTTPException(
                detail="Book not found", status_code=status.HTTP_404_NOT_FOUND
            )

        review_dict = review_data.model_dump()
        new_review = Review(**review_dict)

        new_review.user_uid = user_uid
        new_review.book = book

        session.add(new_review)
        await session.commit()

        return new_review

    async def get_all_reviews(
        self, 
        book_uid : uuid.UUID,
        session : AsyncSession
    ):
        
        stmt = select(Review).where(Review.book_uid == book_uid)
        result = await session.exec(stmt)
        return result.all()

    async def get_review(
        self,
        book_uid : uuid.UUID,
        review_uid : uuid.UUID,
        session : AsyncSession
    ):
        stmt = (
            select(Review)
            .where(Review.book_uid == book_uid)
            .where(Review.uid == review_uid)
        )
        result = await session.exec(stmt)
        review = result.first()

        return review if review is not None else None
        
    async def update_review(
        self,
        book_uid : uuid.UUID,
        review_uid : uuid.UUID,
        user_uid : uuid.UUID,
        updated_data : ReviewUpdate,
        session : AsyncSession
    ):
        review = await self.get_review(book_uid,review_uid,session)

        if review is None:
            raise HTTPException(
                status_code=404,
                detail="Review not found"
            )
        if review.user_uid != user_uid:
            raise HTTPException(
                status_code=403,
                detail="Only the creator can Update the review"
            )    

        updated_data_dict = updated_data.model_dump()
        for k,v in updated_data_dict.items():
            setattr(review,k,v)    

        await session.commit()
        return review        

    async def delete_review(
        self,
        book_uid : uuid.UUID,
        review_uid : uuid.UUID,
        user_uid : uuid.UUID,
        session : AsyncSession
    ):
        
        review = await self.get_review(book_uid,review_uid,session)

        if review is None:
            raise HTTPException(
                status_code=404,
                detail="Review not found"
            )

        if review.user_uid != user_uid:
            raise HTTPException(
                status_code=403,
                detail="Only the creator can delete the review"
            )

        await session.delete(review)
        await session.commit()
        return {"message": "Review deleted successfully"}

       

        

    


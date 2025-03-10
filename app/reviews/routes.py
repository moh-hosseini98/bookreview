import uuid
from auth.utils import get_current_user
from fastapi import APIRouter,Depends,HTTPException,status
from core.db import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from datetime import datetime

from .service import ReviewService
from .models import Review
from .schemas import ReviewBase,ReviewCreate,ReviewUpdate,ReviewReadWithUser




review_service = ReviewService()
review_router = APIRouter()

@review_router.post(
    "/books/{book_uid}/reviews"
)
async def create_review(
    *,
    book_uid : uuid.UUID,
    review_data : ReviewCreate,
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session)
):
    new_review = await review_service.create_review(
        book_uid,user.get('user_uid'),review_data,session
    )
    return new_review

@review_router.get(
    "/books/{book_uid}/reviews"
)
async def get_all_reviews(
    book_uid : uuid.UUID,
    session : AsyncSession= Depends(get_session)
):
    reviews = await review_service.get_all_reviews(book_uid,session)
    return reviews


@review_router.get(
    "/books/{book_uid}/reviews/{review_uid}"
)
async def get_review(
    book_uid : uuid.UUID,
    review_uid : uuid.UUID,
    session : AsyncSession = Depends(get_session)
):
    review = await review_service.get_review(book_uid,review_uid,session)
    if review is None:
        raise HTTPException(
            status_code=404,
            detail="review not found"
        )
    return review

@review_router.get(
    "/reviews/{review_uid}",
    response_model=ReviewReadWithUser
)
async def get_review_with_user(
    review_uid : uuid.UUID,
    session : AsyncSession = Depends(get_session)
):
    review = await review_service.get_review_with_user(review_uid,session)
    if review is None:
        raise HTTPException(
            status_code=404,
            detail="review not found"
        )
    return review

@review_router.patch(
    "/books/{book_uid}/reviews/{review_uid}"
)
async def update_review(
    book_uid : uuid.UUID,
    review_uid : uuid.UUID,
    update_data : ReviewUpdate,
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session),
):
    review = await review_service.update_review(book_uid,review_uid,user.get('user_uid'),update_data,session)
    return review


@review_router.delete(
    "/books/{book_uid}/reviews/{review_uid}"
)
async def delete_review(
    book_uid : uuid.UUID,
    review_uid : uuid.UUID,
    user = Depends(get_current_user),
    session : AsyncSession = Depends(get_session),
):
    review = await review_service.delete_review(book_uid,review_uid,user.get('user_uid'),session)
    return review



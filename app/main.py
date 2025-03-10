from fastapi import FastAPI
from books.routes import book_router
from auth.routes import auth_router
from reviews.routes import review_router
from core.db import init_db







app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version='v1',
)

@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(book_router,prefix=f"/api/{app.version}/books", tags=["books"])
app.include_router(review_router, prefix=f"/api/{app.version}", tags=["reviews"])
app.include_router(auth_router,prefix=f"/api/{app.version}/auth",tags=["auth"])
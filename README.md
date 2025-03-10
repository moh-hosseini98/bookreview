 ### 🚀 Features

FastAPI framework for high performance
PostgreSQL database integration
JWT authentication
SQLModel
Docker containerization
Docker & Docker Compose setup

#### HTTP request CRUD

## BOOK CRUD:
- GET: Read and retrieve data. Supports query and path parameters.
- all books : @app.get("/books/")
- one book : @app.get("/books/{book_uid}")
- POST: Create resources and submit data.
- @app.post("/books/")
- PATCH: Partially update resources, modifying only the fields that need changes without affecting others.
- @app.patch("/books/{book_uid}")
- DELETE: Remove resources.
- @app.delete("/books/{book_uid}")

## REVIEW CRUD:
- GET: Read and retrieve data. Supports query and path parameters.
- all reviews for  book : @app.get("/books/{book_uid}/reviews")
- retrieve one review for book : @app.get("/books/{book_uid}/reviws/{review_uid}")
- POST: Create resources and submit data.
- @app.post("/books/{book_uid}/reviews")
- PATCH: Partially update resources, modifying only the fields that need changes without affecting others.
- @app.patch("/books/{book_uid}/reviews/{review_uid}")
- DELETE: Remove resources.
- @app.delete("/books/{book_uid}/reviews/{review_uid}")
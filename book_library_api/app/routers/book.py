from fastapi import APIRouter, HTTPException
from app.database.mongo import db
from app.models.book import Book

router = APIRouter()

@router.get("/books")
async def get_books():
    return await db.books.find().to_list(100)

@router.post("/books")
async def add_book(book: Book):
    result = await db.books.insert_one(book.dict())
    return {"id": str(result.inserted_id)}

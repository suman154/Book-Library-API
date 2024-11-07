from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    published_date: Optional[str]
    isbn: Optional[str]
    pages: Optional[int]
    cover_url: Optional[str]
    language: Optional[str]

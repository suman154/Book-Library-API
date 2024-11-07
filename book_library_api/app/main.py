from fastapi import FastAPI
from . import routers
from app.routers import book

app = FastAPI()

# Include routers
app.include_router(book.router)

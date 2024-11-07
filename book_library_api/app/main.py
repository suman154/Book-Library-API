from fastapi import FastAPI
from routers import books

app = FastAPI()

# Include routers
app.include_router(books.router)

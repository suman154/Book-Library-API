📚 Book Library API
A FastAPI-based API for managing a personal book library with MongoDB, JWT authentication, and Google Books integration.

✨ Features
CRUD Operations: Add, update, delete, and retrieve books
External API Integration: Fetch additional details from Google Books API
JWT Authentication: Secure access to endpoints
Dockerized: Easily deploy with Docker & Docker Compose


🛠️ Tech Stack
Python + FastAPI
MongoDB for database
Docker for containerization
Google Books API for additional book info

🚀 Getting Started
Clone the Repository
```
git clone https://github.com/your-username/book_library_api.git
cd book_library_api
```

```
Install Dependencies
pip install -r requirements.txt

```

```
Set Up Environment Variables (create a .env file)
MONGO_URI=mongodb://<your_mongo_uri>
SECRET_KEY=<your_secret_key>
```

```
Run with Docker
docker-compose up --build
The API is now available at http://localhost:8000.
```

🔗 Endpoints
GET /books - List all books
POST /books - Add a book
GET /books/{id} - Get book by ID
PUT /books/{id} - Update book
DELETE /books/{id} - Delete book
GET /books/search/{title} - Search for a book (Google Books API)

🐳 Deploy with Docker
```
docker-compose up --build
```
🧪 Run Tests
```
pytest tests
```
Happy coding! 📚







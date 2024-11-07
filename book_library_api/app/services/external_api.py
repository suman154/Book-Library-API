import requests

def fetch_book_details(title: str):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title}")
    return response.json().get("items", [])

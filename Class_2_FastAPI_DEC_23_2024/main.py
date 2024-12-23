# Import necessary modules from FastAPI
from fastapi import FastAPI, Body
from .validators import BookRequest

# Sample data to work with
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
]

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get('/api-endpoint')
async def first_api():
    return {'message': 'Hello Eric!'}

# Define a GET endpoint to return all books
@app.get('/')
async def version_one():
    return BOOKS

# Define a GET endpoint with a dynamic parameter
@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return {"dynamic_param": dynamic_param}

# Define a GET endpoint to read a book by its title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

# Define a GET endpoint to read books by category using query parameters
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Define a GET endpoint to read books by author and category using query parameters
@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Define a POST endpoint to create a new book using Body
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

# Define a POST endpoint to create a new book using a Pydantic model
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = book_request.dict()
    BOOKS.append(new_book)
    return new_book

# Define a PUT endpoint to update an existing book
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
            return updated_book
    return {"message": "Book not found"}

# Define a DELETE endpoint to delete a book by its title
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}
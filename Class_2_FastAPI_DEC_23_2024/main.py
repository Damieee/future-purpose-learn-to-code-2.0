# Import necessary modules from FastAPI
from fastapi import FastAPI, Body, Query
from .validators import CreateBookDTO, UpdateBookAuthorDto
from .data import BOOKS
# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get('/')
async def first_api():
    return {'message': 'Hello, there! 🌟'}

# Define a GET endpoint to return all books
@app.get('/books')
async def get_all_books():
    return BOOKS

# Define a GET endpoint to read books by category using query parameters
@app.get("/books/")
async def read_books_by_category(category: str = Query(...)):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Define a GET endpoint to read a book by its title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}


# Define a GET endpoint to read books by author and category using query parameters
@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str = Query(...)):
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
async def create_book(book_request: CreateBookDTO):
    new_book = book_request.model_dump()
    BOOKS.append(new_book)
    return new_book


# Define a PUT endpoint to update an existing book
@app.patch("/books/{title}/update_book_author")
async def update_book(title: str, updated_book: UpdateBookAuthorDto):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == title.casefold():
            BOOKS[i]["author"] = updated_book.author
            return BOOKS[i]
    return {"message": f"Book with title  {title} not found"}

# Define a DELETE endpoint to delete a book by its title
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}
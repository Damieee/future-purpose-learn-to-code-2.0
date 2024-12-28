# Import necessary modules from FastAPI
from fastapi import FastAPI, Body, Query, Path
from .validators import CreateBookDTO
from .data import BOOKS

# Create an instance of FastAPI
app = FastAPI()

# Define a GET endpoint to search for books by keyword in title or author
@app.get("/books/search")
async def search_books(keyword: str = Query(...)):
    matched_books = [
        book for book in BOOKS if keyword.casefold() in book["title"].casefold() or keyword.casefold() in book["author"].casefold()
    ]
    return matched_books

# Define a GET endpoint to get the count of books in a specific category
@app.get("/books/count")
async def count_books_by_category(category: str = Query(...)):
    count = sum(1 for book in BOOKS if book["category"].casefold() == category.casefold())
    return {"category": category, "count": count}

# Define a PUT endpoint to update the category of a book by its title
@app.put("/books/{book_title}/update_category")
async def update_book_category(book_title: str = Path(...), category: str = Body(...)):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book["category"] = category
            return book
    return {"message": f"Book with title '{book_title}' not found"}

# Define a PATCH endpoint to update the title of a book
@app.patch("/books/{book_title}/update_title")
async def update_book_title(book_title: str = Path(...), new_title: str = Body(...)):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book["title"] = new_title
            return book
    return {"message": f"Book with title '{book_title}' not found"}

# Define a DELETE endpoint to delete all books by a specific author
@app.delete("/books/delete_by_author")
async def delete_books_by_author(author: str = Query(...)):
    global BOOKS
    books_to_delete = [book for book in BOOKS if book["author"].casefold() == author.casefold()]
    BOOKS = [book for book in BOOKS if book["author"].casefold() != author.casefold()]
    return {"message": f"{len(books_to_delete)} books by author '{author}' have been deleted"}

# Define a POST endpoint to create multiple books at once
@app.post("/books/bulk_create")
async def bulk_create_books(new_books: list[CreateBookDTO]):
    created_books = [book.model_dump() for book in new_books]
    BOOKS.extend(created_books)
    return created_books

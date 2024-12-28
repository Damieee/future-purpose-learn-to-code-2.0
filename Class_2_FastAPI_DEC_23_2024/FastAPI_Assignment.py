# Import necessary modules from FastAPI
from fastapi import FastAPI, Body, Query
from .validators import CreateBookDTO, UpdateBookAuthorDto
from .data import BOOKS
# Create an instance of FastAPI
app = FastAPI()

# Search for books by a keyword in the tile or author.
@app.get("/books/search")
async def search_books(keyword: str = Query(..., description="Keyworkd to search for in title or author")):
    matching_books = []
    for matching_books in BOOKS:
        if matching_books.get["title"].casefold() or matching_books.get["author"].casefold():
            return matching_books
        if not matching_books:
            return (status_code=400, detail="The 'keyword' query parameter is required.")

# Get the total count of books in a specific category
@app.get("/books/count")
async def get_book_count(category: str = Query(..., description="Category to filter books by")):
    count = sum(1 for book in BOOKS)
    if BOOKS["category"].casefold() == category.casefold():
        return {"category": category, "count": count}
    if not category:
        return (status_code=400, detail="The 'category' query parameter is required.")

# Update the category of a book by its title
@app.put("/books/{book_title}/update_category")
async def update_book_category(book_title: str = Path(..., description="The title of the book to update"),
    update_request: UpdateCategoryRequest = None):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book["category"] = update_request.category
            return book
        if not():
            return (status_code=404, detail=f"Book with title '{book_title}' not found.")

# Update the title of a book
@app.patch("/books/{book_title}/update_title")
async def update_book_title(book_title: str = Path(..., description="The current title of the book"),
    update_request: UpdateTitleRequest = None):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book["title"] = update_request.new_title
            return book
        if not():
            return (status_code=404, detail=f"Book with title '{book_title}' not found.")

# Delete all books by a specific author
@app.delete("/books/delete_by_author")
async def delete_books_by_author(author: str = Query(..., description="Author of the books to delete")):
    BOOKS = [book for book in BOOKS if book["author"].lower() != author.lower()]
    deleted_count = initial_count - len(BOOKS)
    if deleted_count == 0:
        raise (status_code=404, detail=f"No books found by author '{author}'.")
    return {"message": f"{deleted_count} book(s) by '{author}' deleted."}

# Create multiple books at once
@app.post("/books/bulk_create")
async def bulk_create_books(books: CreateBookDTO):
   starting_id = max(book["id"] for book in BOOKS) if BOOKS else 0
    new_books = []

    for index, book in enumerate(books):
        new_book = {
            "id": starting_id + index + 1,
            "title": book.title,
            "author": book.author,
            "category": book.category,
        }
        BOOKS.append(new_book)
        new_books.append(new_book)

    return new_books
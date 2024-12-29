# Import necessary modules from FastAPI
from fastapi import FastAPI, Body, Query, Path
from .validators import CreateBookDTO, UpdateBookAuthorDto
from .data import BOOKS
from pydantic import BaseModel

#FastAPI Instance

app = FastAPI()


#route 1: Get all books
@app.get("/books/search/")
def search_books(keyword: str = Query(..., description="Search for books by a keyword in the title or author.")):
        books_to_return = [
        book for book in BOOKS
            if keyword.casefold() in book["title"].casefold() or keyword.casefold() in book["author"].casefold()
]
        return books_to_return



#route 2: Get anumber of  books in a specific category
@app.get("/books/count/")
async def count_of_books(category: str = Query(..., description="Get the total count of books in a specific category")):
    total_count_of_books = 0

    for book in BOOKS:
            if category.casefold() in book["category"].casefold():
                total_count_of_books += 1
    return {"category": category, "count": total_count_of_books} 

#route 3: Update the category of a book by its title.
@app.put("/books/{book_title}/update_category")
def update_book_category(book_title: str = Path(..., description="The title of the book to update"), category: str = Query(...)):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book["category"] = category
            return book
    return {"message": "Book not found"}

#route 4: Update the title of a book.
@app.patch("/books/{book_title}/update_title")
def update_book_title(book_title: str = Path(..., description="Current title of the book to update"), new_title: str = Query(..., description="New title for the book"),):
    for book in BOOKS:
        if book_title.casefold() == book["title"].casefold():
            book["title"] = new_title
            return book
    return {"message": "Book not found"}

#route 5: Delete all books by a specific author.
@app.delete("/books/delete_by_author")
def delete_book_by_author(author: str = Query(..., description="Delete all books by a specific author.")):
    global BOOKS
    BOOKS = [book for book in BOOKS if author.casefold() != book["author"].casefold()]
    return {"message": f"All books by {author} have been deleted."}


#route 6: Create multiple books at once.
@app.post("/books/bulk_create")
def bulk_create(books: list[CreateBookDTO] = Body(..., description="List of books to create")):
    global BOOKS
    for book in books:
        BOOKS.append(book.model_dump())
    return {"message": "Books have been created successfully.", "books": books}



              
    
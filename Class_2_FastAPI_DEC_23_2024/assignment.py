from fastapi import FastAPI, Body, Query
from typing import List
from .data import BOOKS
from .validators import CreateBookDTO, UpdateBookCategoryDto, UpdateBookTitleDto

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get('/')
async def first_api():
    return {'message': 'Hello, there! 🌟'}

#Search for books by a keyword in the title or author
@app.get('/books/search')
async def search_by_keyword(keyword: str = Query(...)):
    results = []
    for book in BOOKS:
        if keyword.casefold() in book["title"].casefold() or keyword.casefold() in book["author"].casefold():
            results.append(book)
            return results
    return {"message": f"Book with title {keyword} not found"}


#Get the total count of books in a specific category
@app.get('/book/count')
async def total_count(category: str = Query(...)):
    counts = 0
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            counts += 1
    return counts

#Update the category of a book by its title
@app.put('/books/{book_title}/update_category')
async def update_category(book_title: str, updated_book:UpdateBookCategoryDto):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS[i]["category"] = updated_book.category 
            return BOOKS[i]
    return {"message": f"Book with title {book_title} not found"}

# Update the title of a book
@app.patch('/books/{book_title}/update_title')
async def update_title(book_title:str, updated_book:UpdateBookTitleDto):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS[i]["new_title"] = updated_book.title
            return BOOKS[i]
    return {"message": f"Book with title {book_title} not found"}

#Delete all books by a specific author
@app.delete('/books/delete_by_author')
async def delete_book(author:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == author.casefold():
            BOOKS.pop(i)
            return {"message": f"Book with Title {author} has been deleted"}
    return {"message": f"Book with title {author} not found"}

#create multiple books at once
@app.post("/create-book")
async def create_books(book_requests: List[CreateBookDTO]):
    new_books = []
    for book in book_requests:
        new_book = book.model_dump()
        new_books.append(new_book)
    return {"created_books": new_books}
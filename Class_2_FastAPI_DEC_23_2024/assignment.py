from fastapi import FastAPI, Body, Query
from .data import BOOKS
from .validators import UpdateBookCategoryDto, UpdateBookTitleDto, CreateBookDTO

app = FastAPI()

@app.get('/')
async def server():
    return { 'message': 'Server is running' }

@app.get('/books/search/')
async def search_books_by_keyword(keyword : str = Query(...)):
    books_to_return = []
    for book in BOOKS:
        if keyword.casefold() in book.get('title').casefold() or keyword.casefold() in book.get('author').casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/count/')
async def count_books(category : str = Query(...)):
    count = 0
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            count += 1
    return { 'count': count }


@app.put('/books/{book_title}/update_category')
async def update_category(book_title: str, updated_book:UpdateBookCategoryDto):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS[i]["category"] = updated_book.category 
            return BOOKS[i]
    return {"message": f"Book with title {book_title} not found"}

@app.patch('/books/{book_title}/update_title')
async def update_title(book_title:str, updated_book:UpdateBookTitleDto):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS[i]["title"] = updated_book.title
            return BOOKS[i]
    return {"message": f"Book with title {book_title} not found"}

@app.delete('/books/delete_by_author')
async def delete_book_by_author(author:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == author.casefold():
            BOOKS.pop(i)
            return {"message": f"Book with author {author} deleted"}
    return {"message": f"Book with author {author} not found"}

@app.post('/books/create_book')
async def create_books(create_books: list[CreateBookDTO] = Body(...)):
    books = []
    for book in create_books:
        new_book = book.dict()
        BOOKS.append(new_book)
        books.append(new_book)
    return books
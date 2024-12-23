# Assignment: Advanced CRUD Operations with FastAPI

In this assignment, you will create 6 additional routes for the FastAPI application. These routes will involve more technical requirements and logic, building upon the CRUD operations we have already implemented. You will use the `BOOKS` data from `data.py`.

## Requirements

1. **GET /books/search**
   - **Description**: Search for books by a keyword in the title or author.
   - **Query Parameters**: `keyword` (str)
   - **Response**: A list of books that contain the keyword in the title or author.

2. **GET /books/count**
   - **Description**: Get the total count of books in a specific category.
   - **Query Parameters**: `category` (str)
   - **Response**: The count of books in the specified category.

3. **PUT /books/{book_title}/update_category**
   - **Description**: Update the category of a book by its title.
   - **Path Parameters**: `book_title` (str)
   - **Request Body**: `category` (str)
   - **Response**: The updated book with the new category.

4. **PATCH /books/{book_title}/update_title**
   - **Description**: Update the title of a book.
   - **Path Parameters**: `book_title` (str)
   - **Request Body**: `new_title` (str)
   - **Response**: The updated book with the new title.

5. **DELETE /books/delete_by_author**
   - **Description**: Delete all books by a specific author.
   - **Query Parameters**: `author` (str)
   - **Response**: A message indicating the number of books deleted.

6. **POST /books/bulk_create**
   - **Description**: Create multiple books at once.
   - **Request Body**: A list of books (each book should have `title`, `author`, and `category` fields)
   - **Response**: A list of the newly created books.

## Instructions

1. Create a new file named `assignment.py` in the `Class_2_FastAPI_DEC_23_2024` directory.
2. Implement the 6 routes described above in `assignment.py`.
3. Use the `BOOKS` data from `data.py` for all operations.
4. Ensure that your code is well-documented and follows best practices.
5. Run your application with the following command:
   ```sh
   poetry run uvicorn Class_2_FastAPI_DEC_23_2024.assignment:app --reload
   ```

## Submission

- Push your completed `assignment.py` file to your branch only. Do not create a pull request.
- Ensure that all routes are tested and working correctly.
- The deadline for the assignment is Saturday, December 28,2024 at 11:59 PM.

Good luck!

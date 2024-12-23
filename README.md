# FastAPI Application

This is a simple FastAPI application to demonstrate the basics of FastAPI, including creating endpoints, handling requests, and managing dependencies using Poetry.

## Prerequisites

- Python 3.8 or higher
- Poetry

## Installation

1. **Install Poetry**: If you haven't already installed Poetry, you can do so by pasting the below command in your terminal:
   ```sh
   pip install poetry
   ```

2. **Clone the repository**:
   ```sh
   git clone https://github.com/Damieee/future-purpose-learn-to-code-2.0.git
   cd future-purpose-learn-to-code-2.0
   ```

3. **Initialize the Poetry project**: If the project has not been initialized with Poetry yet, run the following command to create a `pyproject.toml` file:
   ```sh
   poetry init
   ```
   Follow the prompts to complete the initialization process.

4. **Install the dependencies**:
   ```sh
   poetry install
   ```

5. **Activate the virtual environment**:
   ```sh
   poetry shell
   ```

## Running the Application

To run the FastAPI application, use the following command:
```sh
poetry run uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

## Project Structure

```
.
├── .gitignore
├── pyproject.toml
├── README.md
├── Class_2_FastAPI_DEC_23_2024
    ├── main.py
    └── validators.py
```

- **main.py**: Contains the FastAPI application with various endpoints.
- **validators.py**: Contains the Pydantic models for request validation.
- **pyproject.toml**: Contains the project dependencies and configuration for Poetry.

## Endpoints

### GET /api-endpoint
Returns a simple greeting message.

### GET /
Returns a list of all books.

### GET /books/{dynamic_param}
Returns the dynamic parameter passed in the URL.

### GET /books/{book_title}
Returns a book by its title.

### GET /books/
Returns books by category using query parameters.

### GET /books/{book_author}/
Returns books by author and category using query parameters.

### POST /books/create_book
Creates a new book using the request body.

### POST /create-book
Creates a new book using a Pydantic model.

### PUT /books/update_book
Updates an existing book using the request body.

### DELETE /books/delete_book/{book_title}
Deletes a book by its title.

## Adding Dependencies

To add new dependencies to the project, use the following command:
```sh
poetry add <package-name>
```

To add development dependencies, use:
```sh
poetry add --dev <package-name>
```

## Running Tests

To run tests, use the following command:
```sh
poetry run pytest
```

## License

This project is licensed under the MIT License.

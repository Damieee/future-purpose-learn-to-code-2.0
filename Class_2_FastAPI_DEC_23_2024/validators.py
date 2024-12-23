from pydantic import BaseModel, Field

class CreateBookDTO(BaseModel):  
    title: str = Field(min_length=3, title="Title of the book")
    author: str = Field(min_length=3, title="Author of the book")
    category: str = Field(min_length=3, title="Category of the book")
    
class UpdateBookAuthorDto(BaseModel):  
    author: str = Field(min_length=3, title="Author of the book")

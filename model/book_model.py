from pydantic import BaseModel, field_validator

class Book(BaseModel):
  isbn:str
  title:str 
  author:str
  published_year:str
  total_copies:int 
  available_copies:int
  category:str|None = None
  
  @field_validator("isbn")
  def validate_isbn(cls, value):
    if len(value) != 13:
      raise ValueError("ISBN must be 13 characters long")
    return value
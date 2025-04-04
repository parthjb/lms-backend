import logging
from fastapi import APIRouter, HTTPException
from logger_config import logging
from dao.book_dao import BookDao
from service.book_service import BookService


router = APIRouter()

book_dao = BookDao()
book_service_obj = BookService(book_dao)


@router.get("/")
def get_all_books():
  try:
    books = book_dao.get_all_books()
    if not books:
      logging.info("No books available")
      return {"message":"No books available","books":[]}
    logging.info(f"Endpoint hit: GET /books/")
    logging.info(f"{len(books)} books fetched from DB.")
    return {"books":books}
  except HTTPException as err:
    raise err
  except Exception as e:
    logging.error(f"Error in get_all_books: {str(e)}")
    raise HTTPException(status_code=500, detail="Internal server error in route!")
  
  
@router.get("/{isbn}")
async def get_book_by_isbn(isbn:int):
  try:
    book = book_dao.get_book_by_isbn(isbn)
    logging.info(f"Endpoint hit: GET /books/{isbn}")
    return {"book":book}
  except Exception as e:
    logging.error(f"Route error in get_book_by_isbn (ISBN: {isbn}): {str(e)}")
    raise HTTPException(status_code=500, detail="Internal server error in route!")
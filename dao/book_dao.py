from database.connection import get_db_connection
from fastapi import HTTPException
import logging
from logger_config import logging

class BookDao:

  def __init__(self):
    self.conn = get_db_connection()

  def get_book_by_isbn(self,isbn):
      #Fetch a book by its isbn
      try:
        query = "SELECT * FROM books WHERE isbn = %(isbn)s"
        params = {"isbn":isbn}
        cursor = self.conn.cursor()
        cursor.execute(query,params)
        data = cursor.fetchone()
        if data:
          logging.info(f"Book found with ISBN: {isbn}")
        else:
          logging.info(f"No book found with ISBN: {isbn}")
        return data
      except Exception as e:
        logging.error(f"Database error in get_book_by_isbn: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error while fetching book.")
  
    

  def get_all_books(self):
    #Fetch all books from the database
    try:
      query = "SELECT * FROM books"
      cursor = self.conn.cursor()
      cursor.execute(query)
      result = cursor.fetchall();  
      logging.info("Fetched all books from DB.")
      return result
    except Exception as e:
      logging.error(f"Database error in get_all_books: {str(e)}")
      raise HTTPException(status_code=500, detail=f"Internal server error in dao!")
 
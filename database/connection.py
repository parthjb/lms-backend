from mysql.connector import connect, Error
from fastapi import HTTPException
from config.db_config import DB_CONFIG

def get_db_connection():
  try:
    connection = connect(**DB_CONFIG)
    return connection
  except Error as e:
    raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

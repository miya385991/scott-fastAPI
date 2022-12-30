from fastapi import HTTPException
from database import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def http_exception():
    return HTTPException(status_code=404, detail="depts not found")


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }

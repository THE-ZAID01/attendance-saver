from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud

router = APIRouter()

@router.post("/students", response_model=schemas.StudentResponse)
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

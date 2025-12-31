from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        roll_no=student.roll_no,
        department=student.department
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

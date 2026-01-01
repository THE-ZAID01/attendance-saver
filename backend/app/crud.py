from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    # check duplicate email
    existing = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student with this email already exists"
        )

    new_student = models.Student(
        name=student.name,
        roll_no=student.roll_no,
        department=student.department,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

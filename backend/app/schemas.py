from pydantic import BaseModel, EmailStr

# ---------- REQUEST SCHEMA ----------
class StudentCreate(BaseModel):
    name: str
    roll_no: str
    department: str
    email: EmailStr


# ---------- RESPONSE SCHEMA ----------
class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: str
    department: str
    email: EmailStr

    class Config:
        from_attributes = True

"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "Pydantic models for request/response schemas"


from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassOut(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True


class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr


class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        orm_mode = True

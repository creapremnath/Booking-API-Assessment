"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "SQLModel ORM models for FitnessClass and Booking"


from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime


class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int = Field(foreign_key="fitnessclass.id")
    client_name: str
    client_email: str

    fitness_class: Optional["FitnessClass"] = Relationship(back_populates="bookings")


class FitnessClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    bookings: List[Booking] = Relationship(back_populates="fitness_class")

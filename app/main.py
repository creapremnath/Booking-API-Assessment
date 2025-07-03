"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "Main FastAPI app file with route definitions"


import logging
from fastapi import FastAPI, Depends, Query
from sqlmodel import Session
import models, schemas, crud, seed, db

# Setup logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("fitness_studio.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("app")

app = FastAPI(title="Fitness Studio Booking API")

models.SQLModel.metadata.create_all(db.engine)
seed.seed()


@app.get("/classes", response_model=list[schemas.ClassOut])
def list_classes(session: Session = Depends(db.get_session)):
    """
    This API is Used to List All classes
    """

    logger.info("List all classess API called")
    return crud.get_classes(session)


@app.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingCreate, session: Session = Depends(db.get_session)):
    logger.info(f"New booking API called for class_id={booking.class_id}")
    return crud.create_booking(session, booking)


@app.get("/bookings", response_model=list[schemas.BookingOut])
def get_bookings(client_email: str = Query(...), session: Session = Depends(db.get_session)):
    """
    This API is used to call specific users Booking details
    """
    logger.info(f"bookings details called for email={client_email}")
    return crud.get_bookings_by_email(session, client_email)

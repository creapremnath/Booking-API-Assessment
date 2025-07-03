"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "CRUD operations for fitness classes and bookings"


from sqlmodel import Session, select
from fastapi import HTTPException
from datetime import datetime
import models, schemas
import logging

logger = logging.getLogger("crud")


def get_classes(db: Session):
    """
    Fetch all upcoming fitness classes (datetime >= now)
    """
    logger.info("Fetching all upcoming fitness classes")
    now = datetime.now()
    statement = select(models.FitnessClass).where(models.FitnessClass.datetime >= now)
    classes = db.exec(statement).all()
    logger.debug(f"Found {len(classes)} classes")
    return classes  # 200 OK by default


def create_booking(db: Session, booking: schemas.BookingCreate):
    """
    Create a booking for a client if slots available.
    Returns booking on success, raises HTTPException on errors.
    """
    logger.info(f"Creating booking for class_id={booking.class_id} by {booking.client_email}")

    # Fetch the fitness class by id
    fitness_class = db.get(models.FitnessClass, booking.class_id)
    if not fitness_class:
        logger.error(f"Fitness class {booking.class_id} not found")
        raise HTTPException(status_code=404, detail="Class not found")

    # Check slot availability
    if fitness_class.available_slots <= 0:
        logger.warning(f"No slots available for class {booking.class_id}")
        raise HTTPException(status_code=400, detail="No slots available")

    # Optional: Check if same client already booked this class (to prevent duplicates)
    existing_booking = db.exec(
        select(models.Booking)
        .where(models.Booking.class_id == booking.class_id)
        .where(models.Booking.client_email == booking.client_email)
    ).first()
    if existing_booking:
        logger.warning(f"Duplicate booking attempt for class {booking.class_id} by {booking.client_email}")
        raise HTTPException(status_code=409, detail="You have already booked this class")

    # Create new booking
    db_booking = models.Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email,
    )
    fitness_class.available_slots -= 1

    db.add(db_booking)
    db.add(fitness_class)
    db.commit()
    db.refresh(db_booking)

    logger.info(f"Booking created successfully with id {db_booking.id}")
    return db_booking  # 200 OK


def get_bookings_by_email(db: Session, email: str):
    """
    Fetch all bookings for a given client email.
    Raises 404 if none found.
    """
    logger.info(f"Fetching bookings for email: {email}")
    statement = select(models.Booking).where(models.Booking.client_email == email)
    bookings = db.exec(statement).all()

    if not bookings:
        logger.warning(f"No bookings found for email: {email}")
        raise HTTPException(status_code=404, detail="No bookings found for this email")

    logger.debug(f"Found {len(bookings)} bookings for {email}")
    return bookings  # 200 OK

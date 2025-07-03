"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "Script to seed initial fitness classes data into the database"


from datetime import datetime, timedelta
import pytz
from sqlmodel import Session, select
import models
from db import engine
import logging

logger = logging.getLogger("seed")

def seed():
    """
    This Fuction will create a few data on DB for API testing
    """
    logger.info("Seeding initial fitness classes...")
    models.SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        statement = select(models.FitnessClass)
        existing = session.exec(statement).first()
        if existing:
            logger.info("Data already seeded, skipping...")
            return

        ist = pytz.timezone("Asia/Kolkata")
        now = datetime.now(ist)

        classes = [
            models.FitnessClass(name="Yoga", datetime=now + timedelta(days=1), instructor="Alice", available_slots=10),
            models.FitnessClass(name="Zumba", datetime=now + timedelta(days=2), instructor="Bob", available_slots=8),
            models.FitnessClass(name="HIIT", datetime=now + timedelta(days=3), instructor="Charlie", available_slots=5),
        ]

        session.add_all(classes)
        session.commit()
        logger.info("Seeding done.")

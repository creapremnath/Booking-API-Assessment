"""
Omnify Assessment using Python FastAPI
"""

__author__ = "Premnath Palanichamy"
__collaborators__ = "Premnath Palanichamy <premnathpalanichamy28@gmail.com>"
__version__ = "1.0"
__maintainer__ = "Premnath Palanichamy"
__status__ = "Development"
__desc__ = "Database connection and session setup"


from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///./fitness_studio.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

from sqlmodel import Session
from app.database.session import engine


def get_session():
    with Session(engine) as session:
        yield session

from sqlmodel import create_engine, SQLModel
from app.core import settings
from loguru import logger

connect_args = {"check_same_thread": False}

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False, connect_args=connect_args)


def create_db_and_tables():
    logger.info(f"Connecting to Database: {settings.SQLALCHEMY_DATABASE_URI}")
    SQLModel.metadata.create_all(engine)

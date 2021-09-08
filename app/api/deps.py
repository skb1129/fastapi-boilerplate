from typing import Generator

from app.database.session import create_session, create_async_session


def get_db() -> Generator:
    try:
        db = create_session()
        yield db
    finally:
        db.close()


async def get_db_async() -> Generator:
    async with create_async_session() as session:
        yield session

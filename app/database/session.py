from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession

from typing import Callable, Optional

from app.core import settings

__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None


def global_init():
    global __factory, __async_engine
    if __factory:
        return
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
    __async_engine = create_async_engine(
        settings.SQLALCHEMY_DATABASE_URI_ASYNC, pool_pre_ping=True
    )
    __factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_session() -> Session:
    global __factory
    if not __factory:
        raise Exception("global_init() must be called first.")
    session: Session = __factory()
    session.expire_on_commit = False
    return session


def create_async_session() -> AsyncSession:
    global __async_engine
    if not __async_engine:
        raise Exception("global_init() must be called first.")
    session: AsyncSession = AsyncSession(bind=__async_engine)
    session.sync_session.expire_on_commit = False
    return session

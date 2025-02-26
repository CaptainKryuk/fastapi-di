"""Database module."""
import contextlib
from collections.abc import AsyncIterator
from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()


db_url = 'postgresql+asyncpg://root:pass@pgdb:5432/db'

async_engine = create_async_engine(
    db_url, echo=True
)
async_session_factory = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)

@contextlib.asynccontextmanager
async def create_session() -> AsyncIterator[AsyncSession]:
    async with async_session_factory.begin() as session:
        yield session
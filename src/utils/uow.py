from abc import ABC
from contextlib import asynccontextmanager
from typing import Any, Generator, Self

from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.repositories.users import IUserRepository, UserRepository
from src.infrastructure.database.session import session_maker

_sentinel: Any = object()


class IUnitOfWork(ABC):
    users: IUserRepository

    def __init__(self) -> None:
        self.session = _sentinel

    async def __aenter__(self) -> Self:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def get_session(self) -> Generator[Any]:
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    def __init__(self) -> None:
        super().__init__()

    async def __aenter__(self) -> Self:
        self.session = session_maker()
        self.users = UserRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_val:
            await self.session.rollback()
        else:
            await self.session.commit()
        await self.session.close()

    @asynccontextmanager
    async def get_session(self) -> Generator[AsyncSession]:  # type: ignore
        session = session_maker()
        try:
            yield session  # type: ignore
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

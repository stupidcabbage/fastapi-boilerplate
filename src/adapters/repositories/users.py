from abc import ABC
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dto.users import User
from src.infrastructure.database.models import User as UserDB


class IUserRepository(ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, model: User) -> None:
        raise NotImplementedError

    async def get(self, id: uuid.UUID) -> User:
        raise NotImplementedError


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, model: User) -> None:
        self.session.add(
            UserDB(
                id=model.id,
                username=model.username,
                password=model.password,
            )
        )

    async def get(self, id: uuid.UUID) -> User | None:
        stmt = (
            select(UserDB).where(UserDB.id == id)
        )
        result = await self.session.scalar(stmt)
        if result:
            return result.to_schema()
        return None

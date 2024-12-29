import uuid
from abc import ABC

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dto.users import User
from src.infrastructure.database.models import User as UserDB


class IUserRepository(ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, model: User) -> None:
        raise NotImplementedError

    async def get_by_id(self, id: uuid.UUID) -> User | None:
        raise NotImplementedError

    async def is_user_exists_by_username(self, username: str) -> bool:
        raise NotImplementedError


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, model: User) -> None:
        self.session.add(
            UserDB(
                id=model.id,
                username=model.username,
                password=model.password.hash(),
            )
        )

    async def get_by_id(self, id: uuid.UUID) -> User | None:
        stmt = select(UserDB).where(UserDB.id == id)
        user = await self.session.scalar(stmt)
        if user:
            return await user.to_schema()
        return None

    async def is_user_exists_by_username(self, username: str) -> bool:
        stmt = select(func.count(UserDB.username)).where(
            UserDB.username == username
        )
        user = await self.session.scalar(stmt)
        return bool(user)

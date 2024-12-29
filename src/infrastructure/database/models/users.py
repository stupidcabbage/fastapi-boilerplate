from datetime import datetime

from sqlalchemy import UUID, func
from sqlalchemy.orm import Mapped, mapped_column

from src.core.dto.users import Password
from src.core.dto.users import User as UserDto

from src.infrastructure.database.models import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    password: Mapped[str] = mapped_column(default=None)
    username: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    async def to_schema(self) -> UserDto:
        return UserDto(
            id=self.id,  # type: ignore
            username=self.username,
            password=Password(self.password),
        )

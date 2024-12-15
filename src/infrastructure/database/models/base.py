from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    "Общая модель объектов в базе данных."

    async def to_schema(self) -> None:
        raise NotImplementedError

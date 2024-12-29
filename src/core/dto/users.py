import uuid

import bcrypt
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import core_schema


class Password:
    def __init__(self, password: str) -> None:
        self.password = password

    def hash(self) -> str:
        return bcrypt.hashpw(
            str(self.password).encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, pswd: str) -> bool:
        return bcrypt.checkpw(
            pswd.encode("utf-8"), str(self.password).encode("utf-8")
        )

    def __len__(self) -> int:
        return len(self.password)

    def __repr__(self) -> str:
        return self.password

    def __str__(self) -> str:
        return str(self.password)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(cls._validate)

    @classmethod
    def _validate(cls, password: str) -> "Password":
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return cls(password)


class UserWithoutPassword(BaseModel):
    id: uuid.UUID
    username: str


class User(BaseModel):
    id: uuid.UUID
    username: str
    password: Password

    def to_user_without_password(self) -> UserWithoutPassword:
        return UserWithoutPassword(id=self.id, username=self.username)


class CreateUserDto(BaseModel):
    username: str
    password: Password

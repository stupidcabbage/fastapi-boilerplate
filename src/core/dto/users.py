import uuid

from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class Password:
    def __init__(self, password: str) -> None:
        self.password = password

    def __repr__(self) -> str:
        return self.password

    @classmethod
    def __get_pydantic_core_schema__(
                cls, source_type: str, handler: GetCoreSchemaHandler
            ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))


class User(BaseModel):
    id: uuid.UUID
    username: str
    password: str


class UserWithoutPassword(BaseModel):
    id: uuid.UUID
    username: str


class CreateUserDto(BaseModel):
    username: str
    password: str

import uuid

from pydantic import BaseModel


class Token(BaseModel):
    token: str


class SignInDto(BaseModel):
    id: uuid.UUID
    password: str

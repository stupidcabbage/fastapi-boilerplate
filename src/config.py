import os
from dataclasses import dataclass
from typing import NewType


@dataclass
class DBConfig:
    DRIVER_URL: str


Minutes = NewType("Minutes", int)


@dataclass
class JWTConfig:
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES: Minutes


class Config:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_db_config() -> DBConfig:
        return DBConfig(DRIVER_URL=os.getenv("DRIVER_URL", ""))

    @staticmethod
    def get_jwt_config() -> JWTConfig:
        return JWTConfig(
            SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
            ALGORITHM=os.getenv("ALGORITHM", "HS256"),
            ACCESS_TOKEN_EXPIRES=Minutes(
                int(os.getenv("ACCESS_TOKEN_EXPIRES", 120))
            ),
        )

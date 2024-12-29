import os
from dataclasses import dataclass
from typing import NewType


@dataclass
class DBConfig:
    driver_url: str


Minutes = NewType("Minutes", int)


@dataclass
class JWTConfig:
    secret_key: str
    algorithm: str
    access_token_expires: Minutes


@dataclass
class InitConfig:
    port: int
    host: str


class Config:
    def __init__(self) -> None: ...

    @staticmethod
    def get_db_config() -> DBConfig:
        return DBConfig(driver_url=os.getenv("DRIVER_URL", ""))

    @staticmethod
    def get_jwt_config() -> JWTConfig:
        return JWTConfig(
            secret_key=os.getenv("SECRET_KEY", "dev"),
            algorithm=os.getenv("ALGORITHM", "HS256"),
            access_token_expires=Minutes(
                int(os.getenv("ACCESS_TOKEN_EXPIRES", "120"))
            ),
        )

    @staticmethod
    def get_init_config() -> InitConfig:
        return InitConfig(
            port=int(os.getenv("PORT", "8000")),
            host=os.getenv("HOST", "0.0.0.0"),
        )

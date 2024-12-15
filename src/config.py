import os
from dataclasses import dataclass


@dataclass
class DBConfig:
    DRIVER_URL: str


class Config():
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_db_config():
        return DBConfig(
            DRIVER_URL=os.getenv("DRIVER_URL", "")
        )

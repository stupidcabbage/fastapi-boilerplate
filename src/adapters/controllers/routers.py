from typing import Callable, Type

from fastapi import APIRouter

from src.adapters.controllers import exceptions, users
from src.core.exceptions.error import BaseError


def get_routers() -> list[APIRouter]:
    return [
        users.router,
    ]


def get_exceptions_handlers() -> list[tuple[Type[BaseError], Callable]]:
    return [
        (BaseError, exceptions.base_exception_handler),
    ]

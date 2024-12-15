from fastapi import APIRouter

from src.adapters.controllers import users


def get_routers() -> list[APIRouter]:
    return [
        users.router,
    ]

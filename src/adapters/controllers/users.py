import uuid

from fastapi import APIRouter

from src.core.dto.users import CreateUserDto, UserWithoutPassword
from src.core.services.users import UserService

from .depends import UOWDep

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", status_code=201)
async def create_user(
            user: CreateUserDto, uow: UOWDep
        ) -> UserWithoutPassword:
    return await UserService(uow).create(user)


@router.get("/{id}", status_code=200)
async def get_user(
            id: uuid.UUID, uow: UOWDep
        ) -> UserWithoutPassword:
    return await UserService(uow).get(id=id)

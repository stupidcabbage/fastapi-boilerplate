import uuid
from http import HTTPStatus

from fastapi import APIRouter

from src.core.dto.users import CreateUserDto, UserWithoutPassword
from src.core.exceptions.base import NotFound
from src.core.services.users import UserService

from .depends import JWTDep, UOWDep

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=HTTPStatus.CREATED)
async def create_user(user: CreateUserDto, uow: UOWDep) -> UserWithoutPassword:
    return await UserService(uow).create(user)


@router.get("/me", status_code=HTTPStatus.OK)
async def get_self_profile(user: JWTDep) -> UserWithoutPassword:
    return user.to_user_without_password()


@router.get("/{id}", status_code=HTTPStatus.OK)
async def get_user(
    id: uuid.UUID, user: JWTDep, uow: UOWDep
) -> UserWithoutPassword | None:
    u_model = await UserService(uow).get_by_id(id=id)
    if not u_model:
        raise NotFound
    return u_model

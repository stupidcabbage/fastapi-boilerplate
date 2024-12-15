import uuid
from abc import ABC
from uuid import uuid4

from src.adapters.repositories.users import IUserRepository
from src.core.dto.users import CreateUserDto, User, UserWithoutPassword
from src.core.exceptions.users import UserAlreadyExists
from src.utils.uow import UnitOfWork


class IUserService(ABC):
    def __init__(self, repository: IUserRepository) -> None:
        pass

    def create(self, model: CreateUserDto) -> UserWithoutPassword:
        raise NotImplementedError

    def get(self, id: uuid.UUID) -> UserWithoutPassword:
        raise NotImplementedError


class UserService(IUserService):
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def create(self, model: CreateUserDto) -> UserWithoutPassword:
        u_model = User(
            id=uuid4(),
            username=model.username,
            password=model.password
        )
        async with self.uow as uow:
            if await uow.users.is_user_exists_by_username(u_model.username):
                raise UserAlreadyExists
            await uow.users.create(u_model)
        return UserWithoutPassword(**u_model.model_dump())

    async def get(self, id: uuid.UUID) -> UserWithoutPassword:
        async with self.uow as uow:
            u_model = await uow.users.get(id=id)
        return UserWithoutPassword(**u_model.model_dump())

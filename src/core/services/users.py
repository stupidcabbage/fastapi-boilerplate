from abc import ABC
from uuid import UUID, uuid4

from src.core.dto.users import CreateUserDto, User, UserWithoutPassword
from src.core.exceptions.users import UserAlreadyExists
from src.utils.uow import IUnitOfWork, UnitOfWork


class IUserService(ABC):
    def __init__(self, uow: IUnitOfWork) -> None: ...

    async def create(self, model: CreateUserDto) -> UserWithoutPassword:
        raise NotImplementedError

    async def get_by_id(self, id: UUID) -> UserWithoutPassword:
        raise NotImplementedError

    async def get_by_id_with_password(self, id: UUID) -> User | None:
        raise NotImplementedError


class UserService(IUserService):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)
        self.uow = uow

    async def create(self, model: CreateUserDto) -> UserWithoutPassword:
        u_model = User(
            id=uuid4(), username=model.username, password=model.password
        )
        async with self.uow as uow:
            if await uow.users.is_user_exists_by_username(u_model.username):
                raise UserAlreadyExists
            await uow.users.create(u_model)
        return UserWithoutPassword(**u_model.model_dump())

    async def get_by_id(self, id: UUID) -> UserWithoutPassword | None:
        async with self.uow as uow:
            u_model = await uow.users.get_by_id(id=id)
        return UserWithoutPassword(**u_model.model_dump()) if u_model else None

    async def get_by_id_with_password(self, id: UUID) -> User | None:
        async with self.uow as uow:
            u_model = await uow.users.get_by_id(id=id)
        return u_model

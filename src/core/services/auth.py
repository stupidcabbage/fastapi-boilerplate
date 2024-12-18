import time
import uuid
from abc import ABC

import jwt

from src.config import Config
from src.core.dto.tokens import SignInDto, Token
from src.core.exceptions.auth import IncorrectAuthorizeData
from src.core.exceptions.error import BaseError
from src.core.exceptions.users import UserNotExists
from src.utils.uow import IUnitOfWork, UnitOfWork


class IAuthService(ABC):
    def __init__(self, uow: IUnitOfWork) -> None: ...

    async def authorize(self, sign_data: SignInDto) -> Token:
        raise NotImplementedError


class AuthService(IAuthService):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)
        self.jwt_settings = Config.get_jwt_config()
        self.uow = uow

    async def authorize(self, sign_data: SignInDto) -> Token:
        async with self.uow as uow:
            user = await uow.users.get_by_id(id=sign_data.id)
            if not user:
                raise UserNotExists
            if not user.password.check_password(sign_data.password):
                raise IncorrectAuthorizeData
            return self.sign_jwt(user.id)

    def sign_jwt(self, id: uuid.UUID) -> Token:
        payload = {
            "id": str(id),
            "created_at": time.time(),
            "expires": time.time()
            + self.jwt_settings.ACCESS_TOKEN_EXPIRES * 60,
        }
        token = jwt.encode(
            payload,
            self.jwt_settings.SECRET_KEY,
            algorithm=self.jwt_settings.ALGORITHM,
        )
        return Token(token=token)

    def decode_jwt(self, token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                token,
                self.jwt_settings.SECRET_KEY,
                algorithms=[self.jwt_settings.ALGORITHM],
            )
            return decoded_token
        except Exception as e:
            raise BaseError(401, "Incorrect authorization data.", e)

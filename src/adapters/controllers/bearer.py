import time
import uuid
from typing import Literal

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.core.dto.users import User
from src.core.exceptions.auth import (
    ExpiredToken,
    IncorrectAuthorizationSchema,
    InvalidToken,
)
from src.core.exceptions.error import BaseError
from src.core.exceptions.users import UserNotExists
from src.core.services.auth import AuthService
from src.core.services.users import UserService
from src.utils.uow import UnitOfWork


class JWTBearer(HTTPBearer):
    def __init__(self, uow: UnitOfWork, auto_error: bool = True) -> None:
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.uow = uow

    async def __call__(self, request: Request) -> User | Literal[False]:
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(
            request
        )  # type: ignore
        if credentials:
            if not credentials.scheme == "Bearer":
                raise IncorrectAuthorizationSchema
            verify_jwt_status = await self.verify_jwt(
                self.uow, credentials.credentials
            )
            if not verify_jwt_status:
                raise ExpiredToken
            return verify_jwt_status
        else:
            raise InvalidToken

    async def verify_jwt(
        self, uow: UnitOfWork, jwtoken: str
    ) -> Literal[False] | User:
        try:
            payload = AuthService(uow).decode_jwt(jwtoken)
        except Exception as e:
            raise BaseError(401, "Invalid token.", e)
        if payload:
            user = await UserService(uow).get_by_id_with_password(
                id=uuid.UUID(payload.get("id"))
            )
            if self._is_token_verified(payload, user):
                return user
        return False

    # TODO: добавить blacklist токенов.
    def _is_token_verified(self, payload: dict, user: User | None) -> bool:
        expires = payload.get("expires")
        if not payload.get("expires"):
            raise InvalidToken
        if expires < time.time():
            return False
        if not user:
            raise UserNotExists

        return True

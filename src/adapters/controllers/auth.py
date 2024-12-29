from typing import Annotated

from fastapi import APIRouter, Body

from src.adapters.controllers.depends import UOWDep
from src.core.dto.tokens import SignInDto, Token
from src.core.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/")
async def sign_in(
    uow: UOWDep, sign_data: Annotated[SignInDto, Body()]
) -> Token:
    return await AuthService(uow).authorize(sign_data)

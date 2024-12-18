from typing import Annotated

from fastapi import Depends

from src.adapters.controllers.bearer import JWTBearer
from src.core.dto.users import User
from src.utils.uow import UnitOfWork

UOWDep = Annotated[UnitOfWork, Depends(UnitOfWork)]
JWTDep = Annotated[User, Depends(JWTBearer(UnitOfWork()))]

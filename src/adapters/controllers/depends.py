from typing import Annotated

from fastapi import Depends

from src.utils.uow import UnitOfWork

UOWDep = Annotated[UnitOfWork, Depends(UnitOfWork)]

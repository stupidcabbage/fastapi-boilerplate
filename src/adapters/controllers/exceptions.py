from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.exceptions.error import BaseError


async def base_exception_handler(
            request: Request, exc: BaseError
        ) -> JSONResponse:
    return JSONResponse(
        content={"message": exc.message},
        status_code=exc.http_code
    )

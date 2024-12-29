import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.adapters.controllers.routers import (
    get_exceptions_handlers,
    get_routers,
)
from src.config import Config


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("🚀 Starting application")
    for router in get_routers():
        app.include_router(router, prefix="/api/v1")

    yield
    logging.info("⛔ Stopping application")


# TODO: рассмотреть что за баг и почему хенделеры надо добавлять только здесь
app = FastAPI(lifespan=lifespan, debug=True)
for type, exception_handler in get_exceptions_handlers():
    app.add_exception_handler(type, exception_handler)


if __name__ == "__main__":
    _init_config = Config.get_init_config()
    uvicorn.run(
        "src.__main__:app",
        host=_init_config.host,
        port=_init_config.port,
        forwarded_allow_ips=[
            "*",
        ],
    )

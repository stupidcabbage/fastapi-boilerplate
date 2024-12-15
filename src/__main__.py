import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.adapters.controllers.routers import get_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("🚀 Starting application")
    for router in get_routers():
        app.include_router(router)

    yield
    logging.info("⛔ Stopping application")

app = FastAPI(lifespan=lifespan)


# TODO: переписать host, port в ENV.
if __name__ == "__main__":
    uvicorn.run("src.__main__:app", host="0.0.0.0", port=8000,
                forwarded_allow_ips=["*", ])

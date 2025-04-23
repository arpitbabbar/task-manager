from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.routes import router as task_router
from src.core.database import create_tables
from src.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    logger.info("App is shutting down...")


app = FastAPI(title="Task Management System", lifespan=lifespan)

app.include_router(task_router, prefix="/api/v1")

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.repository import task as task_repository
from src.core.logger import logger


# Create a task
async def create_task(db: AsyncSession, task_in):
    try:
        return await task_repository.create_task(db, task_in)
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise


# Get all tasks
async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10):
    try:
        return await task_repository.get_tasks(db, skip, limit)
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        raise


# Get Task by ID
async def get_task_by_id(db: AsyncSession, task_id: UUID):
    try:
        return await task_repository.get_task_by_id(db, task_id)
    except Exception as e:
        logger.error(f"Error fetching task with id {task_id}: {e}")
        raise


# Update a task
async def update_task(db: AsyncSession, task_id: UUID, task_in):
    try:
        return await task_repository.update_task(db, task_id, task_in)
    except Exception as e:
        logger.error(f"Error updating task with id {task_id}: {e}")
        raise


# Delete a task
async def delete_task(db: AsyncSession, task_id: UUID):
    try:
        return await task_repository.delete_task(db, task_id)
    except Exception as e:
        logger.error(f"Error deleting task with id {task_id}: {e}")
        raise

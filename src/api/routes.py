from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.core.logger import logger
from src.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TasksResponse
from src.services.task_service import create_task, get_tasks, update_task, delete_task, get_task_by_id

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "status_code_message": "Database is reachable", "data": []}
    except Exception as e:
        logger.error(f"Database unreachable: {e}")
        raise HTTPException(status_code=500, detail="Database unreachable")


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task_endpoint(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    try:
        created_task = await create_task(db, task)
        return TaskResponse(
            status="success",
            detail="Task created successfully",
            data=created_task
        )
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Error creating task")


@router.get("/tasks", response_model=TasksResponse)
async def get_tasks_endpoint(skip: int = 0, limit: int = Query(default=10, lt=50), db: AsyncSession = Depends(get_db)):
    try:
        tasks = await get_tasks(db, skip, limit)
        return TasksResponse(
            status="success",
            detail="Tasks fetched successfully",
            data=tasks
        )
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        raise HTTPException(status_code=500, detail="Error fetching tasks")


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_by_id_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
    try:
        task = await get_task_by_id(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return TaskResponse(
            status="success",
            status_code_message="Task fetched successfully",
            data=task
        )
    except Exception as e:
        logger.error(f"Error fetching task with id {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Error fetching task")


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task_endpoint(task_id: UUID, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    try:
        updated_task = await update_task(db, task_id, task)
        if not updated_task:
            raise HTTPException(status_code=404, detail="Task not found")
        return TaskResponse(
            status="success",
            detail="Task updated successfully",
            data=updated_task
        )
    except Exception as e:
        logger.error(f"Error updating task with id {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Error updating task")


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
    try:
        deleted_task = await delete_task(db, task_id)
        if not deleted_task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {
            "status": "success",
            "detail": "Task deleted successfully",
            "data": []
        }
    except Exception as e:
        logger.error(f"Error deleting task with id {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Error deleting task")

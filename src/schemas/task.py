from datetime import datetime
from enum import Enum
from typing import Generic, TypeVar, List, Optional
from uuid import UUID

from pydantic import BaseModel

T = TypeVar('T')


class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


# Define the task models as before
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[StatusEnum] = None


class TaskOut(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: StatusEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Define the generic response format
class ResponseModel(BaseModel, Generic[T]):
    status: str
    detail: str
    data: Optional[T]

    class Config:
        from_attributes = True


class TaskResponse(ResponseModel[TaskOut]):
    pass


class TasksResponse(ResponseModel[List[TaskOut]]):
    pass

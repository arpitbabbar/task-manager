import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from src.core.database import Base


class StatusEnum(str, enum.Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = Column(String, nullable=False)
    description: Mapped[str] = Column(String, nullable=True)
    status: Mapped[StatusEnum] = Column(Enum(StatusEnum), default=StatusEnum.pending)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings

# Create async engine
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)


# Session factory
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Base class for models
Base = declarative_base()


# Create all tables in the database (this will create them if they don't exist)
async def create_tables():
    async with engine.begin() as conn:
        # This will create all tables that are defined in your models
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully.")


# Dependency for routes
async def get_db():
    async with async_session() as session:
        yield session

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from talk_to_pdf.core.config import settings

# Create the async engine (echo=True logs all SQL queries to the terminal)
engine = create_async_engine(settings.database_url, echo=True)

# Create a session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# This is the base class our database models will inherit from
Base = declarative_base()

# A FastAPI dependency to inject database sessions into our routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

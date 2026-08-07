from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    # We call AsyncSessionLocal() to spawn the session, then use it as a context manager
    async with AsyncSessionLocal() as session:
        yield session

"""Database connection management"""

import asyncio
import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

import psycopg
from psycopg_pool import AsyncConnectionPool

from app.config import Settings

logger = logging.getLogger(__name__)

_pool: AsyncConnectionPool | None = None
_lock = asyncio.Lock()


async def init_db(settings: Settings) -> None:
    """Initialize database connection pool."""
    global _pool
    
    async with _lock:
        if _pool is None:
            _pool = AsyncConnectionPool(
                conninfo=settings.database_url,
                min_size=5,
                max_size=20,
                timeout=60,
            )
            await _pool.open()
            logger.info("✅ Database connection pool initialized")


async def close_db_pool() -> None:
    """Close database connection pool."""
    global _pool
    
    if _pool:
        await _pool.close()
        logger.info("✅ Database connection pool closed")
        _pool = None


@asynccontextmanager
async def get_db_connection() -> AsyncIterator[psycopg.AsyncConnection]:
    """Get database connection from pool."""
    if _pool is None:
        raise RuntimeError("Database pool not initialized")
    
    async with _pool.connection() as conn:
        yield conn


def get_pool() -> AsyncConnectionPool | None:
    """Get connection pool."""
    return _pool

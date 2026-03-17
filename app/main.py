"""Telegram Accounting Bot - Main Entry Point"""

import asyncio
import logging
from app.config import Settings
from app.db.connection import init_db, close_db_pool
from app.logger import setup_logging
from app.bot.dispatcher import dp

logger = logging.getLogger(__name__)


async def main():
    """Main bot entry point."""
    # Setup logging
    setup_logging()
    logger.info("🚀 Starting Telegram Accounting Bot...")
    
    # Initialize settings
    settings = Settings()
    
    # Initialize database
    await init_db(settings)
    logger.info("✅ Database initialized")
    
    # Initialize Redis
    from app.main import init_redis
    await init_redis(settings)
    logger.info("✅ Redis initialized")
    
    # Start bot
    logger.info("🤖 Bot starting polling...")
    await dp.start_polling(bot)
    
    # Cleanup
    await close_db_pool()


if __name__ == "__main__":
    asyncio.run(main())

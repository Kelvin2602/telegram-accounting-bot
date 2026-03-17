"""Configuration management using pydantic-settings"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Bot configuration settings."""
    
    # Bot Configuration
    bot_token: str = Field(..., env="BOT_TOKEN")
    
    # Database Configuration
    postgres_host: str = Field(default="localhost", env="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, env="POSTGRES_PORT")
    postgres_db: str = Field(..., env="POSTGRES_DB")
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    
    # Redis Configuration
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    
    # Optional Configuration
    webhook_url: str | None = Field(default=None, env="WEBHOOK_URL")
    webhook_secret: str | None = Field(default=None, env="WEBHOOK_SECRET")
    exchange_rate_update_interval: int = Field(default=300, env="EXCHANGE_RATE_UPDATE_INTERVAL")
    
    @property
    def database_url(self) -> str:
        """Construct database URL."""
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"

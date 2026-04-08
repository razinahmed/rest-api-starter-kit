"""
Application configuration using Pydantic BaseSettings.

Environment variables are loaded from .env file.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.

    All settings can be overridden by environment variables.
    """

    # App settings
    APP_NAME: str = "REST API Starter Kit"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/api_db"

    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = True


settings = Settings()

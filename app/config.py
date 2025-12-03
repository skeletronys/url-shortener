from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str

    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Anthropic AI
    anthropic_api_key: str
    anthropic_model: str = "claude-sonnet-4-20250514"
    max_ai_requests_per_user: int = 100

    # AWS
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_s3_bucket_name: str
    aws_region: str = "eu-central-1"

    # Redis
    redis_url: str

    # App
    app_name: str = "AI URL Shortener"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    project_version: str = "1.0.0"

    # Rate Limiting
    rate_limit_per_minute: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Global settings instance
settings = get_settings()
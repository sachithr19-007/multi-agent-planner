"""
Configuration management for the Multi-Agent Task Planning System.

Centralizes settings from environment variables with validation
and sensible defaults for production use.
"""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = "Multi-Agent Task Planning System"
    debug: bool = False

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Logging
    log_level: str = "INFO"
    log_format: str = (
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    # LangGraph (placeholders for future integration)
    langgraph_checkpoint_dir: Optional[str] = None

    # LLM configuration
    llm_provider: str = "openai"  # "openai" or "anthropic"
    llm_model: str = "gpt-4o-mini"  # e.g. gpt-4o-mini, gpt-4o, claude-3-haiku-20240307

    # LLM / API Keys (placeholders - never commit actual keys)
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance for reuse across the application."""
    return Settings()

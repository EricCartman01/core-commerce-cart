from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    SERVICE_NAME: str = "core-commerce-cart"

    HOST: str
    PORT: int
    WORKERS: int
    RELOAD: bool

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

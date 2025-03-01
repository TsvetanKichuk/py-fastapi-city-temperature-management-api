from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        case_sensitive = True


settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Org Management Service"
    MONGO_URL: str = "mongodb://localhost:27017"
    MASTER_DB_NAME: str = "master_db"
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY_HERE"  # Change this in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
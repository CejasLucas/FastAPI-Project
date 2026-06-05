import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://admin:1234@localhost:5432/autoparts"
    )

    ENV: str = os.getenv("ENV", "dev")
    DEBUG: bool = ENV == "dev"


settings = Settings()
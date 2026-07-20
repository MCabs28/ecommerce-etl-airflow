import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    # Database
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    # Logging
    log_level: str

    # ETL
    batch_size: int


config = Config(
    db_host=os.getenv("DB_HOST", "localhost"),
    db_port=int(os.getenv("DB_PORT", "5433")),
    db_name=os.getenv("DB_NAME", "ecommerce_db"),
    db_user=os.getenv("DB_USER", "postgres"),
    db_password=os.getenv("DB_PASSWORD", ""),
    log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
    batch_size=int(os.getenv("BATCH_SIZE", "1000")),
)


def validate_config() -> None:
    """Validate required configuration before the application starts."""
    required_fields = {
        "DB_HOST": config.db_host,
        "DB_NAME": config.db_name,
        "DB_USER": config.db_user,
        "DB_PASSWORD": config.db_password,
    }

    missing = [key for key, value in required_fields.items() if not value]

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


validate_config()

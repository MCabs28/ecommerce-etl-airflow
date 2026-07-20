import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from config import config

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{config.db_user}:{config.db_password}"
    f"@{config.db_host}:{config.db_port}"
    f"/{config.db_name}"
)


engine: Engine = create_engine(DATABASE_URL)


def get_connection():

    return psycopg2.connect(
        host=config.db_host,
        port=config.db_port,
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_password,
    )


def get_engine() -> Engine:

    return engine

from sqlalchemy import create_engine
import psycopg2

from config import DB_CONFIG


def get_connection():
    """
    Returns a psycopg2 connection.

    Use for:
    - Transactions
    - Cursor operations
    - Stored procedures
    """

    return psycopg2.connect(**DB_CONFIG)


def get_engine():
    """
    Returns a SQLAlchemy Engine.

    Use for:
    - pandas.read_sql()
    - DataFrame.to_sql()
    """

    db_url = (
        f"postgresql+psycopg2://"
        f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}"
        f":{DB_CONFIG['port']}"
        f"/{DB_CONFIG['dbname']}"
    )

    return create_engine(db_url)

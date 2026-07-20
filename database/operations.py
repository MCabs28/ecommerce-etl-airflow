from sqlalchemy import text

from database.connection import get_engine


def truncate_table(table_name: str):
    """
    Remove all rows from a table while preserving
    its schema, indexes, and constraints.
    """

    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;"))

    print(f"Truncated {table_name}")

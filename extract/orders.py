import pandas as pd

from database.connection import get_engine


def extract_orders():
    engine = get_engine()

    query = """
    SELECT *
    FROM orders;
    """

    return pd.read_sql(query, engine)

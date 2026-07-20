import pandas as pd

from database.connection import get_engine


def extract_order_items():
    engine = get_engine()

    query = """
    SELECT *
    FROM order_items;
    """

    return pd.read_sql(query, engine)

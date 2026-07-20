import pandas as pd

from database.connection import get_engine


def extract_products():
    engine = get_engine()

    query = """
    SELECT *
    FROM products;
    """

    return pd.read_sql(query, engine)

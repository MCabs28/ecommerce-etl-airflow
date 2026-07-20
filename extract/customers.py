import pandas as pd

from database.connection import get_engine


def extract_customers():
    engine = get_engine()

    query = """
    SELECT *
    FROM customers;
    """

    return pd.read_sql(query, engine)

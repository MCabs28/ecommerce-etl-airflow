import logging

import pandas as pd

from database.connection import get_engine

logger = logging.getLogger(__name__)


def extract_customers() -> pd.DataFrame:

    query = """
        SELECT *
        FROM customers
    """

    logger.info("Extracting customers from operational database")

    engine = get_engine()

    customers_df = pd.read_sql(query, engine)

    logger.info(f"Extracted {len(customers_df)} customers")

    return customers_df

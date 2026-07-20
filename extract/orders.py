import logging

import pandas as pd

from database.connection import get_engine

logger = logging.getLogger(__name__)


def extract_orders() -> pd.DataFrame:

    query = """
        SELECT *
        FROM orders
    """

    logger.info("Extracting orders from operational database")

    engine = get_engine()

    orders_df = pd.read_sql(query, engine)

    logger.info(f"Extracted {len(orders_df)} orders")

    return orders_df

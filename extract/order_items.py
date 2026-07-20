import logging

import pandas as pd

from database.connection import get_engine

logger = logging.getLogger(__name__)


def extract_order_items() -> pd.DataFrame:

    query = """
        SELECT *
        FROM order_items
    """

    logger.info("Extracting order items from operational database")

    engine = get_engine()

    order_items_df = pd.read_sql(query, engine)

    logger.info(f"Extracted {len(order_items_df)} order items")

    return order_items_df

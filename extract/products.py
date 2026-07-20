import logging

import pandas as pd

from database.connection import get_engine

logger = logging.getLogger(__name__)


def extract_products() -> pd.DataFrame:

    query = """
        SELECT *
        FROM products
    """

    logger.info("Extracting products from operational database")

    engine = get_engine()

    products_df = pd.read_sql(query, engine)

    logger.info(f"Extracted {len(products_df)} products")

    return products_df

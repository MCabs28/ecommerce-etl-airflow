import logging

from database.connection import get_engine
from database.operations import truncate_table

logger = logging.getLogger(__name__)


def load_order_items(df):

    engine = get_engine()

    truncate_table("analytics_order_items")

    df.to_sql(
        name="analytics_order_items",
        con=engine,
        if_exists="append",
        index=False,
    )

    logger.info(f"Loaded {len(df)} order items into analytics_order_items")

import logging

from database.connection import get_engine
from database.operations import truncate_table

logger = logging.getLogger(__name__)


def load_orders(df):

    engine = get_engine()

    truncate_table("analytics_orders")

    df.to_sql(
        name="analytics_orders",
        con=engine,
        if_exists="append",
        index=False,
    )

    logger.info(f"Loaded {len(df)} orders into analytics_orders")

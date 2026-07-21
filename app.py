import logging

from utils.logger import configure_logging

from pipelines.customers import customers_pipeline
from pipelines.products import products_pipeline
from pipelines.orders import orders_pipeline
from pipelines.order_items import order_items_pipeline

# Configure logging once when the application starts
configure_logging()

# Create a logger for this module
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Ecommerce ETL Pipeline")

    customers_pipeline()

    products_pipeline()

    orders_pipeline()

    order_items_pipeline()

    logger.info("ETL Pipeline Completed Successfully")


if __name__ == "__main__":
    main()

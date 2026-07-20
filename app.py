import logging

from utils.logger import configure_logging

from extract.customers import extract_customers
from extract.products import extract_products
from extract.orders import extract_orders
from extract.order_items import extract_order_items

from transform.customers import transform_customers
from transform.products import transform_products
from transform.orders import transform_orders
from transform.order_items import transform_order_items

from load.customers import load_customers
from load.products import load_products
from load.orders import load_orders
from load.order_items import load_order_items

# Configure logging once when the application starts
configure_logging()

# Create a logger for this module
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Ecommerce ETL Pipeline")

    # ==========================
    # Customers ETL
    # ==========================
    customers_df = extract_customers()
    customers_df = transform_customers(customers_df)
    load_customers(customers_df)

    # ==========================
    # Products ETL
    # ==========================
    products_df = extract_products()
    products_df = transform_products(products_df)
    load_products(products_df)

    # ==========================
    # Orders ETL
    # ==========================
    orders_df = extract_orders()
    orders_df = transform_orders(orders_df)
    load_orders(orders_df)

    # ==========================
    # Order Items ETL
    # ==========================
    order_items_df = extract_order_items()
    order_items_df = transform_order_items(order_items_df)
    load_order_items(order_items_df)

    logger.info("ETL Pipeline Completed Successfully")


if __name__ == "__main__":
    main()

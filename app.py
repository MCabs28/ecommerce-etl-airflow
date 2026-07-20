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


def main():
    print("========== Ecommerce ETL Pipeline ==========\n")

    # Customers
    customers_df = extract_customers()
    customers_df = transform_customers(customers_df)
    load_customers(customers_df)

    # Products
    products_df = extract_products()
    products_df = transform_products(products_df)
    load_products(products_df)

    # Orders
    orders_df = extract_orders()
    orders_df = transform_orders(orders_df)
    load_orders(orders_df)

    # Order Items
    order_items_df = extract_order_items()
    order_items_df = transform_order_items(order_items_df)
    load_order_items(order_items_df)

    print("\n✅ ETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    main()

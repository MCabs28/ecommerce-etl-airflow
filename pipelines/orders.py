from extract.orders import extract_orders
from transform.orders import transform_orders
from load.orders import load_orders


def orders_pipeline():
    orders_df = extract_orders()

    orders_df = transform_orders(orders_df)

    load_orders(orders_df)

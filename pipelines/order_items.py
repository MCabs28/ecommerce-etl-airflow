from extract.order_items import extract_order_items
from transform.order_items import transform_order_items
from load.order_items import load_order_items


def order_items_pipeline():
    order_items_df = extract_order_items()

    order_items_df = transform_order_items(order_items_df)

    load_order_items(order_items_df)

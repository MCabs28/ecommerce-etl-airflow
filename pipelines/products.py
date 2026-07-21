from extract.products import extract_products
from transform.products import transform_products
from load.products import load_products


def products_pipeline():
    products_df = extract_products()

    products_df = transform_products(products_df)

    load_products(products_df)

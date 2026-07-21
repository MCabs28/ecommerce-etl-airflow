from extract.customers import extract_customers
from transform.customers import transform_customers
from load.customers import load_customers


def customers_pipeline():
    customers_df = extract_customers()

    customers_df = transform_customers(customers_df)

    load_customers(customers_df)

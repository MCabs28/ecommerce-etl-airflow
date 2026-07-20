from database.connection import get_engine
from database.operations import truncate_table


def load_products(df):
    engine = get_engine()

    truncate_table("analytics_products")

    df.to_sql(
        name="analytics_products",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(f"Loaded {len(df)} products.")

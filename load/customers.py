from database.connection import get_engine
from database.operations import truncate_table


def load_customers(df):
    engine = get_engine()

    truncate_table("analytics_customers")

    df.to_sql(
        name="analytics_customers",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(f"Loaded {len(df)} customers.")

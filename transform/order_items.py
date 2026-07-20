import pandas as pd


def transform_order_items(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate order item data.
    """

    df = df.copy()

    # Ensure numeric types
    df["quantity"] = pd.to_numeric(df["quantity"])
    df["unit_price"] = pd.to_numeric(df["unit_price"])

    # Keep only valid quantities
    df = df[df["quantity"] > 0]

    # Keep only valid prices
    df = df[df["unit_price"] >= 0]

    # Remove rows with missing required values
    df = df.dropna(
        subset=[
            "order_id",
            "product_id",
            "quantity",
            "unit_price",
        ]
    )

    return df

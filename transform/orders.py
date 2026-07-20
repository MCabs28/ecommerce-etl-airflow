import pandas as pd

VALID_STATUSES = {"Pending", "Shipped", "Delivered", "Cancelled"}


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate order data.
    """

    df = df.copy()

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Standardize order status
    df["order_status"] = df["order_status"].str.strip().str.title()

    # Ensure numeric type
    df["total_amount"] = pd.to_numeric(df["total_amount"])

    # Remove invalid amounts
    df = df[df["total_amount"] >= 0]

    # Keep only valid statuses
    df = df[df["order_status"].isin(VALID_STATUSES)]

    # Remove rows with missing required values
    df = df.dropna(subset=["customer_id", "order_date", "order_status", "total_amount"])

    return df

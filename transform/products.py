import pandas as pd


def transform_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate product data.
    """

    df = df.copy()

    # Remove extra whitespace
    df["product_name"] = df["product_name"].str.strip()
    df["category"] = df["category"].str.strip()

    # Standardize category names
    df["category"] = df["category"].str.title()

    # Ensure numeric types
    df["price"] = pd.to_numeric(df["price"])
    df["stock_quantity"] = pd.to_numeric(df["stock_quantity"])

    # Remove invalid products
    df = df[df["price"] >= 0]
    df = df[df["stock_quantity"] >= 0]

    # Remove rows with missing required values
    df = df.dropna(subset=["product_name", "category", "price", "stock_quantity"])

    return df

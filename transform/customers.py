import pandas as pd


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate customer data.
    """

    # Make a copy to avoid modifying the original DataFrame
    df = df.copy()

    # Normalize email addresses
    df["email"] = df["email"].str.lower().str.strip()

    # Remove extra spaces
    df["first_name"] = df["first_name"].str.strip()
    df["last_name"] = df["last_name"].str.strip()
    df["city"] = df["city"].str.strip()

    # Convert created_at to datetime
    df["created_at"] = pd.to_datetime(df["created_at"])

    # Remove duplicate customers
    df = df.drop_duplicates()

    # Remove rows with missing required values
    df = df.dropna(subset=["first_name", "last_name", "email"])

    return df

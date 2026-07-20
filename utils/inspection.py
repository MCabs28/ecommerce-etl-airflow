import pandas as pd


def inspect_dataframe(name: str, df: pd.DataFrame):
    print("=" * 50)
    print(f"{name}")
    print("=" * 50)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows")
    print(df.head())

    print("\n")

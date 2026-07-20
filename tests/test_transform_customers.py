import pandas as pd

from transform.customers import transform_customers


def test_email_is_normalized():
    data = {
        "customer_id": [1],
        "first_name": [" Mark "],
        "last_name": [" Cabael "],
        "email": [" MARK@GMAIL.COM "],
        "city": [" San Pedro "],
        "created_at": ["2024-01-01"],
    }

    df = pd.DataFrame(data)

    result = transform_customers(df)

    assert result.iloc[0]["email"] == "mark@gmail.com"


def test_names_are_trimmed():
    data = {
        "customer_id": [1],
        "first_name": [" Mark "],
        "last_name": [" Cabael "],
        "email": ["mark@gmail.com"],
        "city": [" San Pedro "],
        "created_at": ["2024-01-01"],
    }

    df = pd.DataFrame(data)

    result = transform_customers(df)

    assert result.iloc[0]["first_name"] == "Mark"
    assert result.iloc[0]["last_name"] == "Cabael"
    assert result.iloc[0]["city"] == "San Pedro"


def test_duplicate_customers_are_removed():
    data = {
        "customer_id": [1, 1],
        "first_name": ["Mark", "Mark"],
        "last_name": ["Cabael", "Cabael"],
        "email": ["mark@gmail.com", "mark@gmail.com"],
        "city": ["San Pedro", "San Pedro"],
        "created_at": ["2024-01-01", "2024-01-01"],
    }

    df = pd.DataFrame(data)

    result = transform_customers(df)

    assert len(result) == 1


def test_missing_required_fields_are_removed():
    data = {
        "customer_id": [1],
        "first_name": [None],
        "last_name": ["Cabael"],
        "email": ["mark@gmail.com"],
        "city": ["San Pedro"],
        "created_at": ["2024-01-01"],
    }

    df = pd.DataFrame(data)

    result = transform_customers(df)

    assert result.empty


def test_invalid_dates_are_removed():
    data = {
        "customer_id": [1],
        "first_name": ["Mark"],
        "last_name": ["Cabael"],
        "email": ["mark@gmail.com"],
        "city": ["San Pedro"],
        "created_at": ["not-a-date"],
    }

    df = pd.DataFrame(data)

    result = transform_customers(df)

    assert result.empty

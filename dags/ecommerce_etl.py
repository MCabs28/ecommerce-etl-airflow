import os
import sys

PROJECT_ROOT = "/opt/airflow/project"

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from datetime import datetime, timedelta

from airflow import DAG
from airflow.sdk import task

from pipelines import (
    customers_pipeline,
    products_pipeline,
    orders_pipeline,
    order_items_pipeline,
)

default_args = {
    "owner": "mark",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="ecommerce_etl",
    description="Daily ETL pipeline for the ecommerce analytics database.",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "ecommerce", "postgres", "pandas"],
) as dag:

    @task(execution_timeout=timedelta(minutes=10))
    def customers_task():
        """Run the customers ETL pipeline."""
        customers_pipeline()

    @task(execution_timeout=timedelta(minutes=10))
    def products_task():
        """Run the products ETL pipeline."""
        products_pipeline()

    @task(execution_timeout=timedelta(minutes=10))
    def orders_task():
        """Run the orders ETL pipeline."""
        orders_pipeline()

    @task(execution_timeout=timedelta(minutes=10))
    def order_items_task():
        """Run the order items ETL pipeline."""
        order_items_pipeline()

    customers = customers_task()
    products = products_task()
    orders = orders_task()
    order_items = order_items_task()

    customers >> products >> orders >> order_items

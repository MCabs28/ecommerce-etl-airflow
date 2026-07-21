from airflow.decorators import task
from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="ecommerce_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    @task
    def hello():
        print("Airflow is orchestrating my ETL pipeline!")

    hello()

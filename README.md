# Ecommerce ETL Pipeline with Apache Airflow

A batch ETL pipeline that extracts e-commerce sales data from Excel, transforms it using Python, loads it into PostgreSQL, and orchestrates the workflow with Apache Airflow.

**Project Status:** In Progress

## Project Overview

This project simulates a real-world Data Engineering workflow for an e-commerce business. The pipeline processes sales data from Excel files, performs data cleaning and transformation, loads the data into PostgreSQL, and automates the entire process using Apache Airflow.

The goal of this project is to demonstrate modern Data Engineering practices, including containerized development, modular ETL design, SQL analytics, dbt transformations, and workflow orchestration.

## Tech Stack

* Python
* PostgreSQL
* Apache Airflow
* Docker & Docker Compose
* SQL
* Pandas
* OpenPyXL
* DBeaver
* Git & GitHub

## Project Structure

```text
ecommerce-etl-airflow/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── db_connection.py
│
├── extract/
├── transform/
├── load/
├── logs/
├── utils/
│
├── app.py
├── config.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```



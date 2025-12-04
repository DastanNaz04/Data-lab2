from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

PROJECT_PATH = "/opt/airflow/project/src"

def run_scraper():
    subprocess.run(["python", f"{PROJECT_PATH}/scraper.py"], check=True)

def run_cleaner():
    subprocess.run(["python", f"{PROJECT_PATH}/cleaner.py"], check=True)

def run_loader():
    subprocess.run(["python", f"{PROJECT_PATH}/loader.py"], check=True)

with DAG(
    dag_id="coinmarketcap_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["coinmarketcap"],
) as dag:

    scraper = PythonOperator(
        task_id="scrape_data",
        python_callable=run_scraper,
    )

    cleaner = PythonOperator(
        task_id="clean_data",
        python_callable=run_cleaner,
    )

    loader = PythonOperator(
        task_id="load_data",
        python_callable=run_loader,
    )

    scraper >> cleaner >> loader

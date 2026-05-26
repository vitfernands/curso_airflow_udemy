import pendulum
from datetime import datetime
from airflow import DAG, Dataset
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

with DAG (
    dag_id="producer",
    description="Entendendo producer",
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 26, tz='America/Sao_Paulo'),
    catchup=False
) as dag:
    
    def create_dataset_file():
        dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=';')
        dataset.to_csv("/opt/airflow/data/Churn_new.csv", sep=';', index=False)

    task1 = PythonOperator(
        task_id="task1",
        python_callable=create_dataset_file,
        outlets=[mydataset]
    )

    task1
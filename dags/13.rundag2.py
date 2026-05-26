from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator 

with DAG (
    dag_id="dagrun2",
    description="Dagrun2",
    schedule=None,
    start_date=datetime(2026, 5, 17),
    catchup=False
) as dag:
    
    task1 = BashOperator(task_id="tsk1", bash_command='echo "{{ dag_run.conf["Chave"] }}"')

    task2 = BashOperator(task_id="tsk2", bash_command='sleep 5')

    task1 >> task2
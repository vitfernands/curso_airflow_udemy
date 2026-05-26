from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

with DAG (
    dag_id="dagrun1",
    description="Dagrun1",
    schedule=None,
    start_date=datetime(2026, 5, 17),
    catchup=False
) as dag:
    
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = TriggerDagRunOperator(
        task_id="tsk2",
        trigger_dag_id="dagrundag2",
        conf={"Chave": "Valor"},
        wait_for_completion=True,
        poke_interval=5
    )

    task1 >> task2
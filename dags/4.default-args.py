import pendulum
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "depends_on_past": False,
    "email": ["teste@email.com"],
    "email_on_fail": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10)
}

with DAG (
    dag_id="default_args_4",
    description="Entedendo Default Args",
    default_args = default_args,
    schedule=None,
    start_date=pendulum.datetime(2026, 3, 30,tz="America/Sao_Paulo"),
    catchup=False,
    tags=["args", "curso", "exemplo_args"]
) as dag:
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", retries=3)
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")

    task1 >> task2 >> task3
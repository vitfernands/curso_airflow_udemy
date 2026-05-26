import pendulum
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "depends_on_past": False,
    "email": ["vitfernands@gmail.com"],
    "email_on_fail": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG (
    dag_id="test_email_failure_error",
    description="Testando funcionamento de email",
    default_args = default_args,
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 17,tz="America/Sao_Paulo"),
    catchup=False,
    tags=["args", "curso", "email"]
) as dag:
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")

    task1 >> task2 >> task3
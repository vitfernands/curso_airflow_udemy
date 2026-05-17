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
    dag_id="dag_complexa",
    description="Dag complexa",
    default_args = default_args,
    schedule=None,
    start_date=pendulum.datetime(2026, 3, 30,tz="America/Sao_Paulo"),
    catchup=False,
    tags=["curso", "dag complexa"]
) as dag:
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 5")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 5")
    task6 = BashOperator(task_id="tsk6", bash_command="sleep 5")
    task7 = BashOperator(task_id="tsk7", bash_command="sleep 5")
    task8 = BashOperator(task_id="tsk8", bash_command="sleep 5")
    task9 = BashOperator(task_id="tsk9", bash_command="sleep 5")

    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6 >> [task7, task8, task9]
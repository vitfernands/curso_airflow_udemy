import pendulum
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG (
    dag_id="empty_operator1",
    description="Usando EmptyOperator",
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 17, tz='America/Sao_Paulo'),
    catchup=False
) as dag:
    
    task1 = BashOperator(task_id="tsk1", bash_command='sleep 5')
    
    task2 = BashOperator(task_id="tsk2", bash_command='sleep 5')

    task3 = BashOperator(task_id="tsk3", bash_command='sleep 5')
    
    task4 = BashOperator(task_id="tsk4", bash_command='sleep 5')
    
    task5 = BashOperator(task_id="tsk5", bash_command='sleep 5')

    taskempty = EmptyOperator(
        task_id='tskempty'
    )

    [task1, task2, task3] >> taskempty >> [task4, task5]
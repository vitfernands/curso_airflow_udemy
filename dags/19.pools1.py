import pendulum
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG (
    dag_id="pools_1",
    description="Utilizando pools",
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 18, tz='America/Sao_Paulo'),
    catchup=False
) as dag:
    
    task_leve = BashOperator(
        task_id='task_leve',
        bash_command='sleep 5',
        pool='meupool',
        priority_weight=1,
        weight_rule='absolute'
    )

    task_media = BashOperator(
        task_id='task_media',
        bash_command='sleep 5',
        pool='meupool',
        priority_weight=5,
        weight_rule='absolute'
    )

    task_pesada = BashOperator(
        task_id='task_pesada',
        bash_command='sleep 5',
        pool='meupool',
        pool_slots=2,
        priority_weight=10,
        weight_rule='absolute'
    )
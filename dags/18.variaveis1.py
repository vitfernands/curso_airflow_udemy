import pendulum
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.models import Variable


with DAG (
    dag_id="variaveis_1",
    description="Utilizando variaveis",
    schedule=None,
    start_date=pendulum.datetime(2026, 5, 17, tz='America/Sao_Paulo'),
    catchup=False
) as dag:
    
    def print_variable():
        minha_var = Variable.get("minhavar")
        print(f"Valor da variavel: {minha_var}")
    
    task1 = PythonOperator(
        task_id='tsk1',
        python_callable=print_variable
    )

    task1
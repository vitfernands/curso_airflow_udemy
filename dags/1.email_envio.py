from airflow import DAG
from airflow.providers.smtp.operators.smtp.EmailOperator import EmailOperator
from datetime import datetime

with DAG (
    dag_id="teste_envio_email",
    description="Testando envio de emails",
    schedule=None,
    start_date=datetime(2026, 5, 17),
    catchup=False,
    tags=["curso", "exemplo", "email"]
) as dag:
    EmailOperator(
        task_id='send_email',
        to=['vitfernands@gmail.com'],
        subject='TESTANDO EMAIL AIRFLOW',
        html_content='<p>Email enviado com sucesso pelo Airflow</p>',
    )
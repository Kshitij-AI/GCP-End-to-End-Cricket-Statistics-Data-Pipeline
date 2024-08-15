from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner':'airflow',
    'start_date':datetime(2024,8,10),
    'retries': 1,
    'retry_delay': timedelta(seconds=15)
}

with DAG('push_data_to_gcs',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    t1 = BashOperator(
        task_id='extract_and_push_data_to_gcs',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push.py')
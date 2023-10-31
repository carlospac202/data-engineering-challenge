from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from etl_process import EtlProcess


default_args = {
    'owner': 'carlos_pacheco',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ETL_DAG',
    default_args=default_args,
    schedule_interval='0 0 * * *',  # Adjust the schedule as needed
    catchup=False,
)

def run_etl():
    etl = EtlProcess()
    etl.process()


etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)

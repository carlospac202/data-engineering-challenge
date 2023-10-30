from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from etl_process import EtlProcess

default_args = {
    'owner': 'carlos_pac',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 29),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ETL_DAG',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Adjust the schedule as needed
)


def run_etl():
    etl = EtlProcess()
    etl.process()


etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)

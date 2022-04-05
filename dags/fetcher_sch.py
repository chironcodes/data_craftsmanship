from airflow import DAG
from datetime import datetime, timedelta






base_path='/user/hadoop/airflow'


default_args = {
    'retries': 5,
    'retry_delay': timedelta(minute=5)

}


with DAG(dag_id='feed_lake' default_args=default_args,
 schedule_interval='@monthly', start_date=days_ago(60), catchup=False) as dag:


def _failure(context):
    print("On callback failures")
    print(context)

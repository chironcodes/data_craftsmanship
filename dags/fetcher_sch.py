from airflow import DAG
from datetime import date, datetime, timedelta
from airflow.utils.dates import days_ago


from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor


staging_folder = '/home/hadoop/staging'
base_path_hdfs='/user/hadoop/airflow'


default_args = {
    'retries': 5,
    'retry_delay': timedelta(minutes=5),

    'email': ['chiron@github.com'],
    'email_on_retry': False ,
    'email_on_failure': False
}


# we use mainly 'handlebars' for params
hdfs_bash_exists = """hdfs dfs -test -d {{ params.path }};
                        if [ $? -eq 0 ]
                        then
                            echo "True."
                        else
                            echo "False."
                        fi
"""


with DAG(dag_id='staging_to_dlake', default_args=default_args,
 schedule_interval='@monthly', start_date=days_ago(30), catchup=False) as dag:

  
    def _failure(context):
        print("On callback failures")
        print(context)


    #check if path exists R->True/False
    hdfs_check_folder = BashOperator(
        task_id='hdfs_check_folder',
        bash_command=hdfs_bash_exists,
        params={'path' : base_path_hdfs},
    )
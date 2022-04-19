from airflow import DAG
from datetime import date, datetime, timedelta
from airflow.utils.dates import days_ago


from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor


staging_folder = '/home/hadoop/staging'
base_path_hdfs='/user/hadoop/airflow'


year,month, day = date.today().strftime('%Y.%m.%d').split('.')


def _failure(context):
    print("On callback failures")
    print(f"task { ti.task_id } failed in dag { ti.dag_id }")

default_args = {
    'retries': 5,
    'retry_delay': timedelta(minutes=5),

    'email': ['chiron@github.com'],
    'email_on_retry': False ,
    'on_failure_callback': _failure,
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

hdfs_bash_mkdir = """hdfs dfs -mkdir {{ params.path }}"""


with DAG(dag_id='stage_to_dlake', default_args=default_args,
 schedule_interval='@monthly', start_date=days_ago(30), catchup=False) as dag:

  

    staging_area_sensor = FileSensor(
        task_id= 'staging_area_sensor',
        fs_conn_id='my_staging_area',
        filepath='*',
        poke_interval=5,
        timeout=20
    )

    
    # hdfs_check_folder = BashOperator(
    #     task_id='hdfs_check_folder',
    #     bash_command=hdfs_bash_exists,
    #     params={'path' : base_path_hdfs+f'/{month}'},
    # )


    hdfs_mkdir_folder = BashOperator(
        task_id='hdfs_mkdir_folder',
        bash_command=hdfs_bash_mkdir,
        params={'path': base_path_hdfs+f'/{month}'}
    )

    
    move_dlake = BashOperator (
        task_id='move_dlake',
        bash_command=("hdfs dfs -put -f {{params.staging_folder}}/* {{params.base_path_hdfs}}"),
        params={'staging_folder':staging_folder,'base_path_hdfs':base_path_hdfs},
    )


staging_area_sensor >> hdfs_mkdir_folder >> move_dlake



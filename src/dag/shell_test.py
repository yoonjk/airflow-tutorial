from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
import pendulum

local_tz = pendulum.timezone("Asia/Seoul")

default_args= {
    'start_date': days_ago(1),
    'retries': 0,
    'catchup': False,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
        'shell_test', 
        default_args=default_args, 
        schedule_interval="@daily",
)

# Task 1
dummy_task = DummyOperator(task_id='dummy_task', retries=1, dag=dag)
# Task 2
bash_task = BashOperator(task_id='bash_task', bash_command="$AIRFLOW_HOME/dags/command.sh ", dag=dag)

dummy_task >> bash_task
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG(
	'shell_test', 
	schedule_interval="0 1 * * *", 
	start_date=datetime(2021, 8, 31), 
	catchup=False,
)

# Task 1
dummy_task = DummyOperator(task_id='dummy_task', retries=1, dag=dag)
# Task 2
bash_task = BashOperator(task_id='bash_task', bash_command="$AIRFLOW_HOME/dags/command.sh ", xcom_push=True, dag=dag)

dummy_task >> bash_task
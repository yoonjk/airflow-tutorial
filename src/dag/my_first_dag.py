# We'll start by importing the DAG object
from airflow import DAG 
from datetime import timedelta
# We need to import the operators used in our tasks
from airflow.operators.bash_operator import BashOperator
# We then import the days_ago function
from airflow.utils.dates import days_ago

# initializing the default arguments that we'll pass to our DAG
default_args = {
	'owner': 'airflow',
	'start_date': days_ago(2),
	'retries': 1,
	'retry_delay': timedelta(minutes=5),
}

my_first_dag = DAG(
	'first_dag',
	default_args=default_args,
	description='My First DAG',
	schedule_interval=None,
)

task_1 = BashOperator(
	task_id='first_task',
	bash_command='echo 1',
	dag=my_first_dag
)

task_2 = BashOperator(
	task_id='second_task',
	bash_command='echo 2',
	dag=my_first_dag,
)

task_1.set_downstream(task_2)
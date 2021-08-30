from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
	'owner': 'airflow',
	'start_date': days_ago(2),
	'retries': 1,
	'retry_delay': timedelta(minutes=5),
}

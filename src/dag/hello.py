from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
	return 'Hello world from first Airflow DAG!'

dag = DAG('hello', description='Hello World DAG',
		  schedule_interval='0 10 * * *',
		  start_date=datetime(2021, 8, 23), catchup=False)

hello_operator = PythonOperator(task_id='hello', python_callable=print_hello, dag=dag)

hello_operator

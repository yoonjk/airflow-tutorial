from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta

dag = DAG('hello-world',description='Hello world DAG',
          schedule_interval = '* 1 * * *',
          start_date=datetime(2021,8,21),catchup=False)

def print_hello():
    return 'Hello world'

python_task = PythonOperator(
                    task_id='python_operator',
                    python_callable = print_hello,
                    dag = dag)

bash_task = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag)

bash_task.set_downstream(python_task)
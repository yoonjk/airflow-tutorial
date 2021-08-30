from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'admin',
}

dag = DAG(
    dag_id='demo_test',
    default_args=args,
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=1),
    schedule_interval='0 1 * * *',
)

templated_command = """
$HOME/airflow/make_csv.sh
"""

# [START howto_operator_bash]
run_this = BashOperator(
    task_id='bash_test',
    bash_command=templated_command,
    dag=dag,
)
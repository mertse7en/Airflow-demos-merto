from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from random import uniform
from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('structure', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    downloading_data = BashOperator(
        task_id='api_request',
        bash_command='sleep 3'
    )

    with TaskGroup('fetch_report') as fetch_report:
            fetch_1 = BashOperator(
                task_id='fetch_report_1',
                bash_command='sleep 3'
            )

            fetch_2 = BashOperator(
                task_id='fetch_report_2',
                bash_command='sleep 3'
            )

            fetch_3 = BashOperator(
                task_id='fetch_report_3',
                bash_command='sleep 3'
            )

            push_1 = BashOperator(
                task_id='push_report_1',
                bash_command='sleep 3'
            )

            push_2 = BashOperator(
                task_id='push_report_2',
                bash_command='sleep 3'
            )

            push_3 = BashOperator(
                task_id='push_report_3',
                bash_command='sleep 3'
            )

    downloading_data >> fetch_1, fetch_2, fetch_3 >> push_1, push_2, push_3

        
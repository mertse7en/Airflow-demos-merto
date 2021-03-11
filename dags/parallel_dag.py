from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 3)
    # 'owner': 'airflow',
    # 'depends_on_past': False,
    # 'email': ['airflow@example.com'],
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG('parallel_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    # Tasks
    task_1 = BashOperator(
        task_id = 'task1',
        bash_command ='sleep 3'
    )

    task_2 = BashOperator(
        task_id = 'task2',
        bash_command ='sleep 3'
    )

    task_3 = BashOperator(
        task_id = 'task3',
        bash_command ='sleep 3'
    )

    task_4 = BashOperator(
        task_id = 'task4',
        bash_command ='sleep 3'
    )

    task_1 >>  [task_2, task_3] >> task_4        ## task_2 task_3 can be executed paralel

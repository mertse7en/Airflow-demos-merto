from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor


from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1),
    'email': ['mert.seven@trt.net.tr'],
    'email_on_failure': True
}

with DAG('appfollow-scrapper', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    task_is_site_accesible = HttpSensor(
        task_id = 'is_site_accessible',
        http_conn_id = 'appfollow_api',
        endpoint = ''
    )

    

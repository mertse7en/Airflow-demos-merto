from datetime import datetime
import io
import requests
import json
import os
import pandas as pd
import urllib

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.postgres_operator import PostgresOperator

from Python.appsflyer_etl import etl_function
from Python.kafka import kafka_push,kafka_read

default_args = {
    'start_date': datetime(2020, 1, 1)
}


with DAG('fetch_report', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    # Tasks

    task_is_api_available = HttpSensor(
        task_id = 'is_api_available',
        http_conn_id = 'appsflyer_api', # ur
        endpoint = ''
    )

    task_fetch_appsflyer = PythonOperator(
        task_id = 'fetch_appsflyer',
        python_callable = (etl_function) # Callable function name ...
    )

    # task_create_table = PostgresOperator(
    #     task_id = 'create_table'
    # ) 

    task_push_kafka = PythonOperator(
        task_id = 'push_kafka',
        python_callable = (kafka_push)
    )

    task_read_from_kafka = PythonOperator(
        task_id = 'read_from_kafka',
        python_callable = (kafka_read)
    )
    
    
    task_is_api_available >> task_fetch_appsflyer >> task_push_kafka >> task_read_from_kafka
    
    # Simply doing same thing with the http operator
       
    # task_fetch_data = SimpleHttpOperator(
    #     task_id = 'fetch_data',
    #     http_conn_id = 'appsflyer_api',
    #     endpoint = '',
    #     method = 'GET',
    #     response_filter = lambda response : response,
    #     log_response = True
    # )


    # task_processing_report = PythonOperator(
    #     task_id = 'processing_report',
    #     python_callable = (processing_report) # Callable function name ...
    # ) 


    









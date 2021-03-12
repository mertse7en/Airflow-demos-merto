import pandas as pd
import socket
import time
import os

from confluent_kafka import Producer


def kafka_push(**kwargs):
    # Create task instance
    ti = kwargs['ti']
    # Took the data from 'fetch_appsflyer' task
    pulled_df = ti.xcom_pull(task_ids='fetch_appsflyer')
    # Convert into df
    pulled_df = pd.DataFrame.from_dict(pulled_df)
    print(pulled_df)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Kafka Part
    topic_name = "airflow-test"
    conf = {'bootstrap.servers':["--------------------------"],
            'client.id':socket.gethostname()}

    print("topic_name :{}".format(topic_name))
    producer = Producer(conf)

    string_ex = ''
    # Method to gather each columns and push kafka one by one
    # Key value may be added
    for index, row in pulled_df.iterrows():
        string_ex = ""
        # dict1 = {}
        for i in range(0, pulled_df.shape[1]):
            string_ex = string_ex +  str(row[i]) + ','

        print("The file will be produced is : {}".format(string_ex))
        producer.produce(topic_name, string_ex)
        producer.flush()



def kafka_read():
    print("Hello world for now !!!")
